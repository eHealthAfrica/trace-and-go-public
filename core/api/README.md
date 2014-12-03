> A really basic rest API.

## Authentication

This runs on basic token authentication. Each user can have a token assigned to them. These can be created in the `admin/` backend.

## GET

Access the API:
```
curl -X GET http://127.0.0.1:8000/api/patients/
```

To do basic filtering on the API:
```
curl -X GET http://127.0.0.1:8000/api/patients/?alive=True
```
Filterable fields are `alive`, `age`, `first_name`, `last_name`.

To do basic search on the API:
```
curl -X GET http://127.0.0.1:8000/api/patients/?search=Doe
```

The API will search on `first_name` and `last_name` fields.

You can separate by spaces:
```
curl -X GET http://127.0.0.1:8000/api/patients/?search=Jane,Doe
```
Only objects will be returned that match all of the search parameters.

## POST

POST to the API:
```
curl -X POST http://127.0.0.1:8000/api/patients/ -d '{uid:"12345679",first_name:"Joan",last_name:"Doe",enter_number:"+182311221",caregiver_number:"+223111811",age:"27",geolocation:"31.11",etu:"Dunno what this is.",alive:true}'
```
Returns:
```
{"detail":"Authentication credentials were not provided."}
```

But, POSTing to the API with a Token:
```
curl -X POST http://127.0.0.1:8000/api/patients/ -H 'Authorization: Token <auth_token>' -H 'Content-Type: application/json' -d '{"uid":"12345679","first_name":"Joan","last_name":"Doe","enter_number":"+182311221","caregiver_number":"+223111811","age":"27","geolocation":"31.11","etu":"Dunno what this is.","alive":true}'
```
(note the token, the content type, and the json formatting)


Returns the posted object:

```
{"uid":"12345679","first_name":"Joan","last_name":"Doe","enter_number":"+182311221","caregiver_number":"+223111811","age":"27","geolocation":"31.11","etu":"Dunno what this is.","alive":true,"json":""}
```

If there are any errors with the POST, this will show.

## PATCH: 

To update a specific patient, you can PATCH to their url:

```
curl -X PATCH http://127.0.0.1:8000/api/patients/<patient_pk>/ -H 'Authorization: Token <auth_token>' -H 'Content-Type: application/json' -d '{"alive":false}'
```

