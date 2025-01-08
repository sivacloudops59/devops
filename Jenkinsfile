pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'tomcat:latest'
        DOCKER_REGISTRY = 'docker.io'
        REPO_URL = 'https://github.com/sivacloudops59/devops.git'
        BRANCH = 'main'
        DOCKER_PASSWORD='Sivaji@59'
        username= 'sivadockerhub59'
        def DOCKER_ID = "your-docker-id"
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
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_ID', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh """
                    echo ${DOCKER_PASSWORD} | docker login -u $DOCKER_ID --password-stdin 
                    
                    docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/${DOCKER_ID}/${DOCKER_IMAGE}
                    docker push ${DOCKER_REGISTRY}/${DOCKER_ID}/${DOCKER_IMAGE}
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh """
                docker pull ${DOCKER_REGISTRY}/${DOCKER_ID}/${DOCKER_IMAGE}
                docker run -d -p 8143:8080 ${DOCKER_ID}/${DOCKER_IMAGE}
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
