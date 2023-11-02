import psutil
import cpuinfo

def Get_CPU_Name():
    return cpuinfo.get_cpu_info()['brand_raw']

def Get_CPU_Cores(logical = False):
    return psutil.cpu_count(logical)

def Get_CPU_Usage():
    return psutil.cpu_percent(interval= None)

def Get_CPU_Base_Freq():
    return cpuinfo.get_cpu_info()["hz_advertised_friendly"]

def Get_CPU_Architecture():
    return cpuinfo.get_cpu_info()["arch"]

def Get_Total_Available_Memory(unit):
    if unit == "GB":
        return str(round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)) + " " + unit
    elif unit == "MB":
        return str(round(psutil.virtual_memory().total / 1024 / 1024)) + " " + unit
    else: 
        return str(round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)) + " " + unit