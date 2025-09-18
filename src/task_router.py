from src.kube_ops import restart_pod, scale_deployment, get_status, apply_manifest

def route_task(payload: dict):
    task = payload.get("task")
    if task == "restart_pod":
        return restart_pod(payload["namespace"], payload["pod_name"])
    elif task == "scale_deployment":
        return scale_deployment(payload["namespace"], payload["deployment_name"], payload["replicas"])
    elif task == "get_status":
        return get_status(payload["namespace"], payload["name"])
    elif task == "apply_manifest":
        return apply_manifest(payload["manifest"])
    else:
        return {"error": "Unknown task"}
