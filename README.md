🎓 Sathyabama AI Chatbot
Cloud-Native Containerized Deployment with Monitoring on GCP
🚀 Project Overview

Sathyabama AI Chatbot is an intelligent academic assistant built for answering university-related queries.

The application is developed using Flask, NLTK, and Google Generative AI (Gemini) and deployed as a Docker container on Google Cloud Platform (GCP).

A separate monitoring stack using Prometheus and Grafana provides real-time observability, metrics tracking, and dashboard visualization.

This project demonstrates practical implementation of:

AI-powered web applications

Docker containerization

Cloud deployment on GCP

Observability using Prometheus & Grafana

Production-style infrastructure separation

🏗️ Architecture
4
Architecture Components
Component	Description
Chatbot VM	Hosts Dockerized Flask application
Docker Container	Runs chatbot service on port 7234
Prometheus VM	Scrapes chatbot metrics
Grafana	Visualizes real-time dashboards
GCP Compute Engine	Cloud infrastructure
✨ Features

AI-powered responses using Google Gemini

Static FAQ-based university information

Dynamic intelligent query handling

Web-based chatbot interface

Dockerized application

Cloud-hosted on GCP VM

Real-time metrics exposure

Dedicated monitoring instance

Custom Grafana dashboards

🛠️ Tech Stack
Backend

Python

Flask

NLTK

Google Generative AI (Gemini API)

Frontend

HTML

CSS

JavaScript

DevOps & Cloud

Docker

Linux (Ubuntu)

Google Cloud Platform (Compute Engine)

Firewall Configuration

Monitoring

Prometheus

Grafana

Flask Metrics Exporter

📦 Local Installation
# Clone repository
git clone https://github.com/yourusername/sathyabama_chatbot.git
cd sathyabama_chatbot

# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -m nltk.downloader punkt wordnet omw-1.4

# Run application
python app.py

Access locally:

http://localhost:7234
🐳 Docker Deployment
Build Image
docker build -t sathyabama-chatbot .
Run Container
docker run -d -p 7234:7234 --name chatbot sathyabama-chatbot
Verify
docker ps

Application URL:

http://<VM_EXTERNAL_IP>:7234
☁️ GCP Deployment

Platform:

Google Cloud Compute Engine (Ubuntu VM)

Application Port:

7234

Firewall Ports Enabled:

Port	Purpose
7234	Chatbot Application
9090	Prometheus
3000	Grafana

Example firewall rule:

gcloud compute firewall-rules create allow-chatbot \
--allow tcp:7234
📊 Monitoring & Observability
Prometheus

Installed on a separate VM instance

Scrapes chatbot metrics endpoint

Example scrape config:

scrape_configs:
  - job_name: "chatbot"
    static_configs:
      - targets: ["<CHATBOT_PRIVATE_IP>:7234"]

Metrics endpoint:

http://<CHATBOT_IP>:7234/metrics
Grafana

Connected to Prometheus as data source

Custom dashboards created

Metrics monitored:

Total HTTP requests

Request latency

CPU usage

Memory usage

Application uptime

Container health

Access:

http://<PROMETHEUS_VM_IP>:3000
📂 Project Structure
sathyabama-chatbot/

├── app.py
├── Dockerfile
├── requirements.txt
├── .env
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
🧠 DevOps Concepts Implemented

Application containerization

Cloud VM deployment

Port exposure & firewall rules

Service separation (App + Monitoring)

Metrics scraping

Dashboard visualization

Linux-based infrastructure management

🚀 Future Enhancements

Jenkins CI/CD pipeline integration

HTTPS with Nginx reverse proxy

Kubernetes deployment

Auto-scaling setup

Prometheus Alertmanager integration

Centralized logging (ELK Stack)



👨‍💻 Author

Ashwath R M
DevOps & Cloud Enthusiast
