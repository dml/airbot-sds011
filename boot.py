import esp
import gc
import network
import webrepl
import config


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(config.WIFI_USER, config.WIFI_PASSWORD)
        while not wlan.isconnected():
            pass


esp.osdebug(None)

do_connect()

webrepl.start()

gc.collect()
