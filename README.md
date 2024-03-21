# Weather_app_project_eks

## Pipeline Architecture Overview
![CI-CD pipeline](CI:CD-Pipeline.png)

## Description
This project implements a robust CI/CD pipeline for a simple Weather application. Leveraging the power of GitHub Actions and Snyk, the pipeline is divided into two stages, providing seamless integration and deployment processes. It is valuable to mention that this Github Repository takes part as one of three repositories that are being utilized for this project.

### Terraform Repository
The Terraform repository contains required infrastructure to create the EKS cluster that will host the weather application. 
To view the repository please view this link: https://github.com/OfekMalul/terraform_eks 

### Helm Repository
The Helm repository is utilize as gitops for ArgoCD. ArgoCD is deployed in the EKS cluster and continously follow on changes taken place to the weather_app helm chart. If changes occured ArgoCD will manage the deployment of it. 
To view the repository please view this link: https://github.com/OfekMalul/helm_charts/tree/main/CreatedByMe/weather_app_chart

## Pipelines Overview
### 1. Pull Request Pipeline:
Triggered upon the creation of a pull request, this pipeline employs Snyk to conduct comprehensive testing of both the project source code and Docker image. This ensures that potential vulnerabilities are identified and addressed before merging changes into the main branch.

### 2. Merge Pipeline:
Triggered upon the successful merge of a pull request, this pipeline orchestrates the deployment process. It pushes the Docker image to Docker Hub, ensuring its availability for deployment. Also, the pipeline updates the Helm repository with the new Docker image tag (https://github.com/OfekMalul/helm_charts/tree/main/CreatedByMe/weather_app_chart). This guarantees that the latest changes are seamlessly integrated into the deployment environment. The deployment of the helm chart is being taken care of by ArgoCD.

## Setup Instructions


