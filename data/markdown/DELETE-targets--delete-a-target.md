## Delete a target

### DELETE /apiv1/targets

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | target1
startDate | ? | ? | ? | 2020-07-28T15:01:28.237569
endDate | ? | ? | ? | 2020-07-28T15:01:28.237590
repeat | ? | ? | ? | never

### CURL

```bash
curl -X DELETE --data '{"title": "target1", "startDate": "2020-07-28T15:01:28.237569", "endDate": "2020-07-28T15:01:28.237590", "repeat": "never"}' -- "$URL/apiv1/targets?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"target is deleted"
```

