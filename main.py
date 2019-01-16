import sds011
import time
import cloud


sensor = sds011.SDS011()
report = cloud.connect()

while True:
    try:
        measurements = sensor.read()
        if measurements is None:
            pass
        else:
            report.compose(*measurements)
            time.sleep_ms(5000)
    except KeyboardInterrupt as e:
        print('KeyboardInterrupt')
