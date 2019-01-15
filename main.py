import machine
import ubinascii
import sds011
from sensor import cloud


client_id = ubinascii.hexlify(machine.unique_id()).decode()
sensor = sds011.SDS011()
report = cloud.connect(client_id)

while True:
    measurements = sensor.read()
    if measurements is None:
        pass
    else:
        report.compose(*measurements)
