#!/usr/bin/python3

import time
import serial

ser = serial.Serial("/dev/ttyACM0", baudrate=9600)

try:
    while True:
          read = ser.readline().strip()
          print(read)

except KeyboardInterrupt:
    print("\nInterrupcion por teclado")

except ValueError as ve:
    print(ve)
    print("F")

finally:
    ser.close()


