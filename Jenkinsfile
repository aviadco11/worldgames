pipeline {
    agent any
    
    environment {
      DOCKERHUB_CREDENTIALS= credentials('dockerhub')	
    }
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
                sh 'sudo rm -rf /tmp/ -R'
                sh 'pip install --disable-pip-version-check -r requirements.txt'
                wrap([$class: 'Xvfb']) {
                sh 'python3 e2e.py'
                }
            }
        }
        stage('Finalize') {
            steps {
	      sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
              sh 'sudo docker tag my_score_image fdsfsrw12/my_score_image'
	      sh 'sudo docker push fdsfsrw12/my_score_image'
	    }
	}
    }
}

