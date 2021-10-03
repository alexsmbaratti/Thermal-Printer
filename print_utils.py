from Adafruit_Thermal import *
from datetime import date
from datetime import datetime
import json

printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)

def init():
    printer.feed(1)
    printer.underlineOff()
    printer.boldOff()


def flush():
    today = date.today()

    printer.setSize('S')
    printer.justify('C')
    printer.println("Pixel Shelf")
    printer.println("Generated on " + str(today.strftime("%B %d, %Y")))
    printer.feed(2)
    printer.sleep()
    printer.wake()
    printer.setDefault()


def print_library_size(count):
    init()
    printer.justify('C')
    printer.setSize('S')
    printer.println('Library Size')
    printer.setSize('L')
#     TODO: Breakdown library size by physical/digital
    printer.println(str(count))
    flush()


def print_library_entry(entry):
    library_json = json.loads(entry)

    addDate = datetime.strptime(str(library_json['date']), '%Y-%m-%dT%H:%M:%S.%f%z')
    condition = 'New' if library_json['new'] == 1 else 'Used'
    box = 'Yes' if library_json['box'] == 1 else 'No'
    manual = 'Yes' if library_json['manual'] == 1 else 'No'
    gift = 'Yes' if library_json['gift'] == 1 else 'No'

    cost = '$' + str(library_json['cost']) # TODO: Handle currency

    init()
    printer.justify('C')
    printer.setSize('M')
    printer.println(library_json['title'])
    printer.setSize('S')
    printer.boldOn()
    printer.println(library_json['platform'])
    printer.boldOff()
    printer.justify('L')
    printer.feed(1)
    printer.println(library_json['edition'] + '\t\t' + cost)  # TODO: Strikethrough MSRP if cost is lower
    printer.println("\tCondition: " + str(condition))
    printer.println("\tBox: " + str(box))
    printer.println("\tManual: " + str(manual))
    printer.println("Added on " + str(addDate.strftime("%B %d, %Y")))
    printer.feed(1)
    printer.justify('C')
    if library_json['upc']:
        printer.setBarcodeHeight(100)
        printer.printBarcode(library_json['upc'], printer.UPC_A)
    flush()


def has_paper():
    return printer.has_paper()
