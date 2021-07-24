from Adafruit_Thermal import *
from datetime import date

printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)

months = ["N/A", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]


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
    printer.println(str(count))
    flush()


def print_library_entry(entry):
    addDate = str(months[entry['month']]) + ' ' + str(entry['day']) + ', ' + str(entry['year'])
    condition = 'New' if entry['new'] == 1 else 'Used'
    box = 'Yes' if entry['box'] == 1 else 'No'
    manual = 'Yes' if entry['manual'] == 1 else 'No'

    cost = '$' + str(entry['cost'])

    init()
    printer.justify('C')
    printer.setSize('M')
    printer.println(entry['title'])
    printer.setSize('S')
    printer.boldOn()
    printer.println(entry['platform'])
    printer.boldOff()
    printer.justify('L')
    printer.feed(1)
    printer.println(entry['edition'] + '\t\t' + cost)  # TODO: Strikethrough MSRP if cost is lower
    printer.println("\tCondition: " + str(condition))
    printer.println("\tBox: " + str(box))
    printer.println("\tManual: " + str(manual))
    printer.println("Added on " + addDate)
    printer.feed(1)
    printer.justify('C')
    if entry['upc']:
        printer.setBarcodeHeight(100)
        printer.printBarcode(entry['upc'], printer.UPC_A)
    flush()


def has_paper():
    return printer.has_paper()
