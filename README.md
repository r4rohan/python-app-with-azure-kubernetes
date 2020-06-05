# python-app-with-azure-kubernetes
A demo python application used in blog Application Deployment on Azure Kubernetes Services.

This repo is used in the Medium blog [Application Deployment with Azure Kubernetes Service and Azure Pipelines](https://medium.com/faun/application-deployment-with-azure-kubernetes-service-and-azure-pipelines-a0bf43916746)

### Steps

**Create a resource group in Azure Subscription**
az group create -l southcentralus -n cloudorbit-resource-grp --subscription pay-as-you-go

**Create Azure k8s cluster**
az aks create -g cloudorbit-resource-grp -n cloudobrit-cluster --node-vm-size Standard_B2s --node-count 2 --generate-ssh-keys

**Create Azure Container Registry**
az acr create -g cloudorbit-resource-grp -n cloudorbit --sku Standard

**Create Azure Pipelines**
Follow the steps in the blog to create and setup Azure Pipeline via Azure DevOps console

Once all done, we need to check the running pod, services and horizontal pod autoscaler

**Authenticate your k8s cluster with cloud-shell**
az aks get-credentials -g cloudorbit-resource-grp -n cloudobrit-cluster

**Get deployments**
kubectl -n dev get deployments

**Get pods**
kubectl -n dev get pods

**Get servics**
kubectl -n dev get svc

**Get Horizontal Pod Autoscaler**
kubectl -n dev get hpa

**To check the app**
curl http://[external-ip]:5000

**To describe pods specification and check logs**
kubectl -n dev describe pods [pod-name]
kubectl -n dev logs [pod-name]

We can scale our deployment manually as well as automatically. For automatic scaling, we have defined HPA in YAML which increases one replica of pod whenever the average traffic on the running pod goes beyond 80%. It will increase replica up to the max number we defined in YAML manifest that’s 3 in our case.

**To manual scale**
kubectl -n dev scale deployment python-app --replicas=3
kubectl -n dev get deployment python-app

**For interactive UI console of k8s cluster**
az aks browse -g cloudorbit-resource-grp -n cloudorbit-cluster

**For entering into pods***
kubectl -n dev exec -it [pod-name] -- /bin/bash
