import network, esp, gc

gc.collect()
esp.osdebug(None)

ssid='jacksparrow'
password='Qwertyuiop'

station=network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid,password)

while station.isconnected()==False:
    pass
print('connection succesful')
print(station.ifconfig())