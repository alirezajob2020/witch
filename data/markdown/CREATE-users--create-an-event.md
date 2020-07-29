## Create an event

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Event1
startDate | ? | ? | ? | 2020-07-29T11:27:53.295039
endDate | ? | ? | ? | 2020-07-29T11:27:53.295061
repeat | ? | ? | ? | never

### CURL

```bash
curl -X CREATE --data '{"title": "Event1", "startDate": "2020-07-29T11:27:53.295039", "endDate": "2020-07-29T11:27:53.295061", "repeat": "never"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "fullname":"tavakoli",
    "id":1,
    "name":"alireza",
    "email":"alitk@msn.com"
}
```

