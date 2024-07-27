from gpiozero import Button
import subprocess

# Set up GPIO
button = Button(27)

# Set up an event detection on GPIO pin 17
while True:
        if button.is_pressed:
        	print("Signal Detected!")
        	subprocess.run(["python3", "piTransmitConstant.py"])
        	break
