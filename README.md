# 🚀 Resilient Deployment System

A production-grade DevOps + Cybersecurity project demonstrating self-healing infrastructure, automated CI/CD, real-time monitoring, and security best practices.

![GitHub Actions](https://github.com/ZorawarSinghKhan/resilient-deployment-system/actions/workflows/deploy.yml/badge.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [CI/CD Pipeline](#cicd-pipeline)
- [Security](#security)
- [Monitoring and Alerts](#monitoring-and-alerts)
- [Cloud Deployment](#cloud-deployment)

## 🌟 Overview

This project builds a system that:
- Detects application failures automatically
- Restarts crashed pods without human intervention (self-healing)
- Monitors everything in real-time with Prometheus and Grafana
- Secures the infrastructure with RBAC and vulnerability scanning
- Deploys automatically on every code push via GitHub Actions

## 🏗️ Architecture

Developer pushes code
        ↓
GitHub Actions CI/CD Pipeline
        ↓
  1. Run Tests (pytest)
  2. Build Docker Image
  3. Trivy Security Scan
        ↓
Kubernetes Cluster (Minikube / GKE-ready)
        ↓
  Pod 1: Flask App
  Pod 2: Flask App  (2 replicas, auto-healing)
        ↓
Prometheus (Metrics) → Grafana (Dashboard + Alerts)

## ✅ Features

| Feature | Description |
|---------|-------------|
| Self-Healing | Kubernetes restarts crashed pods automatically |
| Auto-Scaling | 2 replicas with load balancing |
| CI/CD Pipeline | GitHub Actions runs on every git push |
| Security Scanning | Trivy scans for HIGH/CRITICAL vulnerabilities |
| RBAC | Role-based access control for Kubernetes |
| Monitoring | Prometheus + Grafana real-time dashboards |
| Alerting | Alerts for pod crashes and high memory usage |
| GKE-Ready | Designed for Google Kubernetes Engine |

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python Flask | Web application |
| Docker | Containerization |
| Kubernetes | Orchestration + Self-healing |
| Minikube | Local Kubernetes cluster |
| Prometheus | Metrics collection + Alerting |
| Grafana | Visual dashboards |
| GitHub Actions | CI/CD automation |
| Trivy | Docker image security scanning |
| Helm | Kubernetes package manager |
| RBAC | Kubernetes access control |

## 📁 Project Structure

chaos-project/
├── app.py                        # Flask app (/, /health, /crash)
├── Dockerfile                    # Container definition
├── deployment.yaml               # K8s deployment (2 replicas)
├── service.yaml                  # K8s service (NodePort 30007)
├── rbac.yaml                     # RBAC security config
├── prometheus-alerts.yaml        # Alerting rules
├── tests/
│   └── test_app.py               # Automated tests
└── .github/
    └── workflows/
        └── deploy.yml            # GitHub Actions pipeline

## 🚀 Quick Start

### Prerequisites
- Docker Desktop
- Minikube
- kubectl
- Helm

### 1. Clone the repo
git clone https://github.com/ZorawarSinghKhan/resilient-deployment-system
cd resilient-deployment-system

### 2. Start Minikube
minikube start

### 3. Deploy the app
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

### 4. Apply security
kubectl apply -f rbac.yaml

### 5. Apply Prometheus alerts
kubectl apply -f prometheus-alerts.yaml

### 6. Install monitoring stack
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

### 7. Access the app
minikube service chaos-app-service

### 8. Test self-healing
curl http://localhost:30007/crash
kubectl get pods -w

## 🤖 CI/CD Pipeline

Every git push triggers GitHub Actions automatically:

✅ Checkout code
✅ Set up Python
✅ Install dependencies
✅ Run pytest tests
✅ Build Docker image
✅ Trivy security scan

## 🔐 Security

### Trivy Vulnerability Scanning
- Scans Docker image on every push
- Detects HIGH and CRITICAL vulnerabilities
- Part of the CI/CD pipeline

### Kubernetes RBAC
- Custom ServiceAccount for the app
- Read-only access (get, list, watch)
- Principle of least privilege

## 📊 Monitoring and Alerts

### Start Grafana
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
Open http://localhost:3000

### Prometheus Alerts
| Alert | Trigger | Severity |
|-------|---------|----------|
| PodCrashing | Pod restarts more than 3 times | Critical |
| PodNotRunning | No pods running | Critical |
| HighMemoryUsage | Memory more than 100MB | Warning |

## ☁️ Cloud Deployment (GKE-Ready)

This project is designed to run on Google Kubernetes Engine:

gcloud container clusters create resilient-cluster \
  --num-nodes=2 \
  --machine-type=e2-medium \
  --region=us-central1 \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=3

gcloud container clusters get-credentials resilient-cluster --region=us-central1

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f rbac.yaml
kubectl apply -f prometheus-alerts.yaml

## 👨‍💻 Author

ZorawarSinghKhan
GitHub: https://github.com/ZorawarSinghKhan
