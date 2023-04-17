
                withCredentials([usernamePassword(credentialsId: "$DOCKER_REGISTRY_CREDENTIALS", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "docker login $DOCKER_REGISTRY -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    sh "docker push $DOCKER_REGISTRY/$DOCKER_USER/$DOCKER_IMAGE_NAME"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                sh "docker run -d --name $DOCKER_IMAGE_NAME -p 80:80