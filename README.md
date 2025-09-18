# infra-mcp-agent 🚀

A minimal control plane (MCP) server and client for Kubernetes infrastructure tasks. Built with FastAPI and Python, designed for AKS clusters.

## Features
- Scale deployments
- Restart pods
- Apply manifests
- Query pod/deployment status
- Token-based authentication
- FastAPI server + Python client

## Usage

### 1. Deploy to AKS
```bash
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
2. Send a Task
python
from src.client import send_task

task = {
  "task": "scale_deployment",
  "namespace": "default",
  "deployment_name": "web-api",
  "replicas": 3
}

response = send_task(task, token="your-token")
print(response)
3. Supported Tasks
Task	Description
scale_deployment	Change replica count of a deployment
restart_pod	Delete a pod to trigger restart
get_status	Return pod/deployment status
apply_manifest	Apply base64-encoded YAML manifest
Security
Token-based auth via Authorization: Bearer <token>

Token stored in Kubernetes Secret or Azure Key Vault

Deployment
Containerized with Docker

Runs as a pod in AKS

Exposed via ClusterIP or API Gateway

License
MIT
