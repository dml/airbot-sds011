import config
from umqtt.robust import MQTTClient


class Report:
    def __init__(self):
        self.mqtt = MQTTClient(
            client_id=config.MQTT_CLIENT_ID,
            server=config.MQTT_HOST,
            port=config.MQTT_PORT,
            user=config.MQTT_USER,
            password=config.MQTT_PASSWORD,
        )

    def connect(self):
        self.mqtt.connect()

    def publish(self, metric, value):
        topic = '{}/feeds/{}'.format(
            config.MQTT_USER,
            metric
        )
        # message = 'particulate_matter,mgpcm={}'.format(value)
        self.mqtt.publish(topic, str(value))

    def compose(self, pm2_5, pm10, status):
        self.publish('pm2_5', pm2_5)
        self.publish('pm10', pm10)


def connect():
    report = Report()
    report.connect()
    return report
