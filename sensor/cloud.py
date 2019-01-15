import config
from umqtt.robust import MQTTClient


class Report:
    def __init__(self, client_id):
        self.client_id = client_id
        self.mqtt = MQTTClient(
            client_id=client_id,
            server=config.MQTT_HOST,
            port=config.MQTT_PORT,
            user=config.MQTT_USER,
            password=config.MQTT_PASSWORD,
        )

    def connect(self):
        self.mqtt.connect()

    def publish(self, metric, value):
        topic = 'sensors/{}/{}'.format(self.client_id, metric)
        message = '{},{},{}'.format(self.client_id, metric, value)
        self.mqtt.publish(topic, message)

    def compose(self, pm2_5, pm10, status):
        self.publish('status', status)
        self.publish('pm2_5', pm2_5)
        self.publish('pm10', pm10)


def connect(client_id):
    report = Report(client_id)
    report.connect()
    return report
