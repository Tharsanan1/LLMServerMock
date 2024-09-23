docker build -t llm-backend .

kscaledown -n apk-integration-test employee-service-deployment

watch -n 1 minikube image rm flask-hello-app && minikube image load flask-hello-app && kscaleup -n apk employee-service-deployment

docker tag llm-backend:latest tharsanan/llm-backend:latest

docker push tharsanan/llm-backend:latest

