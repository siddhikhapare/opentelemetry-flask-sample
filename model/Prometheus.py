from prometheus_client import start_http_server

from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
#from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
import time
import random


resource = Resource(attributes={
    SERVICE_NAME: "usersapi-services"
})

# Start Prometheus client
#start_http_server(port=8000, addr="localhost")


reader = PrometheusMetricReader()
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)


if __name__ == "__main__":
    meter = metrics.get_meter(
        name="usersapi", 
        version="0.1.2"
        #__name__
    )
    # create a counter instrument and provide the first data point
    counter = meter.create_counter(
        name="requests",
        description="number of requests",
        unit="1",
        value_type=int,
        label_keys=("environment",),
    )
    # add labels
    labels = {
        #"dimension": "value",
        "environment": "staging"
    }
    counter.add(25, labels)

    # create a updowncounter instrument
    requests_active = meter.create_updowncounter(
        name="requests_active",
        description="number of active requests",
        unit="1",
        value_type=int,
    )
    # add labels
    labels = {
        "environment": "staging"
    }
    # provide the first data point
    requests_active.add(-2, labels)

    
    histogram = meter.create_histogram(
        name="http.server.duration",
        unit="ms",
        description="Response times for all requests",
        value_type=float
    )
    histogram.record(50,http_method="POST", http_scheme="http")
    histogram.record(100,http_method="GET", http_scheme="http")
    
# Labels are used to identify key-values that are associated with a specific
# metric that you want to record. These are useful for pre-aggregation and can
# be used to store custom dimensions pertaining to a metric














