#!/usr/bin/python3
from raspi_lora import LoRa, ModemConfig
from Crypto.Cipher import AES

class node:

   def __init__(self, id, temperature, pressure, humidity, altitude, luminocity):
       self.id = id
       self.temperature = temperature
       self.pressure = pressure
       self.humidity = humidity
       self.altitude = altitude
       self.luminocity = luminocity

   def __init__(self, id):
       node(self, id, -1, -1, -1, -1, -1, -1)

crypto = AES.new(b"planTVkey", AES.MODE_EAX)
LoRa(0, 7, 0, freq = 915, tx_power = 5, modem_config = ModemConfig.Bw31_25Cr48Sf512,
     recieve_all = False, acks = False, crypto = crypto)


devices = dict()


