pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'tomcat:latest'
        DOCKER_REGISTRY = 'docker.io'
        REPO_URL = 'https://github.com/sivacloudops59/devops.git'
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
        withCredentials([usernamePassword(credentialsId: 'docker-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
            sh """
            # Log in to Docker Hub
            echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin

            # Tag the Docker image
            docker tag ${DOCKER_IMAGE} ${DOCKER_REGISTRY}/\$DOCKER_USERNAME/${DOCKER_IMAGE}

            # Push the Docker image to Docker Hub
            docker push ${DOCKER_REGISTRY}/\$DOCKER_USERNAME/${DOCKER_IMAGE}
            """
        }
    }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh """
                docker pull ${DOCKER_REGISTRY}/username/${DOCKER_IMAGE}
                docker run -d --name my-app -p 8143:8143 ${DOCKER_REGISTRY}/username/${DOCKER_IMAGE}
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
