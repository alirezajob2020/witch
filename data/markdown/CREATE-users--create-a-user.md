## Create a user

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
name | ? | ? | ? | alireza
fullname | ? | ? | ? | tavakoli
email | ? | ? | ? | alitk@msn.com

### CURL

```bash
curl -X CREATE --data '{"name": "alireza", "fullname": "tavakoli", "email": "alitk@msn.com"}' -- "$URL/apiv1/users?"
```

### Response: 500 Internal server error

#### Headers

* ContentType: application/json

