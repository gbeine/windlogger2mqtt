
import time

from windlogger2mqtt import mqtt
from windlogger2mqtt import windlogger

class Daemon:

	def __init__(self, config):
		self._config = config
		self._init_mqtt()
		self._init_windlogger()

	def run(self):
		while True:
			self._windlogger.update_and_publish(self._mqtt)

	def _init_mqtt(self):
		self._mqtt = mqtt.Mqtt(self._config.mqtt())
		self._mqtt.connect()

	def _init_windlogger(self):
		self._windlogger = windlogger.windlogger(self._config.windlogger())
