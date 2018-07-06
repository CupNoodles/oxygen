import board
import time
import pulseio
import busio as io

import adafruit_ht16k33.segments

from adafruit_bus_device.i2c_device import I2CDevice

# i2c initialize
i2c = io.I2C(board.SCL, board.SDA)

display = adafruit_ht16k33.segments.Seg7x4(i2c)

# 0x61 is the default for the chip that comes with the Atlas Scientific DO sensor
sensor = I2CDevice(i2c, 0x61)

#RGB Strip Color 
def colors(value):

    # change these to the range you want! keep in mind that if you're putting this on a boat, red and green are kinda off-limits, even between two of the colors
    low = [100, 0, 100]
    mid = [20, 20, 20]
    high = [0, 0, 100]

    # 8mg/l and ideal level of DO (it probably depends on what you are, but most fish like 7-9)
    
    median = 8 #mg/l
    low_range = 5 #mg/l
    high_range = 5 #mg/l
    
    offset = median - value
    c = [0,0,0]
    if offset < 0 : #high
        c[0] = mid[0] - ( ( min(high_range, abs(offset)) / high_range ) * (mid[0] - high[0]) )
        c[1] = mid[1] - ( ( min(high_range, abs(offset)) / high_range ) * (mid[1] - high[1]) )
        c[2] = mid[1] - ( ( min(high_range, abs(offset)) / high_range ) * (mid[2] - high[2]) )        
    elif offset > 0 : #low
        c[0] = mid[0] - ( ( min(low_range, abs(offset)) / low_range ) * (mid[0] - low[0]) )
        c[1] = mid[1] - ( ( min(low_range, abs(offset)) / low_range ) * (mid[1] - low[1]) )
        c[2] = mid[1] - ( ( min(low_range, abs(offset)) / low_range ) * (mid[2] - low[2]) )        
    else:
        c = mid

    red.duty_cycle = duty_cycle(c[0]) 
    green.duty_cycle = duty_cycle(c[1])
    blue.duty_cycle = duty_cycle(c[2]) 
    

    return c

def duty_cycle(percent):
    return int(percent / 100.0 * 65535.0)


red = pulseio.PWMOut(board.D3)
green = pulseio.PWMOut(board.D4)
blue = pulseio.PWMOut(board.D11)

while True:

    with sensor:
        sensor.write(bytes([ord('R')]))
        time.sleep(0.6)
        result = bytearray(5)
        sensor.readinto(result)
    
    ov_char =  chr(result[1]) + chr(result[2]) + chr(result[3]) + chr(result[4])
    ov_num = (float(ov_char))
    colors(ov_num)
    display.number(ov_num)
    display.show()

    time.sleep(0.4)