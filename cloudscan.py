import time
import pygatt
import cloud4rpi

mac = '00:00:00:00:00:00' #change this to your Rapid IoT kit Mac Address
DEVICE_TOKEN = 'xxxxxxxxxxxxxxxxx' #change this to your cloud4rpi device token

char_uuids = {
    "battery" : "08d41e61-ac11-40a2-a95a-e0e0fb5336ff",
    "tvoc" : "08d41e61-ac11-40a2-a95a-e0e0fb5336f9",
    "co2" : "08d41e61-ac11-40a2-a95a-e0e0fb5336fa",
    "pressure" : "08d41e61-ac11-40a2-a95a-e0e0fb5336fc",
    "altitude" : "08d41e61-ac11-40a2-a95a-e0e0fb5336f7",
    "temperature" : "08d41e61-ac11-40a2-a95a-e0e0fb5336fb",
    "humidity" : "08d41e61-ac11-40a2-a95a-e0e0fb5336fd",
    "ambient-light" : "08d41e61-ac11-40a2-a95a-e0e0fb5336fe"
}

def save_sensor_values():
	device = cloud4rpi.connect(DEVICE_TOKEN)
	adapter = pygatt.GATTToolBackend()
	try:
		adapter.start()
	        conn = adapter.connect(mac)

        	time_info = int(time.time()*1000000000.0)
		sensor_values = {}
		for sensor in char_uuids:
			value = conn.char_read(char_uuids[sensor])
			sensor_values[sensor] = float(value.decode("utf-8").rstrip('\00'))

		measure_all = []
		for sensor in sensor_values:
			measure = {"measurement" : sensor, "time" : time_info, "fields" : {"value" : sensor_values[sensor]}}
			measure_all.append(measure)
		co2_value = sensor_values['co2']
		tvoc_value = sensor_values['tvoc']
		battery_value = sensor_values['battery']
		hum_value = sensor_values['humidity']
		temp_value = sensor_values['temperature']
		light_value =  sensor_values['ambient-light']
		pressure_value = sensor_values['pressure']
		altitude_value = sensor_values['altitude']
#		print(measure_all)
		variables = {
                	'CO2': {
                        	'type': 'numeric',
                        	'value': co2_value
                	},
			'Pollution Level': {
                                'type': 'numeric',
                                'value': tvoc_value
                        },
                	'Battery': {
                        	'type': 'numeric',
                        	'value': battery_value
                	},
			'Humidity': {
                                'type': 'numeric',
                                'value': hum_value
                        },
                        'Temperature': {
                                'type': 'numeric',
                                'value': temp_value
                        },
			'Air Pressure': {
                                'type': 'numeric',
                                'value': pressure_value
                        },
			'Altitude': {
                                'type': 'numeric',
                                'value': altitude_value
                        },
			'Sun': {
                                'type': 'numeric',
                                'value': light_value
                        }
			

        	}

		device.declare(variables)
		device.publish_config()
		time.sleep(1)
		device.publish_data()
		print(sensor_values)

	except Exception as e:
		print("Error: ", e)
#		msg = "ParkScan: [%d] %s"%(time_info, e)

	finally:
		adapter.stop()
		

if __name__ == '__main__':
	save_sensor_values()
