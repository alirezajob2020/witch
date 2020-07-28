## Adding a message

### ADD /apiv1/messages

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Message1
startDate | ? | ? | ? | 2020-07-28T15:01:25.402547
endDate | ? | ? | ? | 2020-07-28T15:01:25.402568
repeat | ? | ? | ? | never

### CURL

```bash
curl -X ADD --data '{"title": "Message1", "startDate": "2020-07-28T15:01:25.402547", "endDate": "2020-07-28T15:01:25.402568", "repeat": "never"}' -- "$URL/apiv1/messages?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"new message is added"
```

