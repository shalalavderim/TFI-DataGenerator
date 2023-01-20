import logging

import azure.functions as func
# pip install azure-iot-device==2.0.0rc11

def hello_world():

    message = 'HelloWorld'
    return message

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    hello_world()

    return func.HttpResponse(
      '{"response": "This HTTP triggered function HellloWorld executed successfully."}',
             status_code=200
    )
