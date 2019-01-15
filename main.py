import ubinascii
import machine
import config
from time import sleep_ms
from umqtt.robust import MQTTClient


client_id = ubinascii.hexlify(machine.unique_id()).decode()
topic = 'sensors/{}/dust'.format(client_id)
mqtt = MQTTClient(
    client_id='SDS011',
    server=config.MQTT_HOST,
    port=config.MQTT_PORT,
    user=config.MQTT_USER,
    password=config.MQTT_PASSWORD,
)

mqtt.connect()


while True:
    sleep_ms(2500)
    message = '{},pm2_5,3,pm10,30'.format(client_id)
    mqtt.publish(topic, message)
    sleep_ms(2500)
