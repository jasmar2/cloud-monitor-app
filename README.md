# Cloud Native Monitoring App

This is my first devops project in which, I mainly have learned working Azure Services (Azure Container Registry and Azure Kubernetes Service), deploying Kubernetes with Python client and creating Flask application.

## Steps taken to deploy full application

- Created basic Flask application and used psutil library
- Deployed application locally, to se if everything works fine
- Created Dockerfile, that simply install all of the dependencies and expose a chosen port, and runs command that will make the application accessible
- Deployed created image to the DockerHub, then pulled image locally to see if container from repository is working correctly

- Created an Azure Container Registry resource

  - Firstly, I logged in to my container registry. If problems persists, then go to the Access Key tab, and see if "Admin User" is checked. It will show the username and generated passwords needed to log in to the registry.

  ```
  docker login <container_registry_name>.azurecr.io
  ```

  - Then, push our locally pulled image from DockerHub into the container registry

  ```
  docker tag <name_local_docker_image> <container_registry_name>.azurecr.io/<repository_name>
  docker push <container_registry_name>.azurecr.io/<repository_name>
  ```

  - To test if everything is working pull the image from Azure Container Registry

  ```
  docker pull <container_registry_name>.azurecr.io/<repository_name>
  ```

- Created Azure Kubernetes Service resource

  - Connecting to the cluster:

  ```
  az aks get-credentials --resource-group <resource-group> --name <aks_cluster_name>
  ```

  - Apply the created manifest, it will connect with aks cluster
  - I've got problem with pulling the image from Azure Container Registry to the cluster, but documentation has helped me out
    [https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/cannot-pull-image-from-acr-to-aks-cluster]

- Lastly, making port-forwarding for our created service.

```
kubectl port-forward svc/<svc_name> 5000:5000
```

Interacting with Azure Services was very fun and I tried to only use official documentation and it paid.
