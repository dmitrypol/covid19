# prod setup

kubectl create secret generic covid19-secrets --from-env-file=devops/secrets.env

kubectl proxy

http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#!/login

