from machine import ADC, Pin
import network
import requests
import time

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

ssid = 'AP-Room-01'
password = 'uabcsITC2025'  # are you mad bro?  
base_url = 'http://10.10.10.1:8000/'

magic = 130  # Env on my room

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

led = Pin(2, Pin.OUT)
led.off()

print("[+] Setup complete... ")

while True:
    sample = adc.read()
    if sample > magic:
        print("[!] hit ", sample)
        led.toggle()
        res = requests.get(base_url)
        time.sleep(1)
        led.toggle()
