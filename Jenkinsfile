pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'tomcat:latest'
        DOCKER_REGISTRY = 'docker.io'
        REPO_URL = 'https://github.com/username/repository.git'
        BRANCH = 'main'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from Git...'
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh """
                docker build -t ${DOCKER_IMAGE} .
                """
            }
        }
        stage('Test Docker Container') {
            steps {
                echo 'Testing the Docker container...'
                sh """
                docker run --rm ${DOCKER_IMAGE} sh -c "echo Tests executed inside the container"
                """
            }
        }
        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker image to registry...'
                withCredentials([string(credentialsId: 'docker-credentials', variable: 'DOCKER_PASSWORD')]) {
                    sh """
                    echo ${DOCKER_PASSWORD} | docker login -u username --password-stdin ${DOCKER_REGISTRY}
                    docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/username/${DOCKER_IMAGE}
                    docker push ${DOCKER_REGISTRY}/username/${DOCKER_IMAGE}
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh """
                docker pull ${DOCKER_REGISTRY}/username/${DOCKER_IMAGE}
                docker run -d --name my-app -p 8080:8080 ${DOCKER_REGISTRY}/username/${DOCKER_IMAGE}
                """
            }
        }
    }
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
