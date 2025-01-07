pipeline {
    agent {
        docker { image 'docker:latest' }
    }
    stages {
        stage('Test Docker') {
            steps {
                sh 'docker --version'
            }
        }
    }
}
