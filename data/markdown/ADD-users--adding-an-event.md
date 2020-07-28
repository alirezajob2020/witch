## Adding an event

### ADD /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Event1
startDate | ? | ? | ? | 2020-07-28T15:01:28.866213
endDate | ? | ? | ? | 2020-07-28T15:01:28.866234
repeat | ? | ? | ? | never

### CURL

```bash
curl -X ADD --data '{"title": "Event1", "startDate": "2020-07-28T15:01:28.866213", "endDate": "2020-07-28T15:01:28.866234", "repeat": "never"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"user is added"
```

