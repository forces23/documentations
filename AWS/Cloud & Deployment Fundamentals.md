![1756310389705](image/Cloud&DeploymentFundamentals/1756310389705.png)


# Docker & Containerization

* **Core Concepts** :
  * Container vs Virtual Machine
  * Images vs Containers
  * Dockerfile (build custom images)
  * Docker Hub (public/private images)
* **Container Lifecycle** :
  * `docker build`, `docker run`, `docker ps`, `docker stop`, `docker rm`
* **Docker Compose** :
  * Multi-container apps
  * `docker-compose.yml` structure (services, networks, volumes)
  * Linking frontend, backend, database containers
* **Best Practices** :
  * Lightweight images
  * Avoid storing secrets in images
  * Persistent volumes for databases

# AWS Basics

* **Compute** :
  * EC2 (Elastic Compute Cloud) instances
  * Key pairs, security groups, and networking basics (VPC, subnets)
* **Storage** :
  * S3 buckets (object storage)
  * Versioning, lifecycle policies, public/private access
* **Databases** :
  * RDS (PostgreSQL) setup and connections
  * Automated backups and snapshots
* **Identity & Access** :
  * IAM users, groups, and roles
  * Permissions and policies
  * Least privilege principle

# Serverless

* **AWS Lambda** :
  * Event-driven functions
  * Triggers: API Gateway, S3 events, DynamoDB streams
  * Stateless functions
* **API Gateway** :
  * REST API setup
  * Endpoint routing and request/response mapping
  * Authentication & rate limiting

# CI/CD (Continous Integration / Continous Deployment)

* **Version Control Integration** : GitHub Actions, GitLab CI/CD
* **Pipelines** :
  * Build, test, deploy automation
  * Running unit tests before deployment
  * Environment variables and secrets management
* **Deployment Strategies** :
  * Blue/Green deployment
  * Rolling updates

# Deployment Options

* **AWS Elastic Beanstalk** :
  * PaaS for deploying web applications
  * Automatic load balancing, scaling, and health monitoring
* **AWS ECS / EKS** :
  * Container orchestration (Docker containers in clusters)
  * Scheduling, scaling, and service discovery
* **AWS Amplify (Frontend Hosting)** :
  * React app hosting
  * CI/CD integration with GitHub
  * Domain management

# Monitoring & Logging

* CloudWatch for logs and metrics
* Health checks on EC2, RDS, and Elastic Beanstalk apps
* Alerts and notifications (SNS / CloudWatch alarms)

# Security Best Practices

* Use IAM roles for services instead of long-term credentials
* Enable HTTPS / TLS for all endpoints
* Network isolation with VPCs, subnets, and security groups
* Encrypt data at rest (S3, RDS) and in transit
