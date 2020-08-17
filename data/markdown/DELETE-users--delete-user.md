## Delete user

### DELETE /apiv1/users/:id

### Url Parameters

Name | Example
--- | ---
id | 1

### CURL

```bash
curl -X DELETE -H "Authorization: $TOKEN" -- "$URL/apiv1/users/1?"
```

### Response: 200 OK

#### Headers

* X-Identity: 1

#### Body

Content-Type: application/json

```json
{
    "id":1,
    "birthDate":null,
    "lastName":"tavakoli",
    "title":"mma",
    "firstName":"alirezaa",
    "email":"qq@msn.com"
}
```

---

## WHEN: Request is not authorized

### DELETE /apiv1/users/:id

### CURL

```bash
curl -X DELETE -- "$URL/apiv1/users/1?"
```

### Response: 401 Unauthorized

#### Headers

* ContentType: application/json

