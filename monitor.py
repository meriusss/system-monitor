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

def Get_Total_Available_Memory(unit):
    if unit == "GB":
        return str(round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)) + " " + unit
    elif unit == "MB":
        return str(round(psutil.virtual_memory().total / 1024 / 1024)) + " " + unit
    else: 
        return str(round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)) + " " + unit