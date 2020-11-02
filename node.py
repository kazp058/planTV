from raspi_lora import LoRa, ModemConfig
from Crypto.Cipher import AES

crypto = AES.new(b"planTVkey", AES.MODE_EAX)
LoRa(0, 7, 0, freq = 915, tx_power = 5, modem_config = ModemConfig.Bw31_25Cr48Sf512,
     ,recieve_all = False, acks = False, crypto)


devices = dict()

while len(devices.keys()) == 0:
   set_mode_rx()
