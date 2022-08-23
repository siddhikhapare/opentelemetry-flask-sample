from flask import Flask
#from flask_cors import CORS
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)
#CORS(app)
FlaskInstrumentor().instrument_app(app)


try:
    from controller import *
except Exception as e:
    print(e)





