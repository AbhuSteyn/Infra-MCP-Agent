from kubernetes import client, config
import base64
import yaml

# Load Kubernetes config inside cluster
config.load_incluster_config()

def restart_pod(namespace, pod_name):
    v1 = client.CoreV1Api()
    v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
    return {"status": "Pod deleted"}

def scale_deployment(namespace, name, replicas):
    apps_v1 = client.AppsV1Api()
    body = {"spec": {"replicas": replicas}}
    apps_v1.patch_namespaced_deployment(name, namespace, body)
    return {"status": f"Deployment scaled to {replicas}"}

def get_status(namespace, name):
    v1 = client.CoreV1Api()
    pod = v1.read_namespaced_pod(name=name, namespace=namespace)
    return {"status": pod.status.phase}

def apply_manifest(encoded_manifest):
    decoded = base64.b64decode(encoded_manifest).decode("utf-8")
    manifest = yaml.safe_load(decoded)
    k8s_client = client.ApiClient()
    client.utils.create_from_yaml(k8s_client, yaml_objects=[manifest])
    return {"status": "Manifest applied"}
