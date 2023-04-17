pipeline {
    agent any

    environment {
        PROMETHEUS_PORT = 9090
    }

    
  stages {
        
        stage('Checkout') {
            steps {
                git 'https://github.com/Garv312/Flea_Mart.git'
            }
        }

        stage('Install dependencies') {
            steps {
                // Install Python and pipenv
                sh 'apt-get update && apt-get install -y python3 python3-pip'
                sh 'pip3 install pipenv'
                
                // Install your Django project's dependencies
                sh 'pipenv install --dev'
            }
        }

        stage('Test') {
            steps {
        
                sh 'pipenv run python manage.py test'
            }
        }
        
        stage('Build') {
            steps {
                /*sh 'pip install -r requirements.txt'*/
                sh 'pipenv run python manage.py collectstatic'
                sh 'pipenv run python manage.py compress'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker build -t your-image-name .'
                sh 'docker tag your-image-name your-registry/your-image-name'
                withCredentials([usernamePassword(credentialsId: 'your-registry-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD your-registry'
                    sh 'docker push your-registry/your-image-name'
                }
            }
        }
        
        stage('Monitor') {
            steps {
                sh 'pip install prometheus-flask-exporter'
                sh 'pip install prometheus_client'
                sh 'echo "from prometheus_flask_exporter import PrometheusMetrics\nmetrics = PrometheusMetrics(app=None)\nmetrics.start_http_server(5001)" >> app.py'
                sh 'docker run -d -p 9090:9090 prom/prometheus'
                sh 'docker run -d -p 5001:5001 your-registry/your-image-name python app.py'
            }
        }
    }
}