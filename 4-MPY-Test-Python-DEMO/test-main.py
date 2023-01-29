from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(16, Pin.OUT)   
np = NeoPixel(pin, 1)   
np[0] = (10,0,0) 
np.write()              
r, g, b = np[0]
def handle_interrupt(Pin):
    np[0] = (0, 0, 0)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 0, 10)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 0, 10)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 0, 0)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 10, 0)
    np.write()
    time.sleep_ms(150)
    
    print("test-usr key")
p0 = Pin(0)
p0.init(p0.IN, p0.PULL_UP)       
p0.irq(trigger=p0.IRQ_FALLING, handler=handle_interrupt)