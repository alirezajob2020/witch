## Create a message

### CREATE /apiv1/messages

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Message1
startDate | ? | ? | ? | 2020-07-28T15:01:25.967633
endDate | ? | ? | ? | 2020-07-28T15:01:25.967650
repeat | ? | ? | ? | never

### CURL

```bash
curl -X CREATE --data '{"title": "Message1", "startDate": "2020-07-28T15:01:25.967633", "endDate": "2020-07-28T15:01:25.967650", "repeat": "never"}' -- "$URL/apiv1/messages?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"new message is created"
```

