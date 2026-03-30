pipeline {
    agent any

    stages {
        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test Backend') {
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
