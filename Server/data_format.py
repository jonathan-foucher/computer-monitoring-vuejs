import wmi
import json
import time

# number of values in arrays => 60 for 1 minute history of values
NB_VALUES_ARRAY = 60

NB_CPU_CORES = 6

# wmi to get the data
ohm = wmi.WMI(namespace='root\OpenHardwareMonitor')

class DataToSend:
    def __init__(self):
        self.time = []
        self.cpu = Cpu()
        self.gpu = Gpu()
        self.ram = Ram()
        self.ssd1 = Disk('SSD Kingston 480 Go', '/hdd/0')
        self.ssd2 = Disk('SSD Kingston 120 Go', '/hdd/2')
        self.hdd1 = Disk('HDD WD 930 Go', '/hdd/1')

    def update(self):
        sensors = ohm.Sensor()

        # time
        if(len(self.time) == NB_VALUES_ARRAY):
            self.time.pop(0)
        self.time.append(round(time.time() * 1000))

        # CPU
        if(len(self.cpu.load) == NB_VALUES_ARRAY):
            self.cpu.load.pop(0)
        self.cpu.load.append(next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Total'), None))

        if(len(self.cpu.temperatures) == NB_VALUES_ARRAY):
            self.cpu.temperatures.pop(0)
        self.cpu.temperatures.append(next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Temperature' and sensor.Name == 'CPU Core'), None))

        self.cpu.coresLoad
        for i in range(0, NB_CPU_CORES):
            self.cpu.coresLoad[i] = (next((round(sensor.Value, 2) for sensor in sensors if sensor.SensorType == 'Load' and sensor.Name == 'CPU Core #' + str(i + 1)), self.cpu.coresLoad[i]))

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
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, separators=(',', ':'))

class Cpu:
    def __init__(self):
        self.load = []
        self.temperatures = []
        self.coresLoad = []
        for i in range(1, (NB_CPU_CORES + 1)):
            self.coresLoad.append(None)

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
