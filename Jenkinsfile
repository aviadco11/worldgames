pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aviadco11/worldgames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'sudo docker build -t my_score_image .'
            }
        }
        stage('Run') {
            steps {
                sh 'sudo docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'sudo rm -rf /tmp/.X1 -R'
                sh 'sudo rm -rf /tmp/.X11-unix/X1 -R'
                sh 'pip install --disable-pip-version-check -r requirements.txt'
                wrap([$class: 'Xvfb']) {
                sh 'python3 e2e.py'
                }
            }
        }
    }
}

