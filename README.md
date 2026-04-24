# 🔗 Serverless URL Shortener

A cloud-based URL shortener built using AWS serverless services. Submit a long URL and get a short code back — visit the short link and get redirected to the original URL instantly.

---

## 🏗️ Architecture

```
User → API Gateway → Lambda (shorten) → DynamoDB
User → API Gateway → Lambda (redirect) → DynamoDB → 301 Redirect
```

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| AWS Lambda | Runs Python code on demand (serverless) |
| Amazon DynamoDB | Stores short code → long URL pairs |
| Amazon API Gateway | Exposes HTTP endpoints to the internet |

---

## ⚙️ How It Works

### Shorten a URL
- User sends a `POST /shorten` request with a long URL
- Lambda generates a random 6-character short code
- Short code and original URL are saved to DynamoDB
- Short code is returned to the user

### Redirect
- User visits `GET /{short_code}` in their browser
- Lambda looks up the short code in DynamoDB
- Returns a `301 redirect` to the original URL
- Browser automatically navigates to the original page

---

## 🚀 API Endpoints

### POST /shorten
**Request:**
```json
{
  "long_url": "https://www.example.com/some/very/long/url"
}
```
**Response:**
```json
{
  "short_code": "aB3xYz"
}
```

### GET /{short_code}
**Example:**
```
GET /aB3xYz
```
**Response:** `301 Redirect → https://www.example.com/some/very/long/url`

---

## 🛠️ Setup Instructions

### 1. Create DynamoDB Table
- Table name: `url-shortener`
- Partition key: `short_code` (String)

### 2. Create Lambda Functions
- **shorten_a_URL** — paste code from `shorten.py`
- **redirect** — paste code from `redirect.py`
- Attach `AmazonDynamoDBFullAccess` policy to both functions

### 3. Create API Gateway
- Type: HTTP API
- Name: `url-shortener-api`
- Routes:
  - `POST /shorten` → shorten_a_URL Lambda
  - `GET /{short_code}` → redirect Lambda

### 4. Test
```bash
# Shorten a URL
curl -X POST https://YOUR_INVOKE_URL/shorten \
  -H "Content-Type: application/json" \
  -d '{"long_url": "https://www.google.com"}'

# Visit short link in browser
https://YOUR_INVOKE_URL/{short_code}
```

---

## 📁 Project Structure

```
serverless-url-shortener/
│
├── shorten.py        # Lambda function 1 - generates short code
├── redirect.py       # Lambda function 2 - handles redirect
└── README.md         # Project documentation
```

---

## 💡 Key Concepts Learned

- Serverless computing with AWS Lambda
- NoSQL database design with DynamoDB
- REST API creation with API Gateway
- IAM roles and permissions
- Event-driven architecture

---

## 👨‍💻 Author

**Sheshadri Jonnagiri**  
B.Tech CSE (IoT) — Presidency University, Bengaluru  
[LinkedIn](https://www.linkedin.com/in/) | [GitHub](https://github.com/)

---

## 📄 License
MIT License
