pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vivinmathew26-byte/chatbot-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-chatbot:latest .'
            }
        }
        stage('Load Image to Minikube') {
            steps {
                sh '/usr/local/bin/minikube image load flask-chatbot:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh '/usr/local/bin/kubectl apply -f deployment.yml'
                sh '/usr/local/bin/kubectl rollout restart deployment flask-chatbot-deployment'
            }
        }
        stage('Verify') {
            steps {
                sh '/usr/local/bin/kubectl get pods'
                sh '/usr/local/bin/kubectl get svc'
            }
        }
        stage('Expose App') {
            steps {
                sh 'pkill -f "kubectl port-forward" || true'
                sh 'nohup /usr/local/bin/kubectl port-forward svc/flask-chatbot-service 8081:80 --address=0.0.0.0 &'
            }
        }
    }
}
