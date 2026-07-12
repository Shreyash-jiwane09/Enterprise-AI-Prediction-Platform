# 🚀 Enterprise AI Prediction Platform

A production-oriented backend application built with **FastAPI** as part of an end-to-end Enterprise Backend Engineering course.

---

## 🎯 Project Goal

Build a scalable, maintainable, and production-ready AI Prediction Platform while learning FastAPI from beginner to enterprise level.

The project evolves throughout the course and follows modern backend engineering practices.

---

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- Uvicorn

> More technologies (PostgreSQL, SQLAlchemy, Redis, Docker, CI/CD, etc.) will be added as the course progresses.

---

## 📂 Project Structure

```text
enterprise-ai-prediction-platform/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── docs/
├── tests/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 Running the Application

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn app.main:app --reload
```

---

## 📌 Available Endpoints

| Endpoint | Description |
|----------|-------------|
| / | Welcome Endpoint |
| /health | Health Check |
| /docs | Swagger UI |
| /redoc | ReDoc |

---

## 📚 Course Progress

Current Milestone:

- ✅ Project Initialization

Upcoming:

- Routing
- Request Handling
- Pydantic
- Dependency Injection
- Enterprise Architecture
- Database Integration
- Authentication
- Machine Learning APIs
- Docker
- CI/CD

---

## 📄 License

This project is created for educational purposes and will evolve into a production-grade backend system.