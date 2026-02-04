pipeline {
    agent any

    stages {
        stage('Build & Deploy') {
            steps {
                bat 'docker compose down || exit 0'
                bat 'docker compose up -d --build'
            }
        }
    }
}
