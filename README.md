Amsel
===========

A huge problem in the current Ebola outbreak in West Africa is the traceability of people that have been admitted to health facilities. Unfortunately it is a very common case that health workers pick up infected people, admit them to a health facility and the person dies without the family knowing which facility the person was admitted to or where they are buried. 

**We want to change this!**

Through assigning a unique number to every patient, on first contact and share this with the family, we can offer a text base (SMS) service that family members can query to find out the status of their loved ones. 

- See [doc/install.md](doc/install.md) for how to run the prototype
- See [doc/services.md](doc/services.md) for a list of services we are currently using
- See [core/api/README.md](core/api/README.md) for an overview of the API

Please keep all discussions on Github with the issues. Otherwise feel free to email us under didi.hoffmann@ehealthnigeria.org 

Amsel => A miniature sms ebola lifeline

## Current flow

### Data entry

1. A health care worker adds a new patient trough odk collect
1. They add the health care worker's mobile number and the number of the family member or relative as well as some personal data
1. As soon as the form is submitted the formhub server triggers a web hook
1. This assigns the patient a unique number/id and sends a text message to both the relative and health care worker

### Data modification

1. A very simple dashboard is available (/admin) for health care workers to update patient data

### Data retrieval 

1. An SMS is sent to a twilio number
1. This is then redirected to RapidPro which starts a flow
1. The flow asks for the number and calls /query (on the server) with the number and retrieves the data
1. Replies to the relative asking


# Contribute

Please check out the [issues](https://github.com/eHealthAfrica/Amsel/issues) we are currently workin on. Feel free to ask questions if you don't understand, or something is not quite clear. If you want some explanation please just email us and we can work on the details. 

[About us](https://github.com/eHealthAfrica/jobs/blob/master/what-we-do.md)

Licensed under the [Apache License Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt).
