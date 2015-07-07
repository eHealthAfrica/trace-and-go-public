# STATIC STRINGS
PATIENT_NO_INFO = "The system has not updated the location of the patient."
PATIENT_NOT_FOUND = 'We can not find a patient with that information id.'
INVALID_ID = 'This is not a valid info code. This is an automated service. Please only text your info code to this number to receive updates.'
TOO_MANY_REQUESTS = "Please only send one message at a time. This query was ignored"
TOO_MANY_REQUESTS_EVER = "You have sent too many requests from this number and have been blocked."
INITIAL_MESSAGE = "You will be notified of all changes in the status and location of your loved one."

# FORMAT STRINGS
REPLY_INFO = "Reply to this message with your Info Code %(info_code)s for updates about your loved one."
PATIENT_INFO = "The patient %(first_name)s %(last_name)s has the information code %(info_code)s."
PATIENT_LOCATION = "The patient %(first_name)s %(last_name)s is at %(health_facility)s."
PATIENT_STATUS = "The patient %(first_name)s %(last_name)s is currently %(status)s."

STATUS_MESSAGES = {
    'A': '%(name)s has just been admitted to %(health_facility)s.',
    'S': '%(name)s is currently stable.',
    'C': '%(name)s is currently not improving.',
    'G': '%(name)s is currently getting better.',
    'D': 'You will receive a call from a doctor about %(name)s.',
    'O': '%(name)s has been discharged.',
}


def get_reply_info_message(patient):
    return REPLY_INFO % {
        'info_code': patient.info_code,
    }


def get_patient_info_message(patient):
    return PATIENT_INFO % {
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'info_code': patient.info_code,
    }


def get_patient_location_message(patient):
    return PATIENT_LOCATION % {
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'health_facility': patient.health_facility,
    }


def get_patient_status_message(patient):
    name = '%(first_name)s %(last_name)s' % {'first_name': patient.first_name,
                                             'last_name': patient.last_name}
    status_message = STATUS_MESSAGES.get(patient.status, None)
    return status_message % {
        'name': name,
        'health_facility': patient.health_facility.name,
    }
