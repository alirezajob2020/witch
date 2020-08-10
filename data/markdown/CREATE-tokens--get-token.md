## Get token

### CREATE /apiv1/tokens

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
email | ? | ? | ? | ali@gmail.com
password | ? | ? | ? | Alitk123123

### CURL

```bash
curl -X CREATE --data '{"email": "ali@gmail.com", "password": "Alitk123123"}' -- "$URL/apiv1/tokens?"
```

### Response: 603 Incorrect Email Or Password

#### Headers

* ContentType: application/json

