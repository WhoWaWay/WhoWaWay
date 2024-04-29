# Derived from: 
# * https://github.com/peterhinch/micropython-async/blob/master/v3/as_demos/auart.py
# * https://github.com/tve/mqboard/blob/master/mqtt_async/hello-world.py


from mqtt_async import MQTTClient, config
import uasyncio as asyncio
import time
from machine import UART
from machine import Pin 
import logging
import my_oled
logging.basicConfig(level=logging.DEBUG)
led = Pin(2, Pin.OUT)
#Old
#Foward = Pin(21, Pin.OUT)
#Backward = Pin(19, Pin.OUT)
#Left = Pin(18, Pin.OUT)
#Right = Pin(5, Pin.OUT)
#New
Foward = Pin(23, Pin.OUT)
Backward = Pin(19, Pin.OUT)
Left = Pin(18, Pin.OUT)
Right = Pin(5, Pin.OUT)
msg = b'0'
#import uos, machine
#uos.dupterm(None, 1) #disable REPL on UART(0)
#import gc
#gc.collect()

MAXTX = 4

# Change the following configs to suit your environment
TOPIC_PUB = 'EGR314/Team205/LYT1'
#TOPIC_SUB = 'EGR314/Team205/OLED'
TOPIC_SUB = 'EGR314/Team205/LYT1/RC'
#TOPIC_OLED = 'EGR314/Team205/OLED'
TOPIC_HALLEFFECT = 'EGR314/Team205/LYT1/HallEffect'
TOPIC_HUMIDITY = 'EGR314/Team205/LYT1/Humidity'
TOPIC_TEMPERATURE = 'EGR314/Team205/LYT1/Temperature'

config.server = 'egr3x4.ddns.net' # can also be a hostname
#config.ssid     = 'ASUS RT-AX3000'
#config.wifi_pw  = 'ASUS12345678'
config.ssid     = 'photon'
config.wifi_pw  = 'particle'
#config.ssid = 'LY iPhone 13 Pro Max'ccccccccccc
#config.wifi_pw = 'luyansmart'

uart = UART(2, 9600,tx=17,rx=16)
uart.init(9600, bits=8, parity=None, stop=1,flow=0) # init with given parameters

async def receiver():
    b = b''
    sreader = asyncio.StreamReader(uart)
    while True:
        res = await sreader.read(1)
        if res==b'\r':
            #await client.publish(TOPIC_PUB, b, qos=1)
            #print('published', b)            
            
            
            debug = chr(b[0])
            print('debug',debug)
            if debug=='A':
                #b[0]=b''
                await client.publish(TOPIC_HALLEFFECT, b, qos=1)
                my_oled.print_data(b)
                print('published', b)
            elif debug=='T':
                #b[0]=b''
                await client.publish(TOPIC_TEMPERATURE, b, qos=1)
                my_oled.print_data(b)
                print('published', b)
            elif debug=='R':
                #b[0]=b''
                await client.publish(TOPIC_HUMIDITY, b, qos=1)
                my_oled.print_data(b)
                print('published', b)            
            
            
            
        #if res==b'\r':
         #   await client.publish(TOPIC_SUB, b, qos=1)
          #  print('published', b)
                
            b = b''
            led.value(led.value()^1)
            
            
        else:
            b+=res
        

def callback(topic, msg, retained, qos):
    print('callback',topic, msg, retained, qos)
    #my_oled.print_data(msg)
    #my_oled.plot_data(msg)
    
    while (not not msg):
        
        #
        print('msg=',msg)
        
        if msg==b'@':
            Left.value(0)
            Right.value(0)
            Foward.value(0)
            Backward.value(0)
        
        if msg==b'QqQ':
            Left.value(1)
            Right.value(0)
            Foward.value(1)
            Backward.value(0)
        
        if msg==b'WwW':
            Left.value(0)
            Right.value(0)
            Foward.value(1)
            Backward.value(0)
        
        if msg==b'EeE':
            Left.value(0)
            Right.value(1)
            Foward.value(1)
            Backward.value(0)
        
        if msg==b'AaA':
            Left.value(1)
            Right.value(0)
            Foward.value(0)
            Backward.value(0)
        
        if msg==b'SsS':
            Left.value(1)
            Right.value(1)
            Foward.value(1)
            Backward.value(1)
            
        
        if msg==b'DdD':
            Left.value(0)
            Right.value(1)
            Foward.value(0)
            Backward.value(0)
            
        if msg==b'ZzZ':
            Left.value(1)
            Right.value(0)
            Foward.value(0)
            Backward.value(1)
        
        if msg==b'XxX':
            Left.value(0)
            Right.value(0)
            Foward.value(0)
            Backward.value(1)
        
        if msg==b'CcC':
            Left.value(0)
            Right.value(1)
            Foward.value(0)
            Backward.value(1)
            
        
        

        uart.write(msg[:MAXTX])
        time.sleep(.01)
        msg = msg[MAXTX:]


        uart.write('\r\n')
        time.sleep(.01)
        
        
        

  
async def conn_callback(client): await client.subscribe(TOPIC_SUB, 1)

async def main(client):
    await client.connect()
    asyncio.create_task(receiver())
    while True:
        await asyncio.sleep(1)

config.subs_cb = callback
config.connect_coro = conn_callback

client = MQTTClient(config)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(client))

