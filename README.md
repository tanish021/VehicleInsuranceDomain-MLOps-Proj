# 🚗 Vehicle Insurance Prediction | End-to-End MLOps Project

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikitlearn)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)
![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonaws)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions)

### 🚀 Production-Ready Machine Learning Pipeline with AWS, Docker & CI/CD

</div>

---

# 📖 Overview

This project demonstrates how a Machine Learning model can be developed, deployed, monitored, and maintained using modern **MLOps practices**.

The objective of this project is to predict whether a customer is likely to purchase a vehicle insurance policy based on customer demographics and vehicle-related information.

Unlike a traditional Machine Learning notebook, this project follows a **production-grade modular architecture** incorporating data ingestion, validation, transformation, model training, evaluation, model registry, prediction pipeline, Docker containerization, CI/CD automation, and AWS deployment.

---

# ✨ Key Features

- ✅ End-to-End MLOps Pipeline
- ✅ Modular Code Architecture
- ✅ MongoDB Atlas Integration
- ✅ Data Validation Pipeline
- ✅ Data Transformation Pipeline
- ✅ Model Training Pipeline
- ✅ Model Evaluation
- ✅ AWS S3 Model Registry
- ✅ Prediction Pipeline
- ✅ FastAPI Web Application
- ✅ Docker Containerization
- ✅ GitHub Actions CI/CD
- ✅ Self Hosted GitHub Runner
- ✅ AWS EC2 Deployment
- ✅ AWS ECR Integration
- ✅ Logging & Exception Handling
- ✅ Production Ready Project Structure

---

# 🏗️ Project Architecture

```text
                   MongoDB Atlas
                         │
                         ▼
                 Data Ingestion
                         │
                         ▼
                 Data Validation
                         │
                         ▼
              Data Transformation
                         │
                         ▼
                 Model Training
                         │
                         ▼
                Model Evaluation
                         │
                         ▼
                Model Registry
                    (AWS S3)
                         │
                         ▼
               Prediction Pipeline
                         │
                         ▼
                  FastAPI Application
                         │
                         ▼
                    Docker Image
                         │
                         ▼
                      AWS ECR
                         │
                         ▼
                    AWS EC2 Server
```

---

# 📂 Project Structure

```text
VehicleInsuranceDomain-MLOps-Proj
│
├── src
│   ├── components
│   ├── configuration
│   ├── constants
│   ├── data_access
│   ├── entity
│   ├── exception
│   ├── logger
│   ├── pipeline
│   └── utils
│
├── static
├── templates
├── app.py
├── demo.py
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── setup.py
└── README.md
```

---

# ⚙️ Complete Project Workflow

```text
Constants
     │
     ▼
Config Entity
     │
     ▼
Artifact Entity
     │
     ▼
Components
     │
     ▼
Training Pipeline
     │
     ▼
Prediction Pipeline
     │
     ▼
FastAPI Application
```

---

# 🤖 Machine Learning Pipeline

```text
Raw Dataset
     │
     ▼
Data Ingestion
     │
     ▼
Data Validation
     │
     ▼
Data Transformation
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Model Pusher (AWS S3)
     │
     ▼
Prediction Pipeline
```

---

# ☁️ AWS Services Used

- IAM
- S3 (Model Registry)
- ECR (Docker Image Registry)
- EC2 (Application Hosting)
- AWS CLI

---

# 🐳 Docker

The application is containerized using Docker to ensure consistency across different environments.

**Benefits:**

- Consistent Deployment
- Easy Scalability
- Portable Environment
- Dependency Isolation

---

# ⚡ CI/CD Pipeline

```text
Developer
     │
     ▼
Git Push
     │
     ▼
GitHub Actions
     │
     ├── Install Dependencies
     ├── Build Docker Image
     ├── Push Docker Image to AWS ECR
     └── Deploy to AWS EC2
     │
     ▼
Production Server
```

---

# 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Backend | FastAPI |
| Machine Learning | Scikit-Learn, Pandas, NumPy |
| Database | MongoDB Atlas |
| Cloud | AWS EC2, AWS S3, AWS ECR, IAM |
| DevOps | Docker, GitHub Actions |
| Version Control | Git, GitHub |

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/tanish021/VehicleInsuranceDomain-MLOps-Proj.git
```

## Create Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
```

## Activate Environment

```bash
conda activate vehicle
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Run Training Pipeline

Open the following route after starting the application:

```text
http://localhost:5000/train
```

---

# ▶️ Run the Application

```bash
python app.py
```

Visit:

```text
http://localhost:5000
```

---

# 📁 Model Deployment Workflow

```text
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
AWS S3 Model Registry
      │
      ▼
Prediction Pipeline
      │
      ▼
FastAPI API
      │
      ▼
Docker Container
      │
      ▼
AWS EC2 Deployment
```

---

# 🌟 Skills Demonstrated

- Machine Learning
- MLOps
- Data Engineering
- Software Engineering
- Docker
- AWS Cloud
- FastAPI
- MongoDB
- GitHub Actions
- CI/CD
- Model Deployment
- Production ML Pipelines

---

# 📊 Project Highlights

✔ Modular Code Structure

✔ Production Ready Architecture

✔ Cloud Integrated

✔ Dockerized Application

✔ Automated CI/CD Pipeline

✔ Model Registry using AWS S3

✔ End-to-End Deployment

✔ FastAPI Backend

✔ Logging & Exception Handling

---

# 📸 Screenshots

> Add screenshots of your application here.

Example:

- Home Page
- Prediction Page
- Training Logs
- AWS Deployment
- GitHub Actions Workflow

---

# 🔮 Future Improvements

- MLflow Integration
- DVC Pipeline
- Model Monitoring
- Data Drift Detection
- Automated Retraining
- Kubernetes Deployment
- Prometheus & Grafana Monitoring
- Terraform Infrastructure Automation

---

# 👨‍💻 Author

**Tanish Shishodia**

🎓 B.Tech Computer Science Engineering

💡 Aspiring Machine Learning Engineer | MLOps Enthusiast

### Connect with Me

- GitHub: https://github.com/tanish021
- LinkedIn: https://www.linkedin.com/in/tanish-shishodia-20243a2a8/?skipRedirect=true

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

</div>