🚀 FastAPI Microservices with Docker, NGINX Gateway & AWS Deployment

A production-ready microservices architecture built using:

FastAPI for backend services

Docker for containerization

Docker Compose for orchestration

NGINX as API Gateway & Reverse Proxy

AWS EC2 for cloud deployment

This project demonstrates how multiple independent services can run in isolated containers and communicate through a centralized gateway.

📌 Features

✔ Three independent FastAPI microservices
✔ Central NGINX API Gateway
✔ Clean folder structure
✔ Dockerized services with simple one-command startup
✔ Cloud-ready (EC2, ECS, Azure, GCP, etc.)
✔ Simplified routing and service discovery
✔ Easily extendable (DB, Auth, CI/CD, Monitoring)

🏗️ Architecture Overview
                   +---------------------------+
                   |     NGINX API Gateway     |
                   |         (Port 80)         |
                   +-------------+-------------+
                                 |
        ---------------------------------------------------
        |                       |                         |
+---------------+     +-----------------+      +-----------------+
| User Service  |     | Product Service |      | Order Service   |
|   Port 8001   |     |    Port 8002    |      |    Port 8003    |
+---------------+     +-----------------+      +-----------------+


NGINX receives client requests and forwards them to the correct backend service.

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

⚡ Microservices Overview
👤 User Service

Returns a list of users.
Route: /users
Port: 8001

📦 Product Service

Returns product catalog.
Route: /products
Port: 8002

🧾 Order Service

Returns order details.
Route: /orders
Port: 8003

🌐 NGINX API Gateway

Handles all traffic to:

/users → User Service

/products → Product Service

/orders → Order Service

🐳 Run With Docker (Local or EC2)
1️⃣ Clone the repository
git clone https://github.com/Nandini-Ellapu/fastapi-microservices-docker.git
cd fastapi-microservices-docker

2️⃣ Start all services
docker compose up -d --build

3️⃣ Check running containers
docker compose ps

🌍 API Endpoints

Replace <SERVER-IP> with your EC2 Public IP:

Service	URL
Users	http://<SERVER-IP>/users
Products	http://<SERVER-IP>/products
Orders	http://<SERVER-IP>/orders
🔧 NGINX Configuration (default.conf)
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

🛠️ Tech Stack

FastAPI

Python 3.11

Docker & Docker Compose

NGINX

AWS EC2

Linux (Ubuntu)

🚀 Future Enhancements (Recommended for Portfolio)

Add PostgreSQL or MongoDB

JWT Authentication (Login/Register)

CI/CD Pipeline (GitHub Actions or Azure DevOps)

Monitoring with Prometheus + Grafana

Deploy on AWS ECS Fargate / Azure Container Apps

Add HTTPS using Certbot or AWS Load Balancer

👩‍💻 Author

Nandini Ellapu
FastAPI | Docker | Microservices | DevOps | Cloud
