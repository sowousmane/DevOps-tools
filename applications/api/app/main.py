from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics
from prometheus_client import Counter

app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# Define custom Prometheus metrics
custom_metric_counter = Counter('custom_metric_counter', 'Description of custom metric counter')


@app.get("/")
def read_root():
    # Increment the custom metric counter when this endpoint is accessed
    custom_metric_counter.inc()
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    # Increment the custom metric counter when this endpoint is accessed
    custom_metric_counter.inc()
    return {"item_id": item_id, "q": q}


@app.get("/api/v1/exemple1")
def exemple1():
    # Increment the custom metric counter when this endpoint is accessed
    custom_metric_counter.inc()
    return {"test": "exemple1"}


@app.get("/api/v1/exemple2")
def exemple2():
    # Increment the custom metric counter when this endpoint is accessed
    custom_metric_counter.inc()
    return {"test": "exemple2"}


@app.get("/api/v1/exemple3")
def exemple3():
    # Increment the custom metric counter when this endpoint is accessed
    custom_metric_counter.inc()
    return {"test": "exemple3"}


@app.get("/api/v1/exemple4")
def exemple4():
    # Increment the custom metric counter when this endpoint is accessed
    custom_metric_counter.inc()
    return {"test": "exemple4"}
