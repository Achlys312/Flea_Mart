pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "flea_mart-app"
        DOCKER_USER = "kartikdhoundiyal"
        DOCKERFILE_PATH = "./Dockerfile"
        DOCKER_REGISTRY = "docker.io"
        DOCKER_REGISTRY_CREDENTIALS = "docker_cred"
        PROMETHEUS_PORT = 9090
    }

    stages {
        stage('Test') {
            steps {
             // Build the Docker image
                sh 'docker build -t my-django-app-test . -f Dockerfile.test'
        
             // Run the tests inside a Docker container.
                //sh 'docker run --rm -p 8000:8000 my-django-app-test '
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -f $DOCKERFILE_PATH -t $DOCKER_REGISTRY/$DOCKER_USER/$DOCKER_IMAGE_NAME .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: "$DOCKER_REGISTRY_CREDENTIALS", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login $DOCKER_REGISTRY -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker push $DOCKER_REGISTRY/$DOCKER_USER/$DOCKER_IMAGE_NAME'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker run -d --name $DOCKER_IMAGE_NAME -p 8000:8000 $DOCKER_REGISTRY/$DOCKER_USER/$DOCKER_IMAGE_NAME' -e PROMETHEUS_MULTIPROC_DIR=/prometheus -v /prometheus:/prometheus my-django-app'
            }
        }

        stage('Monitor') {
            steps {
                // Install Prometheus exporters and Python dependencies.
                sh 'pip install prometheus_client'
                sh 'pip install requests'

                // Start the Prometheus server
                sh 'docker run -d --name prometheus -p 9090:9090 prom/prometheus'

                // Start the Grafana server
                sh 'docker run -d --name grafana -p 3000:3000 grafana/grafana'

                // Restart Prometheus to pick up the new configuration
                sh 'docker restart prometheus'

                // Configure Grafana to use Prometheus as a data source
                sh 'curl -X POST -H "Content-Type: application/json" -d \'{"name":"prometheus","type":"prometheus","url":"http://prometheus:9090","access":"proxy","isDefault":true}\' http://admin:admin@localhost:3000/api/datasources'
            }
        }

    }
}
