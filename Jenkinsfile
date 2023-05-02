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
                sh 'docker run -d --name $DOCKER_IMAGE_NAME -p 8000:8000 $DOCKER_REGISTRY/$DOCKER_USER/$DOCKER_IMAGE_NAME'
            }
        }

        stage('Monitor') {
            steps {
                // Install Prometheus and Prometheus Flask Exporter
                sh 'apt-get update && apt-get install -y curl'
                sh 'curl -LO "https://github.com/prometheus/prometheus/releases/download/v2.32.0/prometheus-2.32.0.linux-amd64.tar.gz"'
                sh 'tar -xzf prometheus-2.32.0.linux-amd64.tar.gz'
                sh 'rm prometheus-2.32.0.linux-amd64.tar.gz'
                sh 'cd prometheus-2.32.0.linux-amd64 && ./prometheus &'
                sh 'pip install prometheus-flask-exporter'

                // Start the Prometheus server
                sh 'docker run -d --name prometheus -p 9091:9091 prom/prometheus'

                // Expose metrics from the Django app using a Prometheus client
                sh 'python prometheus.py &'

                // Add the Django app to Prometheus configuration
                // sh 'mkdir -p /etc/prometheus'
                sh 'echo "  - targets: [\'http://52.152.160.179:8000\']" >> prometheus-2.32.0.linux-amd64/prometheus.yml'
                sh 'cd prometheus-2.32.0.linux-amd64 && ./prometheus &'
                // Verify that Prometheus is scraping metrics from the Django app
                sh 'curl localhost:9090/metrics | grep django_http_requests_total'
            }
        }

    }
}