from setuptools import setup

setup(name='windlogger2mqtt',
      version='0.1',
      description='Windlogger 2 MQTT bridge',
      url='https://github.com/gbeine/windlogger2mqtt',
      author='Gerrit',
      author_email='mail@gerritbeine.de',
      license='MIT',
      packages=['windlogger2mqtt'],
      requires=[
          'logging',
          'paho.mqtt',
          'pyserial',
          'pyyaml',
        ],
      zip_safe=False)
