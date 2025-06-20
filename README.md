# Monitoring-Dockerized-Microservice-with-Prometheus-and-Grafana-using-Ansible
)
📖 Project Overview
This project demonstrates how to monitor a Dockerized Flask microservice using Prometheus and Grafana.
Key highlights:

No DockerHub images used (manual installation and custom Dockerfile builds)

Fully automated with Ansible on localhost

Flask microservice with Prometheus metrics integration

Real-time Grafana dashboards

🛠️ Tech Stack
Docker

Ansible

Prometheus

Grafana

Flask (Python)

Node Exporter (Optional)

📂 Folder Structure
text
Copy
Edit
ansible/
├── inventory.ini
├── playbook.yaml
├── prometheus/
│   ├── Dockerfile
│   └── prometheus.yml
├── node_exporter/
│   ├── Dockerfile
├── grafana/
│   ├── Dockerfile
├── roles/
│   ├── docker/
│   │   └── tasks/
│   │       └── main.yml
│   ├── prometheus/
│   │   └── tasks/
│   │       └── main.yml
│   ├── node_exporter/
│   │   └── tasks/
│   │       └── main.yml
│   ├── grafana/
│       └── tasks/
│           └── main.yml
flask-microservice/
├── Dockerfile
└── app.py


🔗 Medium Blog
👉 Step-by-Step Project Guide on Medium (https://medium.com/@priyamsanodiya340/monitoring-a-dockerized-microservice-application-with-prometheus-and-grafana-using-ansible-without-c19f88a0b182)

