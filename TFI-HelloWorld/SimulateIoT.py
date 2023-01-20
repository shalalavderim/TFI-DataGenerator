# pip install azure-iot-device==2.0.0rc11

def hello_world():

    message = 'HelloWorld'
    return message

    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print ( "IoT Hub device sending periodic messages" )

        f_date = date(2015, 6, 19)
        l_date = date.today()
        delta = l_date - f_date

        i = 1000
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
            #time.sleep(1)
            i = i + 1

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Simulated device" )
    print ( "Press Ctrl-C to exit" )
    hello_world()
