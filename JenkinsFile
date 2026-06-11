pipeline {
    agent any // Make sure this runs on your Windows node/agent

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies from requirements.txt...'
                // Using 'bat' for Windows, and 'python -m pip' to avoid PATH quirks
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Execute Tests') {
            steps {
                echo 'Running Pytest against C++ executable on Windows...'
                bat 'python -m pytest test_solution.py --junitxml=test-reports/results.xml'
            }
        }
    }

    post {
        always {
            echo 'Processing test results...'
            junit 'test-reports/results.xml'
        }
    }
}