
# Django Email Verification API with Rate Limiting

This project provides a secure API endpoint to send verification codes to user emails, with strong protection against abuse using *Django Ratelimit* and *Redis-based custom rate limiting*.

---

## Features

- Send verification code to user email
- Prevent abuse using:
  - Django Ratelimit for IP-level protection
  - Custom Redis logic for email/user-based throttling
- Configurable limits (e.g. 5 attempts per email, 10 requests per minute per IP)
- Simple and clean API response structure

---

## Tech Stack

- Django
- Django REST Framework
- Redis Cloud
- Django Ratelimit
- Django Caching System (Redis backend)
- dotenv

---

## Why both Ratelimit & Custom Logic?

- *Django Ratelimit* is great for general abuse control (based on IP).
- *Custom Redis logic* gives full control over business-specific limits (e.g. max OTP attempts per user/email).
- Using both ensures maximum protection and flexibility.

---