## Create a user

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | alitk777
firstname | ? | ? | ? | alireza
lastname | ? | ? | ? | tavakoli
birth_date | ? | ? | ? | 1970-2-2
email | ? | ? | ? | alitk@msn.com

### CURL

```bash
curl -X CREATE --data '{"title": "alitk777", "firstname": "alireza", "lastname": "tavakoli", "birth_date": "1970-2-2", "email": "alitk@msn.com"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "firstname":"alireza",
    "lastname":"tavakoli",
    "id":1,
    "birthDate":"1970-02-02T00:00:00",
    "email":"alitk@msn.com",
    "title":"alitk777"
}
```

---

## WHEN: Trying to pass without form parameters

### CREATE /apiv1/users

### CURL

```bash
curl -X CREATE -- "$URL/apiv1/users?"
```

### Response: 400 No Parameter Exists In The Form

#### Headers

* ContentType: text/plain;charset=utf-8

---

## WHEN: Trying to pass null title

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | None
firstname | ? | ? | ? | alireza
lastname | ? | ? | ? | tavakoli
birth_date | ? | ? | ? | 1970-2-2
email | ? | ? | ? | alitk@msn.com

### CURL

```bash
curl -X CREATE --data '{"title": null, "firstname": "alireza", "lastname": "tavakoli", "birth_date": "1970-2-2", "email": "alitk@msn.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 title is null

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass empty title

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
firstname | ? | ? | ? | alireza
lastname | ? | ? | ? | tavakoli
birth_date | ? | ? | ? | 1970-2-2
email | ? | ? | ? | alitk@msn.com

### CURL

```bash
curl -X CREATE --data '{"firstname": "alireza", "lastname": "tavakoli", "birth_date": "1970-2-2", "email": "alitk@msn.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 title field is required

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass less than 3 character

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | aq
firstname | ? | ? | ? | alireza
lastname | ? | ? | ? | tavakoli
birth_date | ? | ? | ? | 1970-2-2
email | ? | ? | ? | alitk@msn.com

### CURL

```bash
curl -X CREATE --data '{"title": "aq", "firstname": "alireza", "lastname": "tavakoli", "birth_date": "1970-2-2", "email": "alitk@msn.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 String Length Must Be Greater Than 3 Characters and Less than 256 Character

#### Headers

* ContentType: application/json

