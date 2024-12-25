from flask import Flask
from prometheus_client import generate_latest, Counter, Histogram, REGISTRY
import time

app = Flask(__name__)

REQUESTS = Counter('http_requests_total', 'Total number of HTTP requests')
LATENCY = Histogram('http_request_latency_seconds', 'Latency of HTTP requests')

@app.route('/')
@LATENCY.time()
def hello():
    REQUESTS.inc()
    time.sleep(2)  # Simulate some work
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)