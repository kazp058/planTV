import json
import os
import config as cfg

path = os.getcwd()

def save_devices(devices, filename):
    with open(path + "/saves/" + filename, 'w+') as node_file:
         for device_id in devices.keys():
             cache = device_id + "\n"
             node_file.write(cache)

def save_data(devices, filename):
    pass

def save(devices, test = False):
    extension = cfg.file_extension

    if test == False:
       save_devices(devices, cfg.node_save_filename + "." + extesion)
       save_data(devices, cfg.data_save_filename + "." + extension)
    else:
       save_devices(devices, cfg.test_node_save_filename + "." + extension)
       save_data(devices, cfg.test_data_save_filename + "." + extension)

def read_devices(filename):
    with open("nodes.json",'r') as node_file:
         cache = node_file.read()
         return json.loads(cache)

if __name__ == "__main__":
   print(path)
   test_sample = {"1":{"temperature":29,"pressure":45,"humidity":95,"altitude":122,"luminocity":18},
                  "2":{"temperature":31,"pressure":50,"humidity":78,"altitude":102,"luminocity":20}}
   save(test_sample, test = True)


