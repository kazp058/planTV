from raspi_lora import LoRa, ModemConfig
from config import *
import node
from toolkit import save, read_devices

def on_recv(payload):
    node_id = payload.header_from
    message = payload.message
    return node_id, message

nodes = read_devices()

lora = LoRa(0, 7, 0, freq = 915, tx_power = 5, modem_config = ModemConfig.Bw31_25Cr48Sf512,recieve_all = False, acks = False)
lora.on_recv = on_recv

lora.set_mode_rx()
message = "Hola mundo"
status = lora.send_to_wait(message, 10, retries=2)
if status is True:
    print("Mensaje enviado!")
else:
    print("No hay confirmacion del receptor :c")

lora.close()
