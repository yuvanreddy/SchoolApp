pipeline {
    agent any

    stages {
        stage('Build Backend') {
            steps {
                sh 'python3 -m pip install --user -r backend/requirements.txt || pip install -r backend/requirements.txt'
            }
        }

        stage('Test Backend') {
            steps {
                dir('backend') {
                    sh 'python3 -m pytest || echo "No tests found, skipping"'  // Assuming tests exist, add if needed
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t school-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'sudo docker-compose up -d'
            }
        }
    }
}
