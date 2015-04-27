Amsel (A miniature SMS Ebola lifeline)
===========

A huge problem in the current Ebola outbreak in West Africa is the traceability of people that have been admitted to health facilities. Unfortunately it is a very common case that health workers pick up infected people, admit them to a health facility and the person dies without the family knowing which facility the person was admitted to or where they are buried. 

**We want to change this!**

Through assigning a unique number to every patient, on first contact and share this with the family, we can offer a text base (SMS) service that family members can query to find out the status of their loved ones. 

- See [doc/install.md](doc/install.md) for how to run the prototype
- See [doc/services.md](doc/services.md) for a list of services we are currently using
- See [core/api/README.md](core/api/README.md) for an overview of the API

Please keep all discussions on Github with the issues. Otherwise feel free to email us at lucy.chambers@ehealthnigeria.org 

## Current flow

### Data entry

1. A health care worker adds a new patient through the online interface (connected to Formhub a.k.a. odk collect)
1. They add the case investigator's mobile number and the number of the family member or relative as well as some personal data
1. As soon as the form is submitted the formhub server triggers a web hook
1. This assigns the patient a unique number/id
2. 4 text messages are triggered: 


|To the relative (3 messages)   | To the case investigator (1 message) |   
|-----|-----|
|<ol><li> Gives the unique number,</li><li> Says: "You will be notified of all changes in the status and location of your loved one",</li> <li>Gives the location of the patient</li></ol> | 1. Gives the unique number (as above)  |

### Data modification

1. A very simple dashboard is available (/admin) for health care workers to update patient data. 
2. Updating the status of a patient automatically triggers an update message to be sent to relatives.

### Data retrieval 

1. The relative wishing for details on their loved one SMS is sent to a shortcode number
1. This is then redirected to RapidPro which starts a flow
1. The flow asks for the number and calls /query (on the server) with the number and retrieves the data
1. Relative receives a message with the status of the patient

# Contribute

Please check out the [issues](https://github.com/eHealthAfrica/Amsel/issues) we are currently workin on. Feel free to ask questions via email if something is unclear.  

[About us](https://github.com/eHealthAfrica/jobs/blob/master/what-we-do.md)

Licensed under the [Apache License Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt).
