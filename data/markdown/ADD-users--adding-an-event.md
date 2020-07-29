## Adding an event

### ADD /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Event1
startDate | ? | ? | ? | 2020-07-29T11:27:52.732627
endDate | ? | ? | ? | 2020-07-29T11:27:52.732642
repeat | ? | ? | ? | never

### CURL

```bash
curl -X ADD --data '{"title": "Event1", "startDate": "2020-07-29T11:27:52.732627", "endDate": "2020-07-29T11:27:52.732642", "repeat": "never"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"user is added"
```

