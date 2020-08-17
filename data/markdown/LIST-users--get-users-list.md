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
        "id":1,
        "birthDate":null,
        "lastName":"tavakoli1",
        "title":"alitk777",
        "firstName":"alirezaa2",
        "email":"alireza@msn.com"
    },
    {
        "id":2,
        "birthDate":null,
        "lastName":"tavakoliiii",
        "title":"alitk778",
        "firstName":"alizaaaaa",
        "email":"alireza1@msn.com"
    },
    {
        "id":3,
        "birthDate":null,
        "lastName":"tavakoliiii",
        "title":"alitk779",
        "firstName":"ali",
        "email":"alireza2@msn.com"
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
        "id":1,
        "birthDate":null,
        "lastName":"tavakoli1",
        "title":"alitk777",
        "firstName":"alirezaa2",
        "email":"alireza@msn.com"
    },
    {
        "id":2,
        "birthDate":null,
        "lastName":"tavakoliiii",
        "title":"alitk778",
        "firstName":"alizaaaaa",
        "email":"alireza1@msn.com"
    },
    {
        "id":3,
        "birthDate":null,
        "lastName":"tavakoliiii",
        "title":"alitk779",
        "firstName":"ali",
        "email":"alireza2@msn.com"
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
        "id":3,
        "birthDate":null,
        "lastName":"tavakoliiii",
        "title":"alitk779",
        "firstName":"ali",
        "email":"alireza2@msn.com"
    },
    {
        "id":2,
        "birthDate":null,
        "lastName":"tavakoliiii",
        "title":"alitk778",
        "firstName":"alizaaaaa",
        "email":"alireza1@msn.com"
    },
    {
        "id":1,
        "birthDate":null,
        "lastName":"tavakoli1",
        "title":"alitk777",
        "firstName":"alirezaa2",
        "email":"alireza@msn.com"
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
        "id":1,
        "birthDate":null,
        "lastName":"tavakoli1",
        "title":"alitk777",
        "firstName":"alirezaa2",
        "email":"alireza@msn.com"
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
        "id":2,
        "birthDate":null,
        "lastName":"tavakoliiii",
        "title":"alitk778",
        "firstName":"alizaaaaa",
        "email":"alireza1@msn.com"
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
        "id":1,
        "birthDate":null,
        "lastName":"tavakoli1",
        "title":"alitk777",
        "firstName":"alirezaa2",
        "email":"alireza@msn.com"
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

