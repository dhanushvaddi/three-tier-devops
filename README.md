# 🚀 Three-Tier DevOps Project

This repository demonstrates a **production-style Three-Tier Architecture**
implemented using **Docker, Kubernetes, CI/CD, and Monitoring** with only
**free and open-source tools**.

This project is designed for **hands-on DevOps learning**, real-world
architecture understanding, and **interview readiness**.

---

## 🏗️ Architecture Overview

User
│
▼
Frontend (Nginx)
│
▼
Backend (Python Flask API)
│
▼
Database (PostgreSQL)


Monitoring Flow:
Application / Containers
▼
Prometheus
▼
Grafana


CI/CD Flow:
GitHub → Jenkins → Docker Image → Kubernetes


---

## 📁 Project Structure

three-tier-devops/
│
├── backend/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── frontend/
│ └── index.html
│
├── database/
│ └── init.sql
│
├── k8s/
│ ├── namespace.yaml
│ ├── backend-deployment.yaml
│ ├── frontend-deployment.yaml
│ ├── postgres-statefulset.yaml
│ ├── services.yaml
│ └── ingress.yaml
│
├── monitoring/
│ └── prometheus.yaml
│
├── docker-compose.yaml
├── Jenkinsfile
└── README.md


---

## 🧰 Tech Stack

- **Frontend:** Nginx
- **Backend:** Python (Flask)
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **Orchestration:** Kubernetes (Minikube / EKS)
- **CI:** Jenkins
- **Monitoring:** Prometheus & Grafana
- **Version Control:** Git & GitHub

---

## ▶️ Run Application Using Docker Compose

Start all services:
```bash
docker compose up -d
Stop services:

docker compose stop
Remove containers:

docker compose down
🌐 Access URLs (Docker Compose)
Service	URL
Frontend	http://localhost
Backend	http://localhost:5000
Prometheus	http://localhost:9090
Grafana	http://localhost:3000
Grafana Default Login:

Username: admin
Password: admin
☸️ Deploy Application to Kubernetes
Create namespace and deploy all resources:

kubectl apply -f k8s/
Check resources:

kubectl get all -n three-tier
Access frontend (NodePort):

minikube service frontend -n three-tier
🔄 CI/CD Pipeline (Jenkins)
Pipeline stages:

GitHub code checkout

Docker image build

Security scan using Trivy

Image push to container registry

Deployment to Kubernetes

The pipeline is defined in:

Jenkinsfile
📊 Monitoring
Prometheus collects metrics from containers and services

Grafana visualizes CPU, memory, and application metrics

Easily extendable with Alertmanager for alerts

🎯 Project Highlights
Implements Three-Tier Architecture

Uses Docker Compose for local development

Uses Kubernetes for container orchestration

CI pipeline with Jenkins

Security scanning using Trivy

Monitoring with Prometheus & Grafana

Clean and interview-ready repository structure
