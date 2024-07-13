import RPi.GPIO as GPIO
import subprocess

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Using GPIO pin 17


# Set up an event detection on GPIO pin 17
while True:
    if GPIO.wait_for_edge(17, GPIO.RISING) is not None:
        print("Signal Detected!")
        subprocess.run(["python3", "pitransmit.py"])
        break


