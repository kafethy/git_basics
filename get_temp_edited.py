import psutil
import sounddevice as sd
import numpy as np
from pyobjc import ObjCClass

class MacOCCpuTempSensor(SensorValue):
    def get_value(self):
        try:
            # Using pyobjc to access macOS temperature data
            SMCKit = ObjCClass('SMCKit')
            temperature = SMCKit.SMCProcessor().temperature()
            return temperature
        except Exception as e:
            print(f"Error retrieving temperature: {e}")
            return None

class BatteryLevelSensor(SensorValue):
    def get_value(self):
        try:
            battery = psutil.sensors_battery()
            if battery:
                battery_level = battery.percent
                return battery_level
            else:
                print("Battery information not available.")
                return None
        except Exception as e:
            print(f"Error retrieving battery level: {e}")
            return None

class MicrophoneNoiseSensor(SensorValue):
    def get_value(self):
        try:
            # Update the audio recording code for macOS
            audio_data = sd.rec(int(2 * 44100), samplerate=44100, channels=1, dtype='int16')
            sd.wait()
            rms = np.sqrt(np.mean(audio_data ** 2))
            rms_rounded = round(rms, 2)
            return rms_rounded
        except Exception as e:
            print(f"Error retrieving microphone noise level: {e}")
            return None

class CpuUsageSensor(SensorValue):
    def get_value(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_usage_with_units = f"{cpu_usage}"
            return cpu_usage_with_units
        except Exception as e:
            print(f"Error retrieving CPU usage: {e}")
            return None

if __name__ == '__main__':
    macos_cpu_temp_sensor = MacOCCpuTempSensor()
    sensor_macos_cpu_temp = Sensor(macos_cpu_temp_sensor)
    result_macos_cpu_temp = sensor_macos_cpu_temp.get_value()
    if result_macos_cpu_temp is not None:
        print(f"macOS CPU Temperature: {result_macos_cpu_temp} °C")
    else:
        print("Error retrieving macOS CPU temperature.")

    battery_level_sensor = BatteryLevelSensor()
    sensor_battery_level = Sensor(battery_level_sensor)
    result_battery_level = sensor_battery_level.get_value()
    if result_battery_level is not None:
        print(f"Battery Level: {result_battery_level} %")
    else:
        print("Error retrieving battery level.")

    cpu_usage_sensor = CpuUsageSensor()
    sensor_cpu_usage = Sensor(cpu_usage_sensor)
    result_cpu_usage = sensor_cpu_usage.get_value()
    if result_cpu_usage is not None:
        print(f"CPU Usage: {result_cpu_usage} %")
    else:
        print("Error retrieving CPU usage.")

    microphone_noise_sensor = MicrophoneNoiseSensor()
    sensor_microphone_noise = Sensor(microphone_noise_sensor)
    result_microphone_noise = sensor_microphone_noise.get_value()
    if result_microphone_noise is not None:
        print(f"Microphone Noise Level: {result_microphone_noise} dB")
    else:
        print("Error retrieving microphone noise level.")
