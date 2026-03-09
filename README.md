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
The Sathyabama AI Chatbot features a modern, cloud-native architecture:
- **Frontend**: Premium glassmorphism UI built with HTML5, CSS3, and JavaScript.
- **Backend**: Flask-based REST API with asynchronous Gemini 2.0 integration.
- **AI Engine**: Hybrid model using static FAQ mapping and Google Generative AI fallback.
- **Containerization**: Dockerized deployment optimized for GCP Compute Engine.

✨ Features
- **Modern UI**: Sleek, resume-ready interface with AI-generated university-themed backgrounds.
- **Intelligent Responses**: Leverages Google Gemini for natural language understanding.
- **Real-time Interaction**: Asynchronous chat experience with typing indicators.
- **Observability**: Ready for Prometheus and Grafana monitoring.

📂 Project Structure
sathyabama-chatbot/
├── app.py                # Flask Application Entry
├── chatbot_engine.py      # AI & FAQ Logic
├── Dockerfile            # Container Configuration
├── .dockerignore         # Docker Build Optimization
├── requirements.txt      # Python Dependencies
├── templates/
│   └── index.html        # Modern Glassmorphism UI
└── static/               # AI Generated Assets
    ├── chatbot_bg.png
    └── bot_icon.png
🧠 DevOps Concepts Implemented

Application containerization

Cloud VM deployment

Port exposure & firewall rules

Service separation (App + Monitoring)

Metrics scraping

Dashboard visualization

Linux-based infrastructure management

� Local Installation
```bash
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

# Download NLTK data (handled automatically in Docker)
python -m nltk.downloader punkt wordnet omw-1.4

# Run application
python app.py
```

🐳 Docker Deployment
```bash
# Build the production image
docker build -t sathyabama-chatbot .

# Run the container (Mapping port 7234)
# Note: You must provide your GEMINI_API_KEY as an env variable
docker run -d \
  -p 7234:7234 \
  --name chatbot \
  -e GEMINI_API_KEY="your_api_key_here" \
  sathyabama-chatbot

# Verify container status
docker ps

# Check logs if needed
docker logs -f chatbot
```

☁️ GCP Deployment (GCE)
- **Engine**: Google Compute Engine (Ubuntu 22.04 LTS)
- **Firewall**: Enable **TCP 7234** for app traffic and **9090/3000** for monitoring.
- **Access**: `http://<VM_EXTERNAL_IP>:7234`

�🚀 Future Enhancements

Jenkins CI/CD pipeline integration

HTTPS with Nginx reverse proxy

Kubernetes deployment

Auto-scaling setup

Prometheus Alertmanager integration

Centralized logging (ELK Stack)



👨‍💻 Author

Ashwath R M
DevOps & Cloud Enthusiast
