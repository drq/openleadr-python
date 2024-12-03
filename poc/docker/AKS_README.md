# OpenADR POC

## Local

1. Install Docker locally.
2. Build and run the containers locally using the docker compose.

## AKS

### Setup 

1. Install Docker locally.
2. Install Azure CLI.
3. Setup Azure Container Registry (ACR) through portal or CLI.
4. Setup AKS Cluster through portal or CLI.
5. Setup Azure Application Gateway through portal.
6. Build local images and tag the images with corresponding ACR URI.
7. Deploy local images to AKS.
8. Validate container logs in AKS.