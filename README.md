# 🔐 Cybersecurity Risk Tracker (Django REST API)

A backend system to manage and analyze cybersecurity risks across organizational assets.  
This project allows tracking of Assets, Vulnerabilities, and Risk Assessments, and provides a dashboard with summarized security insights.

Built using Django + Django REST Framework with clean architecture and scalable design.

---

## 📌 Project Overview

The Cybersecurity Risk Tracker helps security teams:
- Manage IT assets
- Track vulnerabilities per asset
- Calculate and monitor risk assessments
- View aggregated dashboard metrics for decision-making

It exposes REST APIs that can be consumed by any frontend (React, Angular, etc.) or used directly via Postman.

---

## 🚀 Features

- Asset Management (CRUD APIs)
- Vulnerability Tracking with severity levels
- Risk Assessment scoring per asset
- Dashboard analytics:
  - Total assets
  - Total vulnerabilities
  - Highest risk score
  - Critical vulnerability count
  - Severity distribution
  - Top risky assets

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 6 |
| API | Django REST Framework |
| Deployment | Render |
| Language | Python 3 |

---


---

## ⚙️ Installation & Setup (Local Development)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Cybersecurity-Risk-Tracker.git
cd Cybersecurity-Risk-Tracker
```
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

# Windows
```venv\Scripts\activate
```
# Mac/Linux
```source venv/bin/activate
```
3️⃣ Install Dependencies
```pip install -r requirements.txt
```

4️⃣ Apply Migrations
```python manage.py migrate
```

5️⃣ Run the Server
```python manage.py runserver
```

Server will run at:
http://127.0.0.1:8000/

---
## API Endpoints
#### Asset APIs
```
GET     /api/assets/
POST    /api/assets/
PUT     /api/assets/{id}/
DELETE  /api/assets/{id}/
```

#### Vulnerability APIs
```
GET     /api/vulnerabilities/
POST    /api/vulnerabilities/
```

#### Risk Assessment APIs
```
GET     /api/risks/
POST    /api/risks/
```

#### Dashboard API
```
GET /api/dashboard/
```
