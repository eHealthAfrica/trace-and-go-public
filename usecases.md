## Relevant user stories: 

### Health Worker 

As a **health worker at a hospital**, 
I want to **easily enter a new case into the system** 
so that I can **trigger a response to the relative**.

As a **health worker at a health facility**, 
I want to **easily search for a patient who is at my health facility** 
so that I can **update their record**.

As a **health worker at a health facility**, 
I want to **easily update any of the cases at my health facility**
so that **the relative knows about the evolving status of their loved one**.

### Health Facility -administrator 

As **an HF administrator** 
I want to **manage who has edit access to our local HFdata** 
so that I can **ensure that new health workers are added when they join and removed when they leave**. 

### Super-admin 

As a **super-administrator of the system** 
I want to **see all patients of all health facilities**  
so that I can **update the status of any patient and troubleshoot any issues.**

As a **super-administrator of the system** 
I want to **add a new health facility or location**
so that I can **update the system without having to wait for a developer each time.** 

## Acceptance criteria:

* Each user has their own login
* Health worker level permissions can: 
    * *view* cases from the HF they are a member of. 
    * *add* new cases to the HF they are a member of
    * *edit* any case from the HF they are a member of 
* HF-administrator can: 
    * Do anything the Health worker can. 
    * Add and remove users to their HF. 
    * [CLARIFYING] Add sublevels to their HF e.g. Wards. So that the family member receives a message like: "Patient X has been admitted to the maternity ward of JFK Hospital" see: #61 
* A Super-Admin can: 
    * *view* cases from any HF 
    * *add* new cases 
    * *edit* any case 
    * Add or remove any user
    * Add an HF
