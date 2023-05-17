pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh "git clone https://github.com/avi061077/world-of-games.git"
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t world-of-games:latest"
            }
        }
        stage('Run') {
            steps {
                sh "cd world-of-games"
                sh "docker run -it world-of-games:latest"
            }
        }
        stage('Test') {
            steps {
                sh "cd world-of-games"
                sh "python3 e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                sh "docker stop worldofgames:latest"
            }
        }
    }
}