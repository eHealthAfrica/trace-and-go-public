Trace and Go (TAG)
==================

A huge problem in the current Ebola outbreak in West Africa is the traceability of people that have been admitted to health facilities. Unfortunately, it is a very common case that health workers pick up infected people, admit them to a health facility and the person dies without the family knowing which facility the person was admitted to or where they are buried. 

**We want to change this!**

By assigning a unique number to every patient on first contact and sharing it with their family, we can offer a text–based (SMS) service that family members can query to find out the status of their loved ones. 

- See [doc/install.md](doc/install.md) for how to run the prototype
- See [doc/services.md](doc/services.md) for a list of services we are currently using
- See [core/api/README.md](core/api/README.md) for an overview of the API

Please keep all discussions on GitHub with the issues. Otherwise feel free to email us at [lucy.chambers@ehealthnigeria.org](mailto:lucy.chambers@ehealthnigeria.org?Subject=TAG)

## Current flow

### Data entry

1. A health care worker adds a new patient through the interface. This can be through formhub a.k.a. ODK Collect (for offline use) or through the TAG admin interface.
2. They add the case investigator’s mobile number and the number of the family member or relative as well as some personal data
3. If formhub is used, as soon as the form is submitted, the formhub server triggers a web hook
4. This assigns the patient a unique number/id
5. The following text messages are triggered: 


|To the relative  | To the case investigator |   
|-----|-----|
|<ol><li> Gives the unique number,</li><li> Says: “You will be notified of all changes in the status and location of your loved one”,</li></ol> | 1. Gives the unique number (as above)  |

### Data modification

1. A very simple dashboard is available (/admin) for health care workers to update patient data. 
2. Updating the status of a patient automatically triggers an update message to be sent to relatives.

### Data retrieval 

1. The relative wishing for updates on the status of their loved one sends a message containing the unique ID of their relative to the designated shortcode number
2. This is then redirected to the TAG backend (/smswebhook)
3. Relative receives a message with the status of the patient

# Contribute

Please check out the [issues](https://github.com/eHealthAfrica/trace-and-go/issues) we are currently working on. Feel free to ask questions via email if something is unclear.  

[About us](https://github.com/eHealthAfrica/jobs/blob/master/what-we-do.md)

Licensed under the [Apache License Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt).