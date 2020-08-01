## Create a message

### CREATE /apiv1/messages

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Message1
startDate | ? | ? | ? | 2020-08-01T13:31:38.305110
endDate | ? | ? | ? | 2020-08-01T13:31:38.305133

### CURL

```bash
curl -X CREATE --data '{"title": "Message1", "startDate": "2020-08-01T13:31:38.305110", "endDate": "2020-08-01T13:31:38.305133"}' -- "$URL/apiv1/messages?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
null
```

