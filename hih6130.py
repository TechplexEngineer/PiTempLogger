import smbus
import time

def readSensor():
	# Get I2C bus
	bus = smbus.SMBus(1)

	# HIH6130 address, 0x27(39)
	# Read data back from 0x00(00), 4 bytes
	# humidity MSB, humidity LSB, temp MSB, temp LSB

	data = bus.read_i2c_block_data(0x27, 0x00, 4)

	Hum_H = data[0];
	Hum_L = data[1];
	Temp_H = data[2];
	Temp_L = data[3];

	# the top two bits in Hum_H are status
	status = (Hum_H >> 6) & 0x03;
	Hum_H = Hum_H & 0x3f; # mask off the status bits
	H_dat = ((Hum_H) << 8) | Hum_L;
	T_dat = ((Temp_H) << 8) | Temp_L;
	T_dat = T_dat / 4;

	RH = H_dat * 6.10e-3;
	T_C = T_dat * 1.007e-2 - 40.0;

	T_F = T_C * 1.8 + 32

	# if (status == 0):
	# 	status_desc = "Normal."
	# elif (status == 1):
	# 	status_desc = "Stale Data."
	# elif (status == 2):
	# 	status_desc = "In command mode."
	# else:
	# 	status_desc = "Diagnostic."

	return {
		# "status": {
		# 	"num": status,
		# 	"desc": status_desc
		# },
		"tempc": T_C,
		"tempf": T_F,
		"humidity": RH
	}