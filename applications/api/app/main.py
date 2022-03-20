from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/v1/exemple1")
def exemple1():
    return {"test": "exemple1"}


@app.get("/api/v1/exemple2")
def exemple2():
    return {"test": "exemple2"}


@app.get("/api/v1/exemple3")
def exemple3():
    return {"test": "exemple3"}


@app.get("/api/v1/exemple4")
def exemple4():
    return {"test": "exemple4"}
