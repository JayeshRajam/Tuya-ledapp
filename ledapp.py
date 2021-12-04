#!/usr/bin/env python
import time
import coloredlogs
from tuyalinksdk.client import TuyaClient
from tuyalinksdk.console_qrcode import qrcode_generate
coloredlogs.install(level='DEBUG')
import sys
import serial
import time
 # Define the serial port and baud rate.
ser = serial.Serial('COM11', 115200)	#ENTER YOUR PORT

client = TuyaClient(productid='YOUR PRODUCTID',
                    uuid='YOUR UUID',
                    authkey='YOUR AUTHKEY')
#ENTER YOUR CORRESPONDING DETAILS

def on_connected():
    print('Connected.')

def on_qrcode(url):
    qrcode_generate(url)

def on_reset(data):
    print('Reset:', data)

def on_dps(dps):
    print('DataPoints:', dps)
    if(dps == {'101':True}):
    	print("LED is on...")
    	time.sleep(0.1)
    	ser.write(b'H')
    	print('ON')
    elif(dps=={'101':False}):
    	print("LED is off...")
    	time.sleep(0.1)
    	ser.write(b'L')
    	print('OFF')
    client.push_dps(dps)

client.on_connected = on_connected
client.on_qrcode = on_qrcode
client.on_reset = on_reset
client.on_dps = on_dps

client.connect()
client.loop_start()

while True:
    time.sleep(1)
