#!/bin/bash

echo "Create the kind cluster..."
kind create cluster --config cluster.yml

kind load docker-image ghcr.io/onlydole/pytorch-keynote-2024/symphony:latest

echo "Applying the Kubernets manifests..."
kubectl apply -f kubernetes/deployment.yml
kubectl apply -f kubernetes/service.yml

# Wait for the pod starting with "keynote" to be running
while [[ $(kubectl get pods --no-headers | grep 'symphony' | awk '{print $3}') != "Running" ]]; do
  echo "Keynote demo is starting, make some noise..."
  sleep 10
done

echo "Forwarding the Keynote pod..."
kubectl port-forward svc/symphony 8080:8080 &

echo "Keynote demo is running, it's time to present! Open your browser to http://localhost:8080"