## Get users list

### LIST /apiv1/users

### CURL

```bash
curl -X LIST -H "Authorization: $TOKEN" -- "$URL/apiv1/users?"
```

### Response: 200 OK

#### Headers

* X-Identity: 1
* X-Pagination-Take: 100
* X-Pagination-Skip: 0
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "firstName":"alirezaa2",
        "id":1,
        "email":"alireza@msn.com",
        "lastName":"tavakoli1",
        "birthDate":null,
        "title":"alitk777"
    },
    {
        "firstName":"alizaaaaa",
        "id":2,
        "email":"alireza1@msn.com",
        "lastName":"tavakoliiii",
        "birthDate":null,
        "title":"alitk778"
    },
    {
        "firstName":"ali",
        "id":3,
        "email":"alireza2@msn.com",
        "lastName":"tavakoliiii",
        "birthDate":null,
        "title":"alitk779"
    }
]
```

---

## WHEN: Request is not authorized

### LIST /apiv1/users

### CURL

```bash
curl -X LIST -- "$URL/apiv1/users?"
```

### Response: 401 Unauthorized

#### Headers

* ContentType: application/json

---

## WHEN: Trying to sorting response

### LIST /apiv1/users

### Query Strings

Name | Example
--- | ---
sort | id

### CURL

```bash
curl -X LIST -H "Authorization: $TOKEN" -- "$URL/apiv1/users?sort=id"
```

### Response: 200 OK

#### Headers

* X-Identity: 1
* X-Pagination-Take: 100
* X-Pagination-Skip: 0
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "firstName":"alirezaa2",
        "id":1,
        "email":"alireza@msn.com",
        "lastName":"tavakoli1",
        "birthDate":null,
        "title":"alitk777"
    },
    {
        "firstName":"alizaaaaa",
        "id":2,
        "email":"alireza1@msn.com",
        "lastName":"tavakoliiii",
        "birthDate":null,
        "title":"alitk778"
    },
    {
        "firstName":"ali",
        "id":3,
        "email":"alireza2@msn.com",
        "lastName":"tavakoliiii",
        "birthDate":null,
        "title":"alitk779"
    }
]
```

---

## WHEN: Sorting the response descending

### LIST /apiv1/users

### Query Strings

Name | Example
--- | ---
sort | -id

### CURL

```bash
curl -X LIST -H "Authorization: $TOKEN" -- "$URL/apiv1/users?sort=-id"
```

### Response: 200 OK

#### Headers

* X-Identity: 1
* X-Pagination-Take: 100
* X-Pagination-Skip: 0
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "firstName":"ali",
        "id":3,
        "email":"alireza2@msn.com",
        "lastName":"tavakoliiii",
        "birthDate":null,
        "title":"alitk779"
    },
    {
        "firstName":"alizaaaaa",
        "id":2,
        "email":"alireza1@msn.com",
        "lastName":"tavakoliiii",
        "birthDate":null,
        "title":"alitk778"
    },
    {
        "firstName":"alirezaa2",
        "id":1,
        "email":"alireza@msn.com",
        "lastName":"tavakoli1",
        "birthDate":null,
        "title":"alitk777"
    }
]
```

---

## WHEN: Trying pagination response

### LIST /apiv1/users

### Query Strings

Name | Example
--- | ---
take | 1

### CURL

```bash
curl -X LIST -H "Authorization: $TOKEN" -- "$URL/apiv1/users?take=1"
```

### Response: 200 OK

#### Headers

* X-Identity: 1
* X-Pagination-Take: 1
* X-Pagination-Skip: 0
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "firstName":"alirezaa2",
        "id":1,
        "email":"alireza@msn.com",
        "lastName":"tavakoli1",
        "birthDate":null,
        "title":"alitk777"
    }
]
```

---

## WHEN: Trying pagination with skip

### LIST /apiv1/users

### Query Strings

Name | Example
--- | ---
take | 1
skip | 1

### CURL

```bash
curl -X LIST -H "Authorization: $TOKEN" -- "$URL/apiv1/users?take=1&skip=1"
```

### Response: 200 OK

#### Headers

* X-Identity: 1
* X-Pagination-Take: 1
* X-Pagination-Skip: 1
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "firstName":"alizaaaaa",
        "id":2,
        "email":"alireza1@msn.com",
        "lastName":"tavakoliiii",
        "birthDate":null,
        "title":"alitk778"
    }
]
```

---

## WHEN: Trying filtering response

### LIST /apiv1/users

### Query Strings

Name | Example
--- | ---
id | 1

### CURL

```bash
curl -X LIST -H "Authorization: $TOKEN" -- "$URL/apiv1/users?id=1"
```

### Response: 200 OK

#### Headers

* X-Identity: 1
* X-Pagination-Take: 100
* X-Pagination-Skip: 0
* X-Pagination-Count: 1

#### Body

Content-Type: application/json

```json
[
    {
        "firstName":"alirezaa2",
        "id":1,
        "email":"alireza@msn.com",
        "lastName":"tavakoli1",
        "birthDate":null,
        "title":"alitk777"
    }
]
```

