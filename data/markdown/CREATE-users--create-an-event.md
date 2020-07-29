## Create an event

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | Event1
startDate | ? | ? | ? | 2020-07-29T11:41:52.690265
endDate | ? | ? | ? | 2020-07-29T11:41:52.690275
repeat | ? | ? | ? | never

### CURL

```bash
curl -X CREATE --data '{"title": "Event1", "startDate": "2020-07-29T11:41:52.690265", "endDate": "2020-07-29T11:41:52.690275", "repeat": "never"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "email":"alitk@msn.com",
    "fullname":"tavakoli",
    "id":1,
    "name":"alireza"
}
```

