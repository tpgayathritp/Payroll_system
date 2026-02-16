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
                    url: 'https://github.com/tpgayathritp/Payroll_system.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKERHUB_USER%/%IMAGE_NAME%:%BUILD_NUMBER% ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                                 usernameVariable: 'USER',
                                                 passwordVariable: 'PASS')]) {
                    bat """
                    echo %PASS% | docker login -u %USER% --password-stdin
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                bat "docker push %DOCKERHUB_USER%/%IMAGE_NAME%:%BUILD_NUMBER%"
                bat "docker tag %DOCKERHUB_USER%/%IMAGE_NAME%:%BUILD_NUMBER% %DOCKERHUB_USER%/%IMAGE_NAME%:latest"
                bat "docker push %DOCKERHUB_USER%/%IMAGE_NAME%:latest"
            }
        }

        stage('Deploy to Server') {
    steps {
        dir('D:\\Python\\Payroll_app_Docker') {
            bat "docker compose down --remove-orphans"
            bat "docker build -t payroll_api ."
            bat "docker compose up -d --force-recreate"
           }
       }
     }


        stage('Health Check') {
    steps {
        powershell "Start-Sleep -Seconds 5"
        bat "curl -f http://localhost:8000/docs"
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
