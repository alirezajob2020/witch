## Create a message

### CREATE /apiv1/messages

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Message1
startDate | ? | ? | ? | 2020-07-29T11:27:49.676284
endDate | ? | ? | ? | 2020-07-29T11:27:49.676309
repeat | ? | ? | ? | never

### CURL

```bash
curl -X CREATE --data '{"title": "Message1", "startDate": "2020-07-29T11:27:49.676284", "endDate": "2020-07-29T11:27:49.676309", "repeat": "never"}' -- "$URL/apiv1/messages?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"new message is created"
```

