# Monitoring-Dockerized-Microservice-with-Prometheus-and-Grafana-using-Ansible
## 📖 Project Overview
This project shows how to:
- Create a Flask microservice with Prometheus metrics.
- Build Prometheus, Node Exporter, and Grafana manually (without using DockerHub images).
- Use Ansible to automate everything on **localhost**.
- Monitor your microservice and visualize metrics on Grafana dashboards.

---

## 🛠️ Tech Stack Used
- Docker
- Ansible
- Prometheus
- Grafana
- Flask (Python)

---

## 📂 Project Folder Structure
ansible/
│
├── inventory.ini
├── playbook.yaml
│
├── prometheus/           # Prometheus files (Dockerfile, prometheus.yml)
│
├── node_exporter/        # Node Exporter files (Dockerfile)
│
├── grafana/              # Grafana files (Dockerfile)
│
├── roles/
│   ├── docker/           # Docker install tasks
│   ├── prometheus/       # Prometheus deploy tasks
│   ├── node_exporter/    # Node Exporter deploy tasks
│   └── grafana/          # Grafana deploy tasks
│
└── flask-microservice/   # Microservice app files (Dockerfile, app.py)





🔗 Medium Blog
👉 Step-by-Step Project Guide on Medium (https://medium.com/@priyamsanodiya340/monitoring-a-dockerized-microservice-application-with-prometheus-and-grafana-using-ansible-without-c19f88a0b182)

