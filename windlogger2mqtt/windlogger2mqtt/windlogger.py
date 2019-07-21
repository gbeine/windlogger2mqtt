
import logging
import serial

class windlogger:

	def __init__(self, config):
		self._config = config
		self._init_device()


	def update_and_publish(self, mqtt):
		line = self._readline()
		logging.info("Read from windlogger: %s", line)
		data = line.split(',')
		self._publish(mqtt, data[3], data[4], data[5])


	def _publish(self, mqtt, temperature, mean, maximum):
		mqtt.publish("temperature", temperature)
		mqtt.publish("mean", mean)
		mqtt.publish("max", maximum)

	def _readline(self):
		chars = []
		while True:
			b = self._device.read()
			chars.append(b.decode())
			if b == b'\n':
				break
		return ''.join(chars)


	def _init_device(self):
		if not "device" in self._config:
			raise ValueError("Missing device for windlogger")

		self._device = serial.Serial()
		self._device.port = self._config["device"]
		self._device.baudrate = 4800
		self._device.bytesize = serial.EIGHTBITS
		self._device.parity = serial.PARITY_NONE
		self._device.stopbits = serial.STOPBITS_ONE
		self._device.xonxoff = False
		self._device.rtscts = False
		self._device.dsrdtr = False
		self._device.open()
