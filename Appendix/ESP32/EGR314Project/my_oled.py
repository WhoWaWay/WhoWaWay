from machine import Pin, SoftI2C
import ssd1306
import gfx
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

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
    # my_values = [float(item) for item in my_strings]

    # clear screen
    oled.fill(0)

    # iterate through values
    for ii,item in enumerate(my_strings):
        # print string on new line
        oled.text(str(item), 0, 10*ii)

    # show screen
    oled.show()

def plot_data(msg):
    #Decode the message and convert to float
    data_points = [float(value) for value in msg.decode('utf-8').split()]
    
    #Check for empty data_points list
    if not data_points:
        print("No data to plot.")
        return
    
    #Calculate min and max values for scaling
    min_val = min(data_points)
    max_val = max(data_points)
    
    #Clear the screen for fresh drawing
    oled.fill(0)
    
    #Calculate the scaling factors for x and y dimensions
    x_increment = oled_width / (len(data_points) - 1) if len(data_points) > 1 else 1
    y_scale = (oled_height - 1)/(max_val - min_val) if max_val != min_val else 1
    
    #Plot and connect the data points
    for i in  range(len(data_points)-1):
        x0 = int(i*x_increment)
        y0 = oled_height - 1 - int((data_points[i] - min_val) * y_scale)
        x1 = int((i+1) * x_increment)
        y1 = oled_height - 1 - int((data_points[i+1] - min_val) * y_scale)
        
        graphics.line(x0, y0, x1, y1, 1)
        
    #Display the min and max values at the bottom and top of the screen, respectively
    oled.text(f"Min: {min_val}", 0, oled_height -10) #Bottom
    oled.text(f"Max: {max_val}", 0, 0) #Top
        
    #Refresh the OLED to show the updates
    oled.show()
    pass
    