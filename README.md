🚀 FastAPI Microservices with Docker & NGINX Gateway

A complete microservices project built using FastAPI, Docker, Docker Compose, and NGINX as an API Gateway.
This project demonstrates how to run multiple backend services behind a single gateway in a cloud environment such as AWS EC2.

🧱 Project Architecture
         ┌─────────────────┐
         │  User Service   │ → FastAPI (Port 8001)
         └─────────────────┘
                   │
                   ▼
         ┌─────────────────┐
Client → │   NGINX API     │ → Routes to /users, /products, /orders
         │     Gateway     │ → Exposes Port 80
         └─────────────────┘
                   │
 ┌─────────────────┴─────────────────┬─────────────────┐
 │                                   │                 │
 ▼                                   ▼                 ▼
User Service                   Product Service     Order Service
(Port 8001)                    (Port 8002)         (Port 8003)

📁 Folder Structure
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

⚡ Services Overview
🧑‍🤝‍🧑 User Service

Endpoint: /users

Runs on port 8001

Simple FastAPI service that returns a user list.

📦 Product Service

Endpoint: /products

Runs on port 8002

Returns product list.

🧾 Order Service

Endpoint: /orders

Runs on port 8003

Returns order details.

🌐 NGINX API Gateway

Routes:

/users    → user-service:8001
/products → product-service:8002
/orders   → order-service:8003


Exposes port 80 to the internet.

🐳 Run Project with Docker Compose
1️⃣ Clone the Repository
git clone https://github.com/Nandini-Ellapu/fastapi-microservices-docker.git
cd fastapi-microservices-docker

2️⃣ Build and Start All Microservices
docker compose up -d --build

3️⃣ Check Running Containers
docker compose ps

🌍 API Endpoints

Use your server IP (EC2 Public IP) or localhost:

User Service
http://<SERVER-IP>/users

Product Service
http://<SERVER-IP>/products

Order Service
http://<SERVER-IP>/orders

🔧 NGINX Gateway Configuration
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

🚀 Skills Demonstrated

✔ FastAPI
✔ Microservices Architecture
✔ Docker & Docker Compose
✔ NGINX Reverse Proxy
✔ AWS EC2 Deployment
✔ Linux Commands
✔ Git & GitHub
✔ Containerized API development

This project is excellent for DevOps, Cloud (AWS/Azure), Backend, and Microservices portfolios.

📌 Future Improvements

You can enhance the project with:

JWT Authentication

Database Integration (PostgreSQL)

Monitoring (Prometheus + Grafana)

HTTPS SSL (Certbot or AWS Load Balancer)

Autoscaling using ECS or Kubernetes

CI/CD Pipeline (GitHub Actions or Azure DevOps)

👩‍💻 Author

Nandini Ellapu
FastAPI | Docker | Microservices | DevOps | Cloud Enthusiast
