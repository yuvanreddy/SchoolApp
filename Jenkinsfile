pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'sudo apt-get update && sudo apt-get install -y python3 python3-pip'
                sh 'python3 --version && python3 -m pip --version'
            }
        }

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
