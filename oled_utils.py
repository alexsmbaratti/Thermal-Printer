from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
width = disp.width
height = disp.height
font = ImageFont.load_default()
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
padding = -2

def init():
    disp.fill(0)
    disp.show()
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

def display_title():
    draw.text((0, padding), "Thermal Printer", font=font, fill=255)

def display_idle():
    init()
    display_title()
    draw.text((0, padding + 8), "Idle...", font=font, fill=255)

    disp.image(image)
    disp.show()

def display_status(status):
    init()
    display_title()
    draw.text((0, padding + 8), str(status), font=font, fill=255)

    disp.image(image)
    disp.show()