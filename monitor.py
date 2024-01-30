import psutil
import cpuinfo
import platform
import time
import datetime
import GPUtil

class CPU:
    def __init__(self):
        cpuInfo = cpuinfo.get_cpu_info()
        self.name = cpuInfo['brand_raw']
        self.cores = psutil.cpu_count(False)
        self.logical_cores = psutil.cpu_count()
        self.base_frequency = round(float(cpuInfo["hz_advertised_friendly"].replace(" GHz", "")), 2)
        self.architecture = cpuInfo["arch"]
    
    @staticmethod
    def get_usage():
        return psutil.cpu_percent()

class System:
    def __init__(self):
        self.name = platform.system()
        self.release = platform.release()
        self.version = platform.version()

    @staticmethod
    def get_uptime():
        timeSinceBootSeconds = int(time.time()) - int(psutil.boot_time())
        timeSinceBootReadable = datetime.timedelta(seconds = timeSinceBootSeconds)
        return timeSinceBootReadable
    
class Memory:
    def __init__(self):
        memory = psutil.virtual_memory()
        self.total = round(memory.total / 1024 / 1024 / 1024, 2)

    def get_used_memory(self):
        memory = psutil.virtual_memory()
        return round(memory.used / 1024 / 1024 / 1024, 2)
    
    def get_free_memory(self):
        return round(self.total - self.get_used_memory(), 2)
    
    def get_memory_usage(self):
        return round((self.total - self.get_free_memory()) / self.total * 100 , 1)
    
class GPU:
    def __init__(self):
        self.check_gpu()

    def check_gpu(self):
        try: 
            GPUtil.getGPUs()
        except:
            self.gpu = "Unknown GPU"
            return self.gpu
        else:
            self.gpu = GPUtil.getGPUs()[0]
            self.name = self.gpu.name
            self.total_memory = round(self.gpu.memoryTotal / 1024, 2)
        
    def get_used_memory(self):
        return round(self.gpu.memoryUsed / 1024, 2) 

    def get_free_memory(self):
        return round((self.gpu.memoryTotal - self.gpu.memoryUsed) / 1024, 2)

    def get_memory_usage(self):
        return round(self.gpu.memoryUtil * 100, 1)
        
    def get_load(self):
        return round(self.gpu.load * 100, 1)
    
    def get_temperature(self):
        return self.gpu.temperature
    
class Storage():
    @staticmethod
    def get_drives():
        partitions = psutil.disk_partitions()
        drives = []
        for partion in partitions:
            drive = psutil.disk_usage(partion.device)
            drives.append([partion.device, 
                           round(drive.total / 1024 / 1024 / 1024, 2), 
                           round(drive.used / 1024 / 1024 / 1024, 2), 
                           round(drive.free / 1024 / 1024 / 1024, 2), 
                           drive.percent])
        return drives
    
gpu = GPU()

