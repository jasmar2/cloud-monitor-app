from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define a deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="monitor-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "monitor-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "monitor-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="monitor-app",
                        image="monitoringapp.azurecr.io/monitoring-app:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ],
                image_pull_secrets=[client.V1LocalObjectReference(name="access-key-acr")]
            )
        )
    )
)

# Create deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define a service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="monitor-app"),
    spec=client.V1ServiceSpec(
        selector={"app": "monitor-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create a service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)
