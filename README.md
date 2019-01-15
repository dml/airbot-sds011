# airbot-sds011

## install libs

```bash
micropython -m upip install -p . micropython-umqtt.robust
```



## Deploy

```bash
mpfshell -n -c "open ws:192.168.0.166,wemos" -s deploy.mpf
```
