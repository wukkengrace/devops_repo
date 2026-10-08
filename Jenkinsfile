pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'your_dockerhub_username/reactive-flask-app:latest'
        CONTAINER_NAME = 'flask_prod'
    }
    stages {
        stage('Pull Image') {
            steps {
                sh "docker pull ${DOCKER_IMAGE}"
            }
        }
        stage('Deploy Container') {
            steps {
                script {
                    // Stop and remove existing container if it exists
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    // Run the new container mapping port 5000 to local 8080
                    sh "docker run -d --name ${CONTAINER_NAME} -p 8080:5000 ${DOCKER_IMAGE}"
                }
            }
        }
        stage('Verify Deployment') {
            steps {
                // Wait for the container to spin up, then test the health endpoint
                sleep 5
                sh "curl -f http://localhost:8080/api/health"
            }
        }
    }
}