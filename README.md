# FastAPI Microservices with Docker and NGINX Gateway

This project demonstrates a microservices architecture using FastAPI, Docker, Docker Compose, and NGINX as an API Gateway.

## Services Included

### User Service
- Endpoint: /users
- Port: 8001

### Product Service
- Endpoint: /products
- Port: 8002

### Order Service
- Endpoint: /orders
- Port: 8003

### NGINX API Gateway
Routes incoming traffic to the correct backend service.

---

## Folder Structure
fastapi-microservices-docker/
- user-service/
- product-service/
- order-service/
- nginx/
- docker-compose.yml

---

## How to Run

### Clone the Repository
git clone https://github.com/Nandini-Ellapu/fastapi-microservices-docker.git
cd fastapi-microservices-docker

### Build and Start Containers
docker compose up -d --build

### Check Status
docker compose ps

---

## API Endpoints
http://<SERVER-IP>/users
http://<SERVER-IP>/products
http://<SERVER-IP>/orders

---

## NGINX Configuration

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

---

## Skills Demonstrated
- FastAPI
- Docker
- Docker Compose
- Microservices
- NGINX Reverse Proxy
- AWS EC2 Deployment
- GitHub Version Control
