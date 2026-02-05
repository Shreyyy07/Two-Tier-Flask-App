pipeline {
    agent any

    stages {

        stage('Clean old containers') {
            steps {
                sh '''
                docker-compose down || true
                '''
            }
        }

        stage('Build & Deploy') {
            steps {
                sh '''
                docker-compose up -d --build
                '''
            }
        }
    }
}
