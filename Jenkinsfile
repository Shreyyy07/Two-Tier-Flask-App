pipeline {
    agent any

    stages {
        stage('Clean old containers') {
            steps {
                bat 'docker compose down --remove-orphans || exit 0'
            }
        }

        stage('Build & Deploy') {
            steps {
                bat 'docker compose up -d --build'
            }
        }
    }
}
