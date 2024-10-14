from flask import Flask
#import flask_monitoringdashboard as dashboard
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
#export DEBUG_METRICS=false
#dashboard.bind(app)
metrics = PrometheusMetrics(app=app)
app.debug = True
# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')


@app.route("/")
def index():
    return "WELCOME!"


@app.route("/v1/greetings")
def greetings():
    return "Hello World!"


@app.route("/v1/test")
def greetingsTest():
    return "Hello test!"


@app.route("/v1/prod")
def greetingsProd():
    return "Hello prod!"


if __name__ == "__main__":
    app.run(debug=True)
