import requests

def send_task(task: dict, token: str):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post("http://mcp-server.default.svc.cluster.local/task", json=task, headers=headers)
    return res.json()
