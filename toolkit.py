import json
import os
from config import node_save_filename, data_save_filename, file_extension, test_node_save_filename, test_data_save_filename
from node import *

path = os.getcwd()


def save_devices(devices, filename):
    with open(path + "/saves/" + filename, 'w+') as node_file:
        for device_id in devices.keys():
            cache = device_id + "\n"
            node_file.write(cache)


def save_data(devices, filename):
    pass


def save(devices, test=False):
    if test == False:
        save_devices(devices, node_save_filename + "." + file_extension)
        save_data(devices, data_save_filename + "." + file_extension)
    else:
        save_devices(devices, test_node_save_filename + "." + file_extension)
        save_data(devices, test_data_save_filename + "." + file_extension)


def read_devices(filename=node_save_filename):
    cache = {}
    with open(path + "/saves/" + filename + "." + file_extension, 'r') as node_file:
        for line in node_file:
            address = line.strip().split(".")
            current = cache
            for node_id in address:
                if node_id not in current.keys():
                    current[node_id] = dict()
                    current = current[node_id]
                else:
                    current = current[node_id]

            print(current)
            node_id = line[0]
            subnodes = {}
            for i in range(len(line[1:])):
                subnodes[Node(i)] = dict()

    return cache


if __name__ == "__main__":
    pass