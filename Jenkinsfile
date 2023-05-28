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
                sh 'cd /home/ubuntu/devops-experts/project/worldgames'
                sh 'sudo docker build -t my_score_image .'
            }
        }
        stage('Run') {
            steps {
                sh 'cd /home/ubuntu/devops-experts/project/worldgames'
                sh 'sudo docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                wrap([$class: 'Xvfb'])
                sh 'cd /home/ubuntu/devops-experts/project/worldgames'
                sh 'python3 e2e.py'
            }
        }
    }
}

