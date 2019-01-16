import config
import network


def connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        sta_if.connect(config.WIFI_USER, config.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
