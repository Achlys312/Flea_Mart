import requests
import time
from prometheus_client import start_http_server, Gauge

# Define Prometheus metrics
http_requests_total = Gauge('http_requests_total', 'Total HTTP requests.')
http_request_duration_seconds = Gauge('http_request_duration_seconds', 'HTTP request duration in seconds.')

# Define endpoint for Django app metrics
metrics_url = 'http://52.152.160.179/:8000/metrics'

def collect_metrics():
    response = requests.get(metrics_url)
    if response.status_code == 200:
        metrics_data = response.content.decode('utf-8')
            # Parse metrics data and update Prometheus metrics
        for line in metrics_data.split('\n'):
            if line.startswith('#'):
                continue
            fields = line.split(' ')
            if fields[0] == 'http_requests_total':
                http_requests_total.set(float(fields[1]))
            elif fields[0] == 'http_request_duration_seconds':
                http_request_duration_seconds.set(float(fields[1]))

if __name__ == '__main__':
    # Start Prometheus server
    start_http_server(8001)

    # Collect metrics from Django app every 10 seconds
    while True:
        collect_metrics()
        time.sleep(10)
