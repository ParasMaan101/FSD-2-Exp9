
Authentication is the process of verifying the identity of a user before granting access to protected resources. In modern web applications, token-based authentication is widely used instead of session-based authentication.

### 1️⃣ Basic Authentication (Authorization Header)

Basic Authentication sends credentials encoded in Base64 format inside the HTTP Authorization header. It is simple but less secure if not used with HTTPS.

Format:

```
Authorization: Basic base64(username:password)
```

---

### 2️⃣ Custom Header Authentication

In this method, credentials are sent through custom HTTP headers.

Example:

```
username: admin
password: 1234
```

The server verifies these credentials before allowing access.

---

### 3️⃣ JWT (JSON Web Token) Authentication

JWT is a secure and scalable token-based authentication method.

After successful login:

* Server generates a JWT token
* Client stores the token
* Client sends token in:

```
Authorization: Bearer <token>
```

JWT consists of:

* Header
* Payload
* Signature

It is widely used in modern APIs and microservices architecture.

---

## 🛠️ Technologies Used

* Python 3.x
* Flask Framework
* Flask-JWT-Extended
* Postman (API Testing Tool)
* Render (Cloud Deployment Platform)

---

## 📂 Project Structure

```
rest-api-auth/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 🚀 API Endpoints

### 1️⃣ Basic Auth Endpoint

```
GET /basic-auth
```

Authentication Method:
Authorization → Basic Auth

---

### 2️⃣ Custom Header Endpoint

```
GET /custom-auth
```

Headers Required:

```
username: admin
password: 1234
```

---

### 3️⃣ JWT Login Endpoint

```
POST /login
```

Body (JSON):

```json
{
  "username": "admin",
  "password": "1234"
}
```

Response:

```json
{
  "access_token": "JWT_TOKEN"
}
```

---

### 4️⃣ JWT Protected Endpoint

```
GET /jwt-protected
```

Header:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 🧪 Testing Procedure (Postman)

1. Start Flask server.
2. Test Basic Auth endpoint.
3. Test Custom Header endpoint.
4. Generate JWT token using login API.
5. Use token in Bearer header.
6. Verify successful authentication response.
7. Capture screenshots for submission.

---

## 🌐 Deployment

The project is deployed on **Render** cloud platform.

Deployment Steps:

1. Push code to GitHub.
2. Connect GitHub repository to Render.
3. Select Python environment.
4. Add Start Command:

   ```
   gunicorn app:app
   ```
5. Deploy and obtain public demo link.

---

## 📚 Learning Outcomes

After completing this experiment, I was able to:

1. Understand the concept of authentication and authorization.
2. Implement Basic Authentication using Authorization Header.
3. Implement authentication using custom HTTP headers.
4. Generate and validate JWT tokens in Flask.
5. Protect API routes using Bearer token authentication.
6. Test APIs using Postman.
7. Deploy Flask backend applications on cloud platforms.
8. Understand the importance of secure API communication.
9. Learn how token-based authentication improves scalability.
10. Gain practical experience in backend API security implementation.
