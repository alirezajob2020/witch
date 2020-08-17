## Update user

### UPDATE /apiv1/users/:id

### Url Parameters

Name | Example
--- | ---
id | 1

### Multipart

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | wwqweqas
firstName | ? | ? | ? | alireza
lastName | ? | ? | ? | tk
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | alirezaaa@msn.com

### CURL

```bash
curl -X UPDATE -F "title=wwqweqas" -F "firstName=alireza" -F "lastName=tk" -F "birthDate=1972-2-2" -F "email=alirezaaa@msn.com" -H "Authorization: $TOKEN" -- "$URL/apiv1/users/1?"
```

### Response: 200 OK

#### Headers

* X-Identity: 1

#### Body

Content-Type: application/json

```json
{
    "id":1,
    "birthDate":"1972-02-02",
    "lastName":"tk",
    "title":"wwqweqas",
    "firstName":"alireza",
    "email":"alirezaaa@msn.com"
}
```

---

## WHEN: duplicated title

### UPDATE /apiv1/users/:id

### Multipart

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | alitkmm

### CURL

```bash
curl -X UPDATE -F "title=alitkmm" -H "Authorization: $TOKEN" -- "$URL/apiv1/users/1?"
```

### Response: 400 title is already exist

#### Headers

* ContentType: application/json

---

## WHEN: duplicated email

### UPDATE /apiv1/users/:id

### Multipart

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
email | ? | ? | ? | alireza@msn.com

### CURL

```bash
curl -X UPDATE -F "email=alireza@msn.com" -H "Authorization: $TOKEN" -- "$URL/apiv1/users/1?"
```

### Response: 400 email address is already exist

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass less than 3 character

### UPDATE /apiv1/users/:id

### Multipart

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | aq

### CURL

```bash
curl -X UPDATE -F "title=aq" -H "Authorization: $TOKEN" -- "$URL/apiv1/users/1?"
```

### Response: 400 Title Length Must Be Greater Than 3 Characters and Less than 256 Character

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass greater than 256 character

### UPDATE /apiv1/users/:id

### Multipart

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

### CURL

```bash
curl -X UPDATE -F "title=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" -H "Authorization: $TOKEN" -- "$URL/apiv1/users/1?"
```

### Response: 400 Title Length Must Be Greater Than 3 Characters and Less than 256 Character

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass invalid email format

### UPDATE /apiv1/users/:id

### Multipart

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
email | ? | ? | ? | asd.com

### CURL

```bash
curl -X UPDATE -F "email=asd.com" -H "Authorization: $TOKEN" -- "$URL/apiv1/users/1?"
```

### Response: 400 Invalid Email Format

#### Headers

* ContentType: application/json

---

## WHEN: Request is not authorized

### UPDATE /apiv1/users/:id

### CURL

```bash
curl -X UPDATE -F "title=wwqweqas" -F "firstName=alireza" -F "lastName=tk" -F "birthDate=1972-2-2" -F "email=alirezaaa@msn.com" -- "$URL/apiv1/users/1?"
```

### Response: 401 Unauthorized

#### Headers

* ContentType: application/json

