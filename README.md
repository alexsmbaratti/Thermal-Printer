# Thermal Printer Server
## Installation
### Hardware Needed
* [Tiny Thermal Receipt Printer - TTL Serial / USB](https://www.adafruit.com/product/2751)
* [5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
* [Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
* Raspberry Pi (recommended)

### Files Needed
* Adafruit_Thermal.py

### Running
```bash
export FLASK_APP=main
flask run --host=0.0.0.0
```