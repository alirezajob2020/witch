## Create a user

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | qweqweqwe
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"title": "qweqweqwe", "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "id":1,
    "title":"qweqweqwe",
    "firstName":"asdasfdsasdd",
    "email":"mohsen@msnaa.com",
    "lastName":"zxczxczxcasdv",
    "birthDate":"1972-02-02T00:00:00"
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
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"title": null, "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
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
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
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
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"title": "aq", "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 Title Length Must Be Greater Than 3 Characters and Less than 256 Character

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass greater than 256 character

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"title": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 Title Length Must Be Greater Than 3 Characters and Less than 256 Character

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass null firstname

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | qweqweqwe
firstName | ? | ? | ? | None
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"title": "qweqweqwe", "firstName": null, "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 firstname field is null

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass null lastname

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | qweqweqwe
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | None
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"title": "qweqweqwe", "firstName": "asdasfdsasdd", "lastName": null, "birthDate": "1972-2-2", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 lastname field is null

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass wrong date

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | qweqweqwe
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 30-50-40
email | ? | ? | ? | mohsen@msnaa.com

### CURL

```bash
curl -X CREATE --data '{"title": "qweqweqwe", "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "30-50-40", "email": "mohsen@msnaa.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 Invalid Date Format

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass null title

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | qweqweqwe
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | None

### CURL

```bash
curl -X CREATE --data '{"title": "qweqweqwe", "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": null}' -- "$URL/apiv1/users?"
```

### Response: 400 email is null

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass empty email

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | qweqweqwe
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2

### CURL

```bash
curl -X CREATE --data '{"title": "qweqweqwe", "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2"}' -- "$URL/apiv1/users?"
```

### Response: 400 Email Not In Form

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass invalid email format

### CREATE /apiv1/users

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
title | ? | ? | ? | qweqweqwe
firstName | ? | ? | ? | asdasfdsasdd
lastName | ? | ? | ? | zxczxczxcasdv
birthDate | ? | ? | ? | 1972-2-2
email | ? | ? | ? | asd.com

### CURL

```bash
curl -X CREATE --data '{"title": "qweqweqwe", "firstName": "asdasfdsasdd", "lastName": "zxczxczxcasdv", "birthDate": "1972-2-2", "email": "asd.com"}' -- "$URL/apiv1/users?"
```

### Response: 400 Invalid Email Format

#### Headers

* ContentType: application/json

