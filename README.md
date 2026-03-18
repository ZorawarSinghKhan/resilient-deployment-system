# Resilient Deployment System

## 📌 Overview
This project demonstrates a system that automatically recovers from application failures using Kubernetes. It ensures high availability and reliability of applications.

## 🚀 Tech Stack
- Docker
- Kubernetes
- Jenkins (CI/CD)
- GitHub

## ⚙️ Features
- Containerized application using Docker
- Deployment using Kubernetes
- Auto-healing (self-recovery)
- Failure simulation
- CI/CD pipeline (concept using Jenkins)
- Version control using GitHub

## 🔄 How It Works
1. Application is containerized using Docker
2. Deployed on Kubernetes
3. Failure is triggered using `/crash` endpoint
4. Kubernetes automatically restarts the application
5. System continues running without downtime

## 🎯 Purpose
To build a resilient system that can handle failures automatically and ensure continuous application availability.

## 👥 Team Roles
- Application Development
- Docker Containerization
- Kubernetes Deployment
- CI/CD Pipeline (Jenkins)
- Testing & Reliability

## 💡 Key Concept
This project focuses on building a **self-healing system** that can recover from failures without manual intervention.
