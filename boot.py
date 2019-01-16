import gc
import webrepl
import time
import wireless
gc.collect()

wireless.connect()
webrepl.start()
time.sleep_ms(1000)
