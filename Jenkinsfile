pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/satpaljangir22/go-rest-api-automation.git']])
            }
        }
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }    
        stage('Run Tests') {
            steps {
                bat 'behavex features'
            }
        }
    }
}
