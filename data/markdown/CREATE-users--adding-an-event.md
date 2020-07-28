## Adding an event

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Event1
startDate | ? | ? | ? | 2020-07-28T12:59:56.381097
endDate | ? | ? | ? | 2020-07-28T12:59:56.381118
repeat | ? | ? | ? | never

### CURL

```bash
curl -X CREATE --data '{"title": "Event1", "startDate": "2020-07-28T12:59:56.381097", "endDate": "2020-07-28T12:59:56.381118", "repeat": "never"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "<built-in function id>":2
}
```

