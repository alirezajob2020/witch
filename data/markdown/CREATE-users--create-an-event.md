## Create an event

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Event1
startDate | ? | ? | ? | 2020-07-28T15:01:29.557650
endDate | ? | ? | ? | 2020-07-28T15:01:29.557671
repeat | ? | ? | ? | never

### CURL

```bash
curl -X CREATE --data '{"title": "Event1", "startDate": "2020-07-28T15:01:29.557650", "endDate": "2020-07-28T15:01:29.557671", "repeat": "never"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "<built-in function id>":2
}
```

