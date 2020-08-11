## Get token

### CREATE /apiv1/tokens

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
email | ? | ? | ? | alireza@msn.com
password | ? | ? | ? | ABc123123

### CURL

```bash
curl -X CREATE --data '{"email": "alireza@msn.com", "password": "ABc123123"}' -- "$URL/apiv1/tokens?"
```

### Response: 200 OK

#### Headers

* X-Identity: 1
* Set-Cookie: refresh-token=eyJhbGciOiJIUzI1NiIsImlhdCI6MTU5NzEzNTU0OCwiZXhwIjoxNTk5ODEzOTQ4fQ.eyJpZCI6MX0.egB4CT8HTvtoNmh3JH8BQ_MCXL7Sw7pjRTrXxYwcdHI; Max-Age=2678400; Secure

#### Body

Content-Type: application/json

```json
{
    "token":"eyJhbGciOiJIUzI1NiIsImlhdCI6MTU5NzEzNTU0OCwiZXhwIjoxNTk3MjIxOTQ4fQ.eyJpZCI6MSwidGl0bGUiOiJhbGl0azc3NyIsImVtYWlsIjoiYWxpcmV6YUBtc24uY29tIiwiZmlyc3ROYW1lIjoiYWxpcmV6YWEiLCJsYXN0TmFtZSI6InRhdmFrb2xpIiwic2Vzc2lvbklkIjoiM2RkMmQ5MjktZThlYi00MjU4LWExM2YtZTFhNTczYzgyMjM3In0.xX3A161_ZGbO3M39QHnGzwOrtil6BAUfGPz5O3DX4Ag"
}
```

---

## WHEN: Invalid password

### CREATE /apiv1/tokens

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
email | ? | ? | ? | alireza@msn.com
password | ? | ? | ? | Ss1236

### CURL

```bash
curl -X CREATE --data '{"email": "alireza@msn.com", "password": "Ss1236"}' -- "$URL/apiv1/tokens?"
```

### Response: 400 Incorrect Email Or Password

#### Headers

* ContentType: application/json

---

## WHEN: Not exist email

### CREATE /apiv1/tokens

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
email | ? | ? | ? | user@example.com
password | ? | ? | ? | ABc123123

### CURL

```bash
curl -X CREATE --data '{"email": "user@example.com", "password": "ABc123123"}' -- "$URL/apiv1/tokens?"
```

### Response: 400 Incorrect Email Or Password

#### Headers

* ContentType: application/json

---

## WHEN: Invalid email format

### CREATE /apiv1/tokens

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
email | ? | ? | ? | user.com
password | ? | ? | ? | ABc123123

### CURL

```bash
curl -X CREATE --data '{"email": "user.com", "password": "ABc123123"}' -- "$URL/apiv1/tokens?"
```

### Response: 400 Invalid Email Format

#### Headers

* ContentType: application/json

---

## WHEN: Trying to pass with empty form

### CREATE /apiv1/tokens

### CURL

```bash
curl -X CREATE -- "$URL/apiv1/tokens?"
```

### Response: 400 Empty Form

#### Headers

* ContentType: text/plain;charset=utf-8

