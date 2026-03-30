# SchoolApp - Real-Time School Management System

A modern, scalable school management application built with real-time features using Flask-SocketIO, PostgreSQL, Docker, AWS, Terraform, and Kubernetes.

## Features

- **Real-Time Notifications**: Live updates via WebSocket connections
- **Dashboard**: Attendance, assignments, and notification tracking
- **Scalable Architecture**: Containerized with Kubernetes on AWS EKS
- **Database**: PostgreSQL for persistent data storage
- **CI/CD**: Automated deployment with GitHub Actions

## Architecture

### Backend (Flask + SocketIO)
- Real-time notifications with Flask-SocketIO
- PostgreSQL database integration
- RESTful API endpoints
- Containerized with Docker

### Frontend (HTML/JS + SocketIO)
- Responsive dashboard interface
- Real-time notification display
- SocketIO client for live updates

### Infrastructure (AWS)
- VPC with public/private subnets
- EKS cluster for Kubernetes orchestration
- RDS PostgreSQL database
- ALB Ingress for load balancing
- ECR for container registry

## Prerequisites

- AWS Account with appropriate permissions
- Terraform v1.0+
- kubectl configured for EKS
- GitHub repository with secrets configured

## Deployment Steps

### 1. Configure AWS and GitHub

**AWS Setup:**
- Create an IAM user with the following policies:
  - AmazonEC2ContainerRegistryFullAccess
  - AmazonEKSClusterPolicy
  - AmazonEKSWorkerNodePolicy
  - AmazonRDSFullAccess
  - AmazonVPCFullAccess
  - AmazonEC2FullAccess
- Generate access keys

**GitHub Secrets:**
- Go to your repo → Settings → Secrets and variables → Actions
- Add the following secrets:
  - `AWS_ACCESS_KEY_ID`: Your AWS access key
  - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key

### 2. Provision Infrastructure with Terraform

```bash
# Navigate to terraform directory
cd terraform

# Initialize Terraform
terraform init

# Plan the deployment
terraform plan -var="db_username=your_db_user" -var="db_password=your_secure_password"

# Apply the infrastructure
terraform apply -var="db_username=your_db_user" -var="db_password=your_secure_password"
```

This creates:
- VPC with subnets and NAT gateway
- EKS cluster with node groups
- RDS PostgreSQL instance
- Security groups and IAM roles

### 3. Update Kubernetes Secrets

After Terraform deployment, update the database URL in `k8s/secrets.yml`:

```yaml
data:
  database-url: <base64-encoded-connection-string>
  secret-key: <base64-encoded-secret-key>
```

### 4. Deploy Application

Push to GitHub main branch to trigger CI/CD:

```bash
git add .
git commit -m "Deploy to production"
git push origin main
```

The GitHub Actions workflow will:
- Build Docker images
- Push to ECR
- Deploy to EKS cluster

### 5. Access the Application

After deployment, get the ALB URL:

```bash
kubectl get ingress -n default
```

Access your app at the provided URL.

## Local Development

### Using Docker Compose

```bash
# Start all services locally
docker-compose up -d

# Access at:
# Frontend: http://localhost:8080
# Backend API: http://localhost:5000
```

### Manual Setup

```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend (serve static files)
cd frontend
python -m http.server 8080
```

## API Endpoints

- `GET /` - Health check
- `GET /dashboard` - Dashboard data
- `POST /notifications` - Create notification (triggers real-time update)

## WebSocket Events

- `connect` - Client connection
- `new_notification` - Real-time notification broadcast

## Best Practices Implemented

- **Security**: VPC isolation, IAM least privilege, encrypted database
- **Scalability**: Auto-scaling EKS nodes, Kubernetes replicas
- **Monitoring**: Ready for CloudWatch integration
- **Secrets**: Kubernetes secrets for sensitive data
- **CI/CD**: Automated testing and deployment

## Troubleshooting

### EKS Cluster Not Found
- Ensure Terraform has successfully created the cluster
- Check AWS region in GitHub Actions environment variables

### ECR Repository Issues
- Verify ECR repositories are created
- Check AWS credentials and permissions

### Database Connection
- Update `k8s/secrets.yml` with correct RDS endpoint
- Ensure security groups allow EKS to RDS communication

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push to GitHub (triggers CI/CD)
5. Create a pull request

## License

MIT License
