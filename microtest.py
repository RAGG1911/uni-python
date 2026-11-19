from machine import Pin
import time

led = Pin("LED", Pin.OUT)

for i in range(5):
    led.on()
    print("LED encendido")
    time.sleep(0.5)
    led.off()
    print("LED apagado")
    time.sleep(0.5)
    
print("Prueba completada")
