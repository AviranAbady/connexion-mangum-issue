import logging.config
import os
import connexion
from config.logging import LOGGING_CONFIG
from connexion.options import SwaggerUIOptions
from mangum import Mangum
from payload import p

logging.config.dictConfig(LOGGING_CONFIG)

LOCAL_PORT = int(os.environ.get('MICROSERVICE_PORT', 0)) or 8080

options = SwaggerUIOptions(swagger_ui_path="/docs")
app = connexion.AsyncApp(__name__, specification_dir="spec", swagger_ui_options=options)

app.add_api("openapi.yaml", swagger_ui_options=options)


if __name__ == "__main__":
    # Development only server start
    # app.run(host='0.0.0.0', port=LOCAL_PORT)

    # p has the payload of an AWS lambda request for POST /api/mangum with request body {"payload": "test"}
    m = Mangum(app)
    m(p, None)
