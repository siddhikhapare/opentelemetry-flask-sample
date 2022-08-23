from prometheus_client import start_http_server

from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
#from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
import time
import random

#https://open-telemetry.github.io/opentelemetry-python/getting-started.html

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "usersapi-services"
})

#meter = _metrics.get_meter("app_or_package_name")
#meter = get_meter_provider().get_meter("view-drop-aggregation", "0.1.2")


# Start Prometheus client
#start_http_server(port=8000, addr="localhost")

# Initialize PrometheusMetricReader which pulls metrics from the SDK
# on-demand to respond to scrape requests
reader = PrometheusMetricReader()
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)

#To get a meter, you need to provide the package name from which you are calling
#  the meter APIs to OpenTelemetry by calling MeterProvider.get_meter with the calling 
# instrumentation name and the version of your package.
#https://opentelemetry-python.readthedocs.io/en/latest/api/metrics.html
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

    #https://lightstep.com/opentelemetry/attributes-and-labels
    #https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md#histogram-creation
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














