import gc
import webrepl
import time
from sensor import network
gc.collect()

network.connect()
webrepl.start()
time.sleep_ms(1000)
