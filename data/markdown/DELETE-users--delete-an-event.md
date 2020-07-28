## Delete an event

### DELETE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Event1
startDate | ? | ? | ? | 2020-07-28T15:01:30.158996
endDate | ? | ? | ? | 2020-07-28T15:01:30.159018
repeat | ? | ? | ? | never

### CURL

```bash
curl -X DELETE --data '{"title": "Event1", "startDate": "2020-07-28T15:01:30.158996", "endDate": "2020-07-28T15:01:30.159018", "repeat": "never"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"user is deleted"
```

