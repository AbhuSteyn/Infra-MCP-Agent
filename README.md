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
