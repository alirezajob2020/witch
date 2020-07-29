## Adding a target

### ADD /apiv1/targets

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | target1
startDate | ? | ? | ? | 2020-07-29T11:27:50.919602
endDate | ? | ? | ? | 2020-07-29T11:27:50.919625
repeat | ? | ? | ? | never

### CURL

```bash
curl -X ADD --data '{"title": "target1", "startDate": "2020-07-29T11:27:50.919602", "endDate": "2020-07-29T11:27:50.919625", "repeat": "never"}' -- "$URL/apiv1/targets?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
"target is added"
```

