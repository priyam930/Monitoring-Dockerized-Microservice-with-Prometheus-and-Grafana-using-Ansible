from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Counter with labels
request_counter = Counter(
    "app_requests_total", 
    "Total number of HTTP requests",
    ["endpoint"]
)

@app.route("/")
def hello():
    request_counter.labels(endpoint="/").inc()
    return "👋 Hello from Flask Microservice!"

@app.route("/about")
def about():
    request_counter.labels(endpoint="/about").inc()
    return "ℹ️ About page: Flask with Prometheus monitoring."

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    # Run Flask with threading enabled
    app.run(host="0.0.0.0", port=5000, threaded=True)
