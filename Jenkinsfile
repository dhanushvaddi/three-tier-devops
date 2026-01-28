pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/dhanushvaddi/three-tier-devops.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                echo "SonarQube scan will be added here"
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t backend:latest backend/'
            }
        }

        stage('Trivy Scan') {
            steps {
                sh 'trivy image backend:latest'
            }
        }
    }
}
