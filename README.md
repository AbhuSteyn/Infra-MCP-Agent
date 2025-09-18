# infra-mcp-agent 🚀  
A Minimal Control Plane (MCP) server and client for Kubernetes infrastructure automation. Built with Python and FastAPI, designed for secure, structured task execution inside AKS or any Kubernetes cluster.

---

## 🧠 Why This Project Exists

Modern infrastructure teams often need lightweight, secure ways to expose internal operations—like scaling deployments or restarting pods—to automation tools, AI agents, or internal dashboards. This project solves that by providing:

- ✅ A FastAPI-based MCP server that receives structured JSON tasks
- ✅ A Python client to send tasks securely
- ✅ Token-based authentication
- ✅ Kubernetes-native operations using the official Python client

Whether you're building internal tooling, integrating with LLMs, or automating DevOps workflows, `infra-mcp-agent` gives you a clean, extensible control interface.

---

## 📦 Features

| Feature               | Description                                  |
|-----------------------|----------------------------------------------|
| `scale_deployment`    | Change replica count of a deployment         |
| `restart_pod`         | Delete a pod to trigger restart              |
| `get_status`          | Return pod or deployment status              |
| `apply_manifest`      | Apply base64-encoded Kubernetes YAML manifest |
| 🔐 Authentication     | Token-based via `Authorization: Bearer <token>` |
| 🐳 Containerized       | Runs as a pod in AKS or any Kubernetes cluster |

---

## 🧱 Architecture

```
Client → API Gateway → MCP Server → Kubernetes API
```

- **MCP Server**: FastAPI app that receives and routes tasks
- **MCP Client**: Python CLI or SDK that sends tasks
- **Auth**: Token-based (stored in Kubernetes Secret or Azure Key Vault)
- **Kubernetes Integration**: Uses `kubernetes` Python SDK

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/infra-mcp-agent.git
cd infra-mcp-agent
```

### 2. Build and Push Docker Image
```bash
docker build -t yourusername/infra-mcp-agent:latest .
docker push yourusername/infra-mcp-agent:latest
```

### 3. Deploy to AKS
```bash
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
```

> 💡 Make sure to create a Kubernetes Secret named `mcp-secret` with your token:
```bash
kubectl create secret generic mcp-secret --from-literal=token=your-secure-token
```

---

## 🧪 Using the MCP Client

```python
from src.client import send_task

task = {
  "task": "scale_deployment",
  "namespace": "default",
  "deployment_name": "web-api",
  "replicas": 3
}

response = send_task(task, token="your-token")
print(response)
```

---

## 🔧 Example Task Payloads

### ✅ Restart a Pod
```json
{
  "task": "restart_pod",
  "namespace": "default",
  "pod_name": "my-app-pod"
}
```

### 📈 Scale a Deployment
```json
{
  "task": "scale_deployment",
  "namespace": "default",
  "deployment_name": "web-api",
  "replicas": 5
}
```

### 📦 Apply a Manifest
```json
{
  "task": "apply_manifest",
  "manifest": "<base64-encoded-yaml>"
}
```

---

## 🧪 Testing

Run unit tests with mocks:
```bash
python -m unittest tests/test_kube_ops.py
```

---

## 🔐 Security Notes

- All requests must include a valid bearer token
- Token is verified against an environment variable (`MCP_AUTH_TOKEN`)
- Recommended: Store token in Azure Key Vault or Kubernetes Secrets
- Optional: Extend to support mTLS or OAuth2

---

## 📚 Extending the Project

You can easily add new tasks by:
1. Defining a new function in `kube_ops.py`
2. Adding a route in `task_router.py`
3. Updating your client payload

---

## 📄 License

MIT License. Feel free to fork, extend, and contribute.

---


---

Would you like help writing a GitHub Actions workflow to automate testing and Docker builds? Or maybe a sample Helm chart to deploy this more cleanly in AKS?
