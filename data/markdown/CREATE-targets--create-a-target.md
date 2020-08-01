## Create a target

### CREATE /apiv1/targets

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | target1
startDate | ? | ? | ? | 2020-08-01T13:31:38.877897
endDate | ? | ? | ? | 2020-08-01T13:31:38.877915

### CURL

```bash
curl -X CREATE --data '{"title": "target1", "startDate": "2020-08-01T13:31:38.877897", "endDate": "2020-08-01T13:31:38.877915"}' -- "$URL/apiv1/targets?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
null
```

