pipeline {
    agent any

    stages {
        stage('Build Backend') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                dir('backend') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test Backend') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                dir('backend') {
                    sh 'python -m pytest'  // Assuming tests exist, add if needed
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t school-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
