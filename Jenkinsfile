pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'tpgayathritp'
        IMAGE_NAME = 'payroll_api'
    }

    stages {

     stage('Checkout') {
    steps {
        git branch: 'main',
            url: 'https://github.com/tpgayathritp/python-payroll-system.git',
            credentialsId: 'github-creds'
        }
      }


        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                                 usernameVariable: 'USER',
                                                 passwordVariable: 'PASS')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    sh "docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}"
                    sh "docker tag ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKERHUB_USER}/${IMAGE_NAME}:latest"
                    sh "docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                script {
                    sh "docker compose down"
                    sh "docker compose pull"
                    sh "docker compose up -d"
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    sh "sleep 5"
                    sh "curl -f http://localhost:8000/docs"
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed. Check logs."
        }
    }
}
