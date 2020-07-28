## Adding a target

### ADD /apiv1/targets

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | target1
startDate | ? | ? | ? | 2020-07-28T15:01:27.158169
endDate | ? | ? | ? | 2020-07-28T15:01:27.158190
repeat | ? | ? | ? | never

### CURL

```bash
curl -X ADD --data '{"title": "target1", "startDate": "2020-07-28T15:01:27.158169", "endDate": "2020-07-28T15:01:27.158190", "repeat": "never"}' -- "$URL/apiv1/targets?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"target is added"
```

