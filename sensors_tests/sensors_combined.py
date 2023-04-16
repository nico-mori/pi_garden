from time import sleep
from smbus import SMBus
from bmp280 import BMP280
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

bus = SMBus(1)


DEVICE = 0x23
ONE_TIME_HIGH_RES_MODE_1 = 0x20

#light_data = bus.read_i2c_block_data(DEVICE,ONE_TIME_HIGH_RES_MODE_1)
#light_result=(light_data[1] + (256 * light_data[0])) / 1.2


bmp280 = BMP280(i2c_dev=bus)

#temperature = bmp280.get_temperature()
#pressure = bmp280.get_pressure()


i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan0 = AnalogIn(ads, ADS.P0)


while True:
	light_data = bus.read_i2c_block_data(DEVICE,ONE_TIME_HIGH_RES_MODE_1)
	light_result=(light_data[1] + (256 * light_data[0])) / 1.2
	
	temperature = bmp280.get_temperature()
	pressure = bmp280.get_pressure()
	
	hum_voltage = chan0.voltage

	print("Light Level : " + format(light_result,'.2f') + " lx	-", '{:05.2f}*C {:05.2f}hPa'.format(temperature, pressure), 'humidity: {:>5.3f}'.format(hum_voltage))
	sleep(5)
