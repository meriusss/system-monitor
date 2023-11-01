import psutil
import cpuinfo

def Get_CPU_Name():
    return cpuinfo.get_cpu_info()['brand_raw']

def Get_CPU_Cores(logical = False):
    return psutil.cpu_count(logical)

def Get_CPU_Usage():
    return psutil.cpu_percent(interval= None)
