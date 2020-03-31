import wmi
import json

# number of values in arrays => 60 for 1 minute history of values
NB_VALUES_ARRAY = 60

# wmi to get the data
ohm = wmi.WMI(namespace='root\OpenHardwareMonitor')

class DataToSend:
    def __init__(self):
        self.cpu = Cpu()
        self.gpu = Gpu()
        self.ram = Ram()
        self.ssd1 = Disk('KINGSTON SA400S37480G', '/hdd/0')
        self.ssd2 = Disk('KINGSTON SV300S37A120G', '/hdd/2')
        self.hdd1 = Disk('WDC WD10EZEX-08M2NA0', '/hdd/1')

    def update(self):
        sensors = ohm.Sensor()

        # CPU
        if(len(self.cpu.load) == NB_VALUES_ARRAY):
            self.cpu.load.pop(0)
        self.cpu.load.append(next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Total'), None))

        if(len(self.cpu.temperatures) == NB_VALUES_ARRAY):
            self.cpu.temperatures.pop(0)
        self.cpu.temperatures.append(next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Temperature' and sensor.Name == 'CPU Core'), None))

        self.cpu.loadCore1 = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Core #1'), self.cpu.loadCore1)
        self.cpu.loadCore2 = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Core #2'), self.cpu.loadCore2)
        self.cpu.loadCore3 = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Core #3'), self.cpu.loadCore3)
        self.cpu.loadCore4 = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Core #4'), self.cpu.loadCore4)
        self.cpu.loadCore5 = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Core #5'), self.cpu.loadCore5)
        self.cpu.loadCore6 = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Core #6'), self.cpu.loadCore6)

        # GPU
        if(len(self.gpu.load) == NB_VALUES_ARRAY):
            self.gpu.load.pop(0)
        self.gpu.load.append(next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'GPU Core'), None))

        if(len(self.gpu.temperatures) == NB_VALUES_ARRAY):
            self.gpu.temperatures.pop(0)
        self.gpu.temperatures.append(next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Temperature' and sensor.Name == 'GPU Core'), None))

        self.gpu.ramLoad = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'GPU Memory'), self.gpu.ramLoad)

        # RAM
        self.ram.load = next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'Memory'), self.ram.load)

        # SSD/HDD
        self.ssd1.usedSpace = next((round(sensor.Value, 2) for sensor in sensors if self.ssd1.parent == sensor.Parent and sensor.Name == 'Used Space'), self.ssd1.usedSpace)

        self.ssd2.usedSpace = next((round(sensor.Value, 2) for sensor in sensors if self.ssd2.parent == sensor.Parent and sensor.Name == 'Used Space'), self.ssd2.usedSpace)

        self.hdd1.usedSpace = next((round(sensor.Value, 2) for sensor in sensors if self.hdd1.parent == sensor.Parent and sensor.Name == 'Used Space'), self.hdd1.usedSpace)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Cpu:
    def __init__(self):
        

        self.load = []
        self.temperatures = []

        self.loadCore1 = None
        self.loadCore2 = None
        self.loadCore3 = None
        self.loadCore4 = None
        self.loadCore5 = None
        self.loadCore6 = None

class Gpu:
    def __init__(self):
        self.load = []
        self.temperatures = []
        self.ramLoad = None

class Ram:
    def __init__(self):
        self.load = None

class Disk:
    def __init__(self, name, parent):
        self.name = name
        self.usedSpace = None
        self.parent = parent
