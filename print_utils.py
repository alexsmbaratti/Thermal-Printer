from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)

def init():
    printer.feed(1)

def flush():
    printer.setSize('S')
    printer.feed(1)
    printer.justify('C')
    printer.println("Pixel Shelf")
    printer.println("Generated on ")
    printer.feed(2)
    printer.sleep()
    printer.wake()
    printer.setDefault()

def print_library_size(count):
    init()
    printer.feed(1)
    printer.justify('C')
    printer.setSize('S')
    printer.println('Library Size')
    printer.setSize('L')
    printer.println(str(count))
    flush()