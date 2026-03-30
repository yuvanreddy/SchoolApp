pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t school-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }

        stage('Test API') {
            steps {
                sh 'curl http://localhost:5000'
            }
        }
    }
}