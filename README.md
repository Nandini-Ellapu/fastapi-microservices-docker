FastAPI Microservices with Docker & NGINX Gateway

A complete microservices project built using FastAPI, Docker, Docker Compose, and NGINX as an API Gateway.
This project demonstrates how to run multiple backend services behind a single gateway on a cloud server such as AWS EC2.

Project Architecture
               ┌───────────────────┐
               │ NGINX API Gateway │  ← Exposes port 80
               └───────────────────┘
                     │     │     │
     ┌───────────────┘     │     └──────────────────────────┐
     │                     │                                 │
┌─────────────┐     ┌──────────────┐                ┌────────────────┐
│ User Service│     │Product Service│                │ Order Service  │
│  Port 8001  │     │  Port 8002   │                │   Port 8003    │
└─────────────┘     └──────────────┘                └────────────────┘

Folder Structure
fastapi-microservices-docker/
│
├── user-service/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── product-service/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── order-service/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── default.conf
│
└── docker-compose.yml

Services Overview
User Service

Endpoint: /users

Runs on port 8001

Product Service

Endpoint: /products

Runs on port 8002

Order Service

Endpoint: /orders

Runs on port 8003

NGINX API Gateway

Routes incoming traffic:

/users    → user-service:8001
/products → product-service:8002
/orders   → order-service:8003

How to Run the Project
1. Clone the Repository
git clone https://github.com/Nandini-Ellapu/fastapi-microservices-docker.git
cd fastapi-microservices-docker

2. Build and Start All Services
docker compose up -d --build

3. Check Running Containers
docker compose ps

API Endpoints

Use your EC2 Public IP:

http://<SERVER-IP>/users
http://<SERVER-IP>/products
http://<SERVER-IP>/orders

NGINX Configuration (default.conf)
server {
    listen 80;

    location /users/ {
        proxy_pass http://user-service:8001/;
    }

    location /products/ {
        proxy_pass http://product-service:8002/;
    }

    location /orders/ {
        proxy_pass http://order-service:8003/;
    }
}

Skills Demonstrated

FastAPI

Microservices Architecture

Docker & Docker Compose

NGINX Reverse Proxy

AWS EC2 Deployment

Linux

Git & GitHub

Containerized API Development

Future Improvements

JWT Authentication

Database Integration (PostgreSQL)

Monitoring (Prometheus + Grafana)

HTTPS with Certbot or AWS Load Balancer

CI/CD Pipeline (GitHub Actions or Azure DevOps)

Deploy using Kubernetes

Author

Nandini Ellapu
FastAPI | Docker | Microservices | DevOps | Cloud
