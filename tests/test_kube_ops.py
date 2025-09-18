import unittest
from unittest.mock import patch, MagicMock
from src.kube_ops import restart_pod, scale_deployment

class TestKubeOps(unittest.TestCase):

    @patch("src.kube_ops.client.CoreV1Api")
    def test_restart_pod(self, mock_core_v1):
        mock_api = MagicMock()
        mock_core_v1.return_value = mock_api

        result = restart_pod("default", "test-pod")
        mock_api.delete_namespaced_pod.assert_called_with(name="test-pod", namespace="default")
        self.assertEqual(result["status"], "Pod deleted")

    @patch("src.kube_ops.client.AppsV1Api")
    def test_scale_deployment(self, mock_apps_v1):
        mock_api = MagicMock()
        mock_apps_v1.return_value = mock_api

        result = scale_deployment("default", "web-api", 3)
        mock_api.patch_namespaced_deployment.assert_called()
        self.assertEqual(result["status"], "Deployment scaled to 3")

if __name__ == "__main__":
    unittest.main()
