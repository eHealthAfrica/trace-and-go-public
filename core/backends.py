from django.core.exceptions import ValidationError
from django.utils.html import escape

import phonenumbers

import json
import requests


def get_phone_obj(to):
    from django.conf import settings

    country_code = getattr(settings, "COUNTRY_CODE")

    try:
        pnumber = phonenumbers.parse(to, country_code)

        if not phonenumbers.is_valid_number(pnumber):
            #If it is invalid let someone else deal with it
            return to

        #Everything seams to be ok so we return a nice E164 number
        return phonenumbers.format_number(pnumber, phonenumbers.PhoneNumberFormat.E164)

    except phonenumbers.phonenumberutil.NumberParseException:
        #TODO: In the futre we need some sort of way to notify people that the number is wrong. For now don't fail
        return to


def sms_send_textit(to, message):
    post_url = "https://api.textit.in/api/v1/sms.json"

    #Clean the number (Add area code etc ... )
    to = get_phone_obj(to)

    params = {
        'phone': to,
        'text': escape(message)
    }

    if len(params["text"]) >= 480:
        raise ValidationError("The text can not be longer than 480 chars.")

    data = json.dumps(params)

    from django.conf import settings

    api_token = getattr(settings, "TEXTIT_AUT")

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': 'Token ' + str(api_token),
    }

    response = requests.post(post_url,
                             data=data,
                             headers=headers)

    return response.json()

def sms_send_rapidpro(to, message):
    post_url = "https://rapidpro.io/api/v1/messages.json"

    #Clean the number (Add area code etc ... )
    to = get_phone_obj(to)

    params = {
        'phone': to,
        'text': escape(message)
    }

    if len(params["text"]) >= 480:
        raise ValidationError("The text can not be longer than 480 chars.")

    data = json.dumps(params)

    from django.conf import settings

    api_token = getattr(settings, "RAPIDPRO_AUT")

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': 'Token ' + str(api_token),
    }

    response = requests.post(post_url,
                             data=data,
                             headers=headers)

    return response.json()


import telerivet


def sms_send_telerivet(to, message):
    from django.conf import settings

    #Clean the number (Add area code etc ... )
    to = get_phone_obj(to)

    # from https://telerivet.com/dashboard/api
    API_KEY = getattr(settings, "API_KEY")
    PROJECT_ID = getattr(settings, "PROJECT_ID")

    if len(message) >= 480:
        raise ValidationError("The text can not be longer than 480 chars.")

    tr = telerivet.API(API_KEY)

    project = tr.initProjectById(PROJECT_ID)

    sent_msg = project.sendMessage(
        to_number=to,
        content=message
    )

    return sent_msg


from twilio.rest import TwilioRestClient


def sms_send_twilio(to, message):
    from django.conf import settings

    #Clean the number (Add area code etc ... )
    to = get_phone_obj(to)

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = getattr(settings, "TW_SID")
    auth_token = getattr(settings, "TW_AUTH")
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=message,
                                     to=to,  # Replace with your phone number
                                     from_="+18609207016")  # Replace with your Twilio number

    return message


def sms_send_test(to, message):

    #Clean the number (Add area code etc ... )
    to = get_phone_obj(to)

    params = {
        'phone': to,
        'text': escape(message)
    }

    return json.dumps(params)

