#!/bin/bash
docker-compose build python && docker tag covid19_python iad.ocir.io/bmcdw/covid19_python && docker push iad.ocir.io/bmcdw/covid19_python
kubectl apply -f devops/oke/
kubectl rollout restart deployment.apps/covid19-deployment