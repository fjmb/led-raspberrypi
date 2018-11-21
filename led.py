import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

print("Ejecucion iniciada...")
iteracion = 0
while iteracion < 100:
  GPIO.output(11, True)
  GPIO.output(13, False)
  GPIO.output(15, False)
  time.sleep(2)
  GPIO.output(11, False)
  GPIO.output(13, True)
  GPIO.output(15, False)
  time.sleep(2)
  GPIO.output(11, False)
  GPIO.output(13, False)
  GPIO.output(15, True)
  time.sleep(2)
  iteracion = iteracion + 1
print "Ejecucion finalizada"
GPIO.cleanup()