#!/bin/bash
docker-compose build python && docker tag covid19_python iad.ocir.io/bmcdw/covid19_python && docker push iad.ocir.io/bmcdw/covid19_python
docker-compose build worker && docker tag covid19_worker iad.ocir.io/bmcdw/covid19_worker && docker push iad.ocir.io/bmcdw/covid19_worker
docker-compose build scheduler && docker tag covid19_scheduler iad.ocir.io/bmcdw/covid19_scheduler && docker push iad.ocir.io/bmcdw/covid19_scheduler
kubectl apply -f devops/oke/
kubectl rollout restart deployment.apps/covid19-deployment
kubectl rollout restart deployment.apps/covid19-worker-deployment
kubectl rollout restart deployment.apps/covid19-scheduler-deployment