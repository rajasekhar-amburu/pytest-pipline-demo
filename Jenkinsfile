pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/rajasekhar-amburu/pytest-pipline-demo.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/rajasekhar-amburu/pytest-pipline-demo.git'
                sh 'python3 calculations.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}