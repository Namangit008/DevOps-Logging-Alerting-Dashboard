# DevOps Monitoring and Alerting Dashboard 🚀

This project demonstrates a real-time monitoring and alerting system for a backend service using Grafana, Loki, MongoDB, and Docker.

## 🔧 Tech Stack
- Docker & Docker Compose
- Loki + Promtail
- Grafana
- MongoDB & Mongo Express
- Node.js (Backend Logging App)
- Email Alerts via Grafana

## 📊 Features
- Real-time backend log collection and filtering with Loki
- Custom Grafana dashboard with alert rules and visualizations
- MongoDB UI interface via Mongo Express
- Alerting setup with email notification on error logs

## 📁 Project Structure
```bash
.
├── backend/                # Simple Node.js app for logging
│   └── logs/app.log        # Application logs for monitoring
├── docker-compose.yml      # Service definitions
├── grafana/                # Grafana provisioning & config
├── loki-config.yaml        # Loki configuration file
├── promtail-config.yaml    # Promtail configuration file
└── screenshots/            # Project screenshots
```

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose installed

### Setup
```bash
git clone https://github.com/Namangit008/devops-monitoring-dashboard.git
cd devops-monitoring-dashboard
docker-compose up -d
```

### Access Services
- Grafana: http://localhost:3001
- Mongo Express: http://localhost:8081
- Backend: http://localhost:8080

## 📷 Screenshots

### Mongo Express Databases
![Mongo Express](screenshots/mongo-express.png)

### Application Logs Viewer
![App Logs](screenshots/app-logs.png)

### Grafana Home
![Grafana Home](screenshots/grafana-home.png)

### Loki Data Source
![Loki Setup](screenshots/loki-config.png)

### Log Explorer Panel
![Log Explorer](screenshots/log-panel.png)

### Custom Grafana Dashboard
![Grafana Dashboard](screenshots/custom-dashboard.png)

### Alert Configuration
![Alert Rule](screenshots/alert-rule.png)

### Email Notification Alert
![Email Alert](screenshots/email-alert.png)

## 📫 Contact
Created by [Naman Jain](https://www.linkedin.com/in/naman-jain-73b795266?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) — feel free to reach out!

## 📝 License
This project is open source and available under the [MIT License](LICENSE).
