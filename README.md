# Weather_app_project_eks

## Pipeline Architecture Overview
![alt text](CI:CD-Pipeline.png)

## Description
This project implements a robust CI/CD pipeline for a simple Weather application. Leveraging the power of GitHub Actions and Snyk, the pipeline is divided into two stages, providing seamless integration and deployment processes.

## Pipelines Overview
### 1. Pull Request Pipeline:
Triggered upon the creation of a pull request, this pipeline employs Snyk to conduct comprehensive testing of both the project source code and Docker image. This ensures that potential vulnerabilities are identified and addressed before merging changes into the main branch.

### 2. Merge Pipeline:
Triggered upon the successful merge of a pull request, this pipeline orchestrates the deployment process. It pushes the Docker image to Docker Hub, ensuring its availability for deployment. Also, the pipeline updates the Helm repository with the new Docker image tag (https://github.com/OfekMalul/helm_charts/tree/main/CreatedByMe/weather_app_chart). This guarantees that the latest changes are seamlessly integrated into the deployment environment. The deployment of the helm chart is being taken care of by ArgoCD.

