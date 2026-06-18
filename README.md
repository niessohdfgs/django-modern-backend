# Django Modern Backend

A production-oriented backend architecture built with Django, PostgreSQL, Redis, Celery, Django Channels, Docker, Nginx, and GitHub Actions.

This project was created to move beyond traditional CRUD applications and explore technologies and architectural patterns commonly used in real-world backend systems.

The goal was not simply to build a Django application, but to understand how different infrastructure components work together in a production-oriented environment.

---

## Table of Contents

- Overview
- Why This Project?
- Technology Stack
- Architecture
- Service Breakdown
- Docker Infrastructure
- Database Layer
- Redis Layer
- Background Tasks
- Real-Time Communication
- ASGI with Daphne
- Reverse Proxy with Nginx
- Continuous Integration
- Project Structure
- Installation
- Development Workflow
- Learning Outcomes
- Future Improvements

---

## Overview

Most beginner Django projects stop after creating models, views, and APIs.

This project takes several steps further by integrating:

- PostgreSQL as the primary database
- Redis as a message broker
- Celery for asynchronous processing
- Django Channels for WebSockets
- Daphne as the ASGI server
- Nginx as a reverse proxy
- Docker for containerization
- GitHub Actions for CI

The result is a backend architecture much closer to what is commonly found in modern production systems.

---

## Why This Project?

The primary objective was to gain hands-on experience with:

- Backend architecture design
- Containerized environments
- Service orchestration
- Asynchronous task processing
- Real-time communication
- Continuous Integration
- Production-oriented deployment patterns

Instead of learning these concepts separately, they were combined into a single project to understand how they interact in practice.

---

## Technology Stack

### Backend

- Django
- Django Channels
- Daphne

### Database

- PostgreSQL

### Message Broker

- Redis

### Background Processing

- Celery

### Infrastructure

- Docker
- Docker Compose
- Nginx

### Automation

- GitHub Actions

---

## System Architecture

```text
                    Client
                       │
                       ▼
                    Nginx
                       │
        ┌──────────────┼──────────────┐
        ▼                             ▼
 Django Application           WebSocket Layer
      (Daphne)                   (Channels)
        │                             │
        ▼                             ▼
   PostgreSQL                     Redis
                                      │
                                      ▼
                                   Celery
```

The application is composed of multiple services, each with a dedicated responsibility.

This separation improves maintainability, scalability, and deployment flexibility.

---

## Docker Infrastructure

The entire application runs inside Docker containers.

Current services:

| Service | Purpose |
|----------|----------|
| backend | Django Application |
| db | PostgreSQL Database |
| redis | Message Broker |
| celery | Background Worker |
| nginx | Reverse Proxy |

Using Docker provides:

- Environment consistency
- Easy onboarding
- Reproducible builds
- Simplified deployment

A developer can run the entire stack with a single command.

---

## Database Layer

The project uses PostgreSQL as the primary database.

Reasons for choosing PostgreSQL:

- Reliability
- Strong relational support
- ACID compliance
- Production readiness
- Excellent Django integration

All persistent application data is stored inside PostgreSQL.

---

## Redis Layer

Redis is used as a high-performance in-memory data store.

Within this project it serves two important roles:

### Celery Broker

Redis acts as the communication channel between Django and Celery workers.

Tasks are pushed into Redis and consumed by workers asynchronously.

### Channels Backend

Redis is used as the channel layer backend for Django Channels.

It allows messages to be shared between multiple WebSocket connections.

---

## Background Tasks with Celery

Long-running operations should not block user requests.

To solve this problem, Celery was integrated.

Workflow:

```text
Django
  │
  ▼
Redis Queue
  │
  ▼
Celery Worker
  │
  ▼
Task Execution
```

Benefits:

- Faster response times
- Better scalability
- Separation of concerns
- Support for scheduled and asynchronous work

---

## Real-Time Communication

Traditional HTTP communication follows a request-response pattern.

For real-time features, Django Channels was introduced.

WebSocket endpoint:

```text
/ws/notifications/
```

Communication Flow:

```text
Client
  │
  ▼
WebSocket Connection
  │
  ▼
Channels Consumer
  │
  ▼
Redis Channel Layer
  │
  ▼
Connected Clients
```

This architecture enables:

- Live notifications
- Real-time updates
- Event-driven communication

---

## ASGI with Daphne

Because WebSockets require asynchronous support, the project runs on ASGI instead of traditional WSGI.

Daphne serves as the ASGI server.

Responsibilities:

- Handling HTTP traffic
- Managing WebSocket connections
- Supporting asynchronous execution

Without ASGI, WebSocket functionality would not be possible.

---

## Reverse Proxy with Nginx

Nginx sits in front of the application and acts as the entry point for incoming traffic.

Responsibilities:

- Reverse proxying requests
- Forwarding traffic to Django
- Production traffic management
- Performance optimization

Architecture:

```text
Client
  │
  ▼
Nginx
  │
  ▼
Django (Daphne)
```

---

## Continuous Integration

The project includes GitHub Actions.

Whenever code is pushed:

1. Dependencies are installed
2. PostgreSQL service is started
3. Database migrations run
4. Tests execute automatically

Benefits:

- Automated validation
- Early bug detection
- Consistent development workflow

---

## Project Structure

```text
project/
│
├── core/
│   ├── blog/
│   ├── core/
│   └── manage.py
│
├── nginx/
│   └── default.conf
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
│
└── .github/
    └── workflows/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/niessohdfgs/django-modern-backend.git
cd django-modern-backend
```

Build and start services:

```bash
docker compose up --build
```

Run migrations:

```bash
docker compose exec backend python manage.py migrate
```

Create a superuser:

```bash
docker compose exec backend python manage.py createsuperuser
```

---

## Development Workflow

```text
Create Feature
      │
      ▼
Commit Changes
      │
      ▼
Push To GitHub
      │
      ▼
GitHub Actions
      │
      ▼
Validation & Testing
```

---

## Learning Outcomes

This project provided practical experience with:

- Django Architecture
- ASGI Applications
- Docker Ecosystem
- PostgreSQL Integration
- Redis Messaging
- Celery Workers
- WebSocket Communication
- Reverse Proxy Configuration
- GitHub Actions
- CI Workflows

---

## Future Improvements

- JWT Authentication
- REST API Expansion
- Kubernetes Deployment
- Monitoring and Logging
- Prometheus
- Grafana
- Automatic Deployments
- SSL/TLS Integration
- Production Hardening

---

## Author

Hossein Seyedzadeh

Backend Developer

Focused on building scalable backend systems with Django and modern infrastructure tools.

---

## License

This project is available for educational and portfolio purposes.
