### Project Structure
```
repo-name/
├── .dockerignore
├── .gitignore
├── CHANGELOG
├── CODEOWNERS
├── CONTRIBUTING
├── Dockerfile
├── LICENSE
├── README.md
├── RELEASE_NOTES.md
├── app
│   ├── __init__.py
│   ├── app.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── v1
│   │   │       ├── __init__.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   └── utils
│   │       └── __init__.py
│   ├── rag
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── v1
│   │   │       ├── __init__.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   └── utils
│   │       └── __init__.py
│   ├── database
│   │   └── __init__.py
│   ├── logger
│   │   └── __init__.py
│   ├── main.py
│   ├── middleware
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── schemas
│   │   └── __init__.py
│   └── settings
│       ├── __init__.py
│       └── config.py
├── docker-compose.yml
├── docs
├── gitlab-ci.yml
├── k8s
│   └── manifests
│       ├── app-deployment.yaml
│       └── app-service.yaml
├── requirements.txt
└── tests
    └── __init__.py

```


# RAG Deployment with GitLab CI/CD and Docker

This repository (RAG) contains the steps and configurations to deploy a **FastAPI** application using **GitLab CI/CD** and **Docker**. The deployment process is fully automated, allowing you to continuously deploy your FastAPI app to a remote server every time you push code to the `main` branch.

## Prerequisites

1. **GitLab Repository**: The FastAPI application is hosted on a GitLab repository.
2. **Server Setup**: A server is set up for deployment, and you have SSH access to it.
3. **Docker**: Docker is used to containerize the FastAPI application for consistent deployment.
4. **GitLab CI/CD Runner**: You must have access to GitLab's CI/CD runner to execute pipeline jobs.
5. **SSH Key**: SSH access to your server is required for deployment. You will need to set up SSH keys for secure communication.


## Additional Considerations
Reverse Proxy (Nginx): In production, you should consider setting up a reverse proxy (e.g., Nginx) to serve your FastAPI app over HTTPS and forward traffic to the Docker container.

SSL Certificates: For secure HTTPS access, you can use a service like Let’s Encrypt to generate free SSL certificates.

Environment Variables: Store sensitive information like database credentials and API keys in GitLab CI/CD environment variables and inject them into your application at runtime.

Monitoring & Logging: In a production environment, consider setting up monitoring (e.g., Prometheus) and logging (e.g., ELK stack) for your FastAPI app.


## STEPS FOR CI (Continuous Integration)

1. Install gitlab binary in the system to make a runner, that runner will be assigned to the repo (available for the repo). (Runner is config with some tags based on the architecture and we define the runner with the executors like docker, shell, etc).
2. If we want to set a rule on multiple applications, then we can create a Kubernetes cluster as well to handle all applications through K8(assign node from cluster).

3. Now, in the repo root folder, make a gitlab-ci.yaml which will have tags, default, variables, rules, stages etc.
we need to define the job and stages, where each stage will jobs in sequence and we can define which job belongs to which scene.
Also, in this yaml, we can set the params on parent level which will be applicable to all the stages and job or we can set it per job as well.
Once all the jobs are triggered, we will push the image to an artifact, preferably cloud artifact. We need to pass th token or other mode of authorization to access the cloud artifact to push the image.

## STEPS FOR CD (Continuous Deployment)
4. In the repo, we can make folder like - 
├── K8s
│   ├── manifest
│       ├── s1
│           ├── service.yaml
│           ├── deployment.yaml

If we setup the CD part with, let's say Argo CD, then we need to pass the manifest path where it will refer the service.yaml and deployment.yaml to update the image tag (generated by the last job to push in the artifact).
We can set the time limit for the polling. It will check if the image tag is updated, if yes, then it will trigger the deployment by updating the same in the yaml.
Alternatively, we can use the  webhook  to trigger the pipeline based on any change.