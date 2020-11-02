#!/usr/bin/python3
from config import retries

class Node:

     def __init__(self, address = [], temperature = "-1", pressure = "-1", \
                  humidity = "-1", altitude = "-1", luminocity = "-1", subnodes = {}):
          
          self.address = address
          self.temperature = temperature
          self.pressure = pressure
          self.humidity = humidity
          self.altitude = altitude
          self.luminocity = luminocity
          self.subnodes = subnodes

     def search_nodes(self, lora):
          new_subnodes = []
          #Search for nodes in every subnode
          for subnode in self.subnodes.keys():
               cache = subnode.search_nodes(lora)              
               new_subnodes.extend(cache)
          
          #Search for new nodes close to itself
          return self.send_protocol(lora, self.address, "sn")
               
     def send_protocol(self, lora, node_address, protocol = "st"):          
          status = lora.send_to_wait(".".join(self.address[1:] + "." + protocol), self.address[0], retries = retries)

          return status

     def add_subnode(self, address)
          pass

