# planTV

## Libraries
- [raspi-lora 0.2] (https://pypi.org/project/raspi-lora/)

## Address
Main node can have from 1 to 254 nodes and then the single nodes can also have from 1 to 254 nodes.


All nodes must have this form in the main node:

```
120.11.110.250
```

|Main node (Raspberry)|Second class node|Third class node|
|0|1-254|1-254|

For subnodes they only contian arrays with information about subnodes and a value to represent the previous node. For more information [click here] ().

## Protocol

The communication protocol shortens every value when transmited to another node.

|Protocol|Description|Returns|Example|
|(address).sn|Searches for subnodes|List of nodes|5.55.102.sn|
|(address).st|Checks current state in node|True if connected, False if not|1.233.4.55.st|
|

