## Delete a message

### DELETE /apiv1/messages

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Message1
startDate | ? | ? | ? | 2020-07-29T11:27:50.334609
endDate | ? | ? | ? | 2020-07-29T11:27:50.334630
repeat | ? | ? | ? | never

### CURL

```bash
curl -X DELETE --data '{"title": "Message1", "startDate": "2020-07-29T11:27:50.334609", "endDate": "2020-07-29T11:27:50.334630", "repeat": "never"}' -- "$URL/apiv1/messages?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"message is deleted"
```

