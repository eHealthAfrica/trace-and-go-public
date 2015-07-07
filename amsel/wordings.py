# STATIC STRINGS
patient_no_info = "The system has not updated the location of the patient."
patient_not_found = 'We can not find a patient with that information id.'
invalid_id = 'This is not a valid information id.'
too_many_requests = "Please only send one message at a time. This query was ignored"
too_many_requests_ever = "You have sent too many requests from this number and have been blocked."
initial_message = "You will be notified of all changes in the status and location of your loved one."

# FORMAT STRINGS
patient_info = "The patient %(first_name)s %(last_name)s has the information code %(info_code)s"
patient_location = "The patient %(first_name)s %(last_name)s is at %(health_facility)s"
patient_status = "The patient %(first_name)s %(last_name)s is currently %(status)s"

def get_patient_info_message(patient):
    return patient_info % {
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'info_code': patient.info_code,
    }

def get_patient_location_message(patient):
    return patient_location % {
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'health_facility': patient.health_facility,
    }

def get_patient_status_message(patient):
    return patient_status % {
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'status': patient.get_status_display(),
    }
