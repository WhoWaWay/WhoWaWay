from machine import Pin, SoftI2C
import ssd1306
import gfx
from time import sleep

i2c = SoftI2C(scl=Pin(33), sda=Pin(32))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)

def print_data(msg):
    # convert byte array to string
    my_string = msg.decode('utf-8')
    # split string by spaces
    my_strings = my_string.split(" ")
    # convert string to float
    my_values = [float(item) for item in my_strings]

    # clear screen
    oled.fill(0)

    # iterate through values
    for ii,item in enumerate(my_values):
        # print string on new line
        oled.text(str(item), 0, 10*ii)

    # show screen
    oled.show()

def plot_data(msg):
    graphics.line(0,0,128,64,1)
