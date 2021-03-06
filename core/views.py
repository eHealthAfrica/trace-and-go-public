import amsel.wordings as wordings
from django.http.response import HttpResponse, HttpResponseForbidden,\
    HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from django.core.cache import cache
from models import Patient
import re
from core import tasks


def check_post_key(request):
    # If a post_key is specified in the settings we use
    # it as a "security" measure
    post_key = getattr(settings, "POST_KEY", None)

    if post_key:
        if "key" in request.GET:
            if request.GET["key"] != post_key:
                # The request has a key but it doesn't match
                return HttpResponseForbidden()
        else:
            # The post key is specified in the settings but not in the URL
            return HttpResponseBadRequest()

    return True


@require_POST
@csrf_exempt
def submit(request):
    from models import id_generator

    postKeyReturn = check_post_key(request)
    if postKeyReturn is not True:
        return postKeyReturn

    # Because the post is not indexed we have to check the key
    if len(unicode(request.body)) == 0:
        return HttpResponseBadRequest()

    # Check if it really json
    try:
        json_object = json.loads(unicode(request.body))
    except ValueError as e:
        print e  # TODO: use real logging
        # The json is not valid
        return HttpResponseBadRequest()

    pat = Patient()

    uid = id_generator()

    # Check if the uid exists
    while Patient.objects.filter(uid__iexact=uid).count() == 1:
        uid = id_generator()

    pat.uid = uid
    pat.first_name = json_object.get("first_name") or None
    pat.last_name = json_object.get("last_name") or None
    pat.moh_id = json_object.get("moh_id") or None
    pat.enter_number = json_object.get("enter_number") or None
    pat.caregiver_number = json_object.get("caregiver_number") or None

    pat.json = unicode(json_object)

    # Message is sent through the save method
    pat.save()

    return HttpResponse(uid)

# This is the regex that we use to identify a patient
PATIENT_REGEX = "^ *([A-Z0-9]{4}) *$"


@require_POST
@csrf_exempt
def smswebhook(request):
    """
    This is called by the sms gateway. For now this is rapidpro
    """

    # Check if the number is in the cache
    if not cache.get(request.POST["phone"]):
        # Only allow a call every 10 seconds
        cache.set(request.POST["phone"], '', 5)

        long_cache_name = "long_%s" % request.POST["phone"]

        if cache.get(long_cache_name):
            cache.set(long_cache_name, cache.get(long_cache_name) + 1)
        else:
            cache.set(long_cache_name, 1)

        if cache.get(long_cache_name) >= 25:
            params = {
                'phone': request.POST["phone"],
                'text': wordings.TOO_MANY_REQUESTS_EVER
            }
            return HttpResponse(json.dumps(params))
    else:
        params = {
            'phone': request.POST["phone"],
            'text': wordings.TOO_MANY_REQUESTS
        }
        return HttpResponse(json.dumps(params))

    sms_content = request.POST["text"]

    patient_code_regex = re.compile(PATIENT_REGEX)
    patient_codes = patient_code_regex.findall(sms_content)

    if len(patient_codes) == 1:
        # Seams to be a patient reference

        if Patient.objects.filter(info_code__iexact=sms_content).count() == 1:
            pat = Patient.objects.get(info_code__iexact=sms_content)

            if pat.health_facility:
                text = wordings.get_patient_location_message(pat)

                if pat.status:
                    text = wordings.get_patient_status_message(pat)
                    tasks.send_sms.delay(pat.contact_phone_number, text)

            else:
                text = wordings.PATIENT_NO_INFO

            params = {
                'phone': request.POST["phone"],
                'text': text
            }

        else:
            params = {
                'phone': request.POST["phone"],
                'text': wordings.PATIENT_NOT_FOUND
            }
    else:
        params = {
            'phone': request.POST["phone"],
            'text': wordings.INVALID_ID
        }

    return HttpResponse(json.dumps(params))
