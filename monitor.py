import psutil
import cpuinfo
import time
import datetime

def Get_CPU_Name():
    return cpuinfo.get_cpu_info()['brand_raw']

def Get_CPU_Cores(logical = False):
    return psutil.cpu_count(logical)

def Get_CPU_Usage():
    return psutil.cpu_percent(interval= 0.1)

def Get_CPU_Base_Freq():
    return str(round(float(cpuinfo.get_cpu_info()["hz_advertised_friendly"].replace(" GHz", "")), 2)) + " GHz"

def Get_CPU_Architecture():
    return cpuinfo.get_cpu_info()["arch"]

def Get_System_Uptime():
    TimeSinceBootSeconds = int(time.time()) - int(psutil.boot_time())
    TimeSinceBootReadable = datetime.timedelta(seconds = TimeSinceBootSeconds)
    return TimeSinceBootReadable

def Get_Memory_Info():
    #total, free, used, util%
    Memory = psutil.virtual_memory()
    return str(round(Memory.total / 1024 / 1024 / 1024, 2)) + " " + "GB", str(round(Memory.used / 1024 / 1024 / 1024, 2)) + " " + "GB", str(round(Memory.free / 1024 / 1024 / 1024, 2)) + " " + "GB", Memory.percent