# Resilient Deployment System

## Overview

Resilient Deployment System is a Kubernetes-based deployment validation and resilience testing platform designed to demonstrate self-healing, scalability, observability, and fault tolerance of cloud-native applications.

The project deploys a Flask application inside Kubernetes and uses Chaos Mesh to inject controlled failures while Prometheus and Grafana monitor system behavior in real time.

## Objectives

- Demonstrate Kubernetes self-healing capabilities
- Validate application resilience under failures
- Monitor application and infrastructure metrics
- Test scalability and recovery mechanisms
- Provide a platform for resilience testing of containerized applications

## Technology Stack

- Python (Flask)
- Docker
- Kubernetes
- Minikube
- Chaos Mesh
- Prometheus
- Grafana
- Git & GitHub

## Project Structure

text chaos-project/ │ ├── app.py ├── Dockerfile ├── README.md │ ├── chaos/ │   ├── cpu-stress.yaml │   ├── memory-stress.yaml │   ├── network-delay.yaml │   ├── packet-loss.yaml │   └── pod-chaos.yaml │ ├── kubernetes/ │   ├── deployment.yaml │   ├── service.yaml │   ├── network-policy.yaml │   └── rbac.yaml │ ├── monitoring/ │   └── prometheus-alerts.yaml │ ├── docs/ │ └── tests/ 

## Features

### Self-Healing
- Automatic pod recovery
- Application crash recovery
- Container restart and recovery

### Scalability
- Horizontal scaling using Kubernetes replicas
- Dynamic workload distribution

### Monitoring
- Prometheus metrics collection
- Grafana dashboards
- CPU and memory monitoring

### Chaos Engineering
- Controlled fault injection using Chaos Mesh
- Failure simulation and recovery validation

## Testing Performed

| Test | Status |
|--------|---------|
| Pod Kill Test | PASS |
| Application Crash Test | PASS |
| CPU Stress Test | PASS |
| Memory Stress Test | PASS |
| Scalability Test | PASS |
| Network Delay Test | PASS |
| Packet Loss Test | PASS |
| Container Kill Test | PASS |
| Service Failure Test | PASS |

## Results

The system successfully demonstrated Kubernetes self-healing and resilience capabilities. Multiple failure scenarios were injected and automatically recovered without manual intervention.

The platform validated:
- Application recovery
- Container recovery
- Pod recovery
- Service restoration
- Resource stress handling
- Network fault tolerance
- Scalability under increased load

## Future Enhancements

- AWS Cloud Deployment
- Trivy Security Scanning
- Horizontal Pod Autoscaler (HPA)
- Alertmanager Integration
- Automated Recovery Workflows
- Custom Dashboard for Chaos Testing

## Author

Ashutosh Chaudhary

B.Tech CSE (DevOps & Cloud Computing)

SRM University Delhi-NCR, Sonipat
