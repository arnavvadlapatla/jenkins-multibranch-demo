pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:/Applications/Docker.app/Contents/Resources/bin:${env.PATH}"
    }

    stages {
        stage('Branch Info') {
            steps {
                echo "Running pipeline for branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest -v'
            }
        }

        stage('Deploy to Dev') {
            when {
                branch pattern: 'feature/*', comparator: 'GLOB'
            }
            steps {
                echo "Deploying ${env.BRANCH_NAME} to DEV environment..."
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying to PRODUCTION..."
            }
        }
    }

    post {
        success { echo "Pipeline succeeded for ${env.BRANCH_NAME}" }
        failure { echo "Pipeline failed for ${env.BRANCH_NAME}" }
    }
}