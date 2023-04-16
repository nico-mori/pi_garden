from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)

try:
	while True:
		print('{:>5.3f}'.format(chan0.voltage))
		sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
