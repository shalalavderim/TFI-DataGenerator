import logging

import azure.functions as func
import random
import time
from datetime import date
# pip install azure-iot-device==2.0.0rc11
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=ih-apio-tfi.azure-devices.net;DeviceId=dv-iot-tfi;SharedAccessKey=zRJnhN8uoBLCLD1rZu/pUsty2OlsOu9SgVmEL/jerTg="
VIN = '1GBJ7T1C1YJ51'
TEMPERATURE = 50.0
TIMESTAMP = time.time()
MSG_TXT = '{{"vin": "{vin}", "temperature": {temperature}, "timestamp": {timestamp}}}'

def iothub_data_generator():

    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print ( "IoT Hub device sending periodic messages" )

        f_date = date(2015, 11, 3)
        l_date = date.today()
        delta = l_date - f_date

        i = 1200
        while (i <= delta.days):
            # Build the message with simulated sensor values.
            temperature = TEMPERATURE + (random.random() * 70)
            vin = VIN + str(i)
            timestamp = TIMESTAMP
            msg_txt_formatted = MSG_TXT.format(vin=vin, temperature=temperature, timestamp=timestamp)
            message = Message(msg_txt_formatted)

            # Add a custom flag property to the message.
            if temperature > 90:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            #print( "Sending message: {}".format(message) )
            client.send_message(message)
            #print ( "Message successfully sent" )
            time.sleep(0.01)
            i = i + 1

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    iothub_data_generator()

    return func.HttpResponse(
      '{"response": "This HTTP triggered function executed successfully."}',
             status_code=200
    )
