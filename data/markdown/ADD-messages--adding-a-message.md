## Adding a message

### ADD /apiv1/messages

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Message1
startDate | ? | ? | ? | 2020-07-29T11:27:49.119221
endDate | ? | ? | ? | 2020-07-29T11:27:49.119243
repeat | ? | ? | ? | never

### CURL

```bash
curl -X ADD --data '{"title": "Message1", "startDate": "2020-07-29T11:27:49.119221", "endDate": "2020-07-29T11:27:49.119243", "repeat": "never"}' -- "$URL/apiv1/messages?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"new message is added"
```

