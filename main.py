from webbrowser import open
import theme
from layouts import *

window = sg.Window('System Monitor', layout, size = (600, 600), icon = "images/icon.ico", element_justification = "center", no_titlebar = False, grab_anywhere = True)

layout = "CPUL"

def Change_Layout(LayoutToChangeTo):
    global layout
    window[layout].update(visible = False)
    layout = LayoutToChangeTo
    window[layout].update(visible = True)

while True:
    
    event, values = window.read(timeout = 1000)

    if event == sg.WIN_CLOSED or event == 'Exit' or event == "-exit-":
        break
    if event == "-github-":
        open("https://github.com/meriusss/system-monitor", new = 2)
    if event == "-settings-":
        SettingsPopup()
    if event == "CPU":
        Change_Layout("CPUL")
    if event == "Memory":
        Change_Layout("MemoryL")
    if event == "GPU":
        Change_Layout("GPUL")
    if event == "Storage":
        Change_Layout("StorageL")
    if event == "Network":
        Change_Layout("NetworkL")

    CPUUsage = Get_CPU_Usage()
    Uptime = Get_System_Uptime()
    Memory = Get_Memory_Info()
    Gpu = Get_Nvidia_GPU_Info()
    Drives = Get_Storage_Info()
    if Gpu[5] < 10:
        GpuPercent = "0" + str(Gpu[5]) + "%"
    else: GpuPercent = str(Gpu[5]) + "%"

    window["-CPU-PROGRESS-"].UpdateBar(current_count = CPUUsage)
    window["-CPU-PROGRESS-PERCENT-"].update(str(CPUUsage) + "%")
    window["-UPTIME-"].update(Uptime)
    window["-USED-MEMORY-"].update(Memory[1])
    window["-FREE-MEMORY-"].update(Memory[2])
    window["-MEMORY-PROGRESS-"].UpdateBar(current_count = Memory[3])
    window["-MEMORY-PROGRESS-PERCENT-"].update(str(Memory[3]) + "%")
    window["-GPU-USED-MEMORY-"].update(Gpu[2])
    window["-GPU-FREE-MEMORY-"].update(Gpu[3])
    window["-GPU-LOAD-PROGRESS-"].UpdateBar(current_count = Gpu[5])
    window["-GPU-LOAD-PERCENT-"].update(GpuPercent)
    window["-GPU-MEMORY-PROGRESS-"].UpdateBar(current_count = Gpu[4])
    window["-GPU-MEMORY-PERCENT-"].update(Gpu[4] + "%")
    
    DriveNumber = 0

    for drive in Drives:
        window["-USED-STORAGE{}-".format(DriveNumber)].update(str(round(drive[2] / 1024 / 1024 / 1024, 2)))
        window["-FREE-STORAGE{}-".format(DriveNumber)].update(str(round(drive[3] / 1024 / 1024 / 1024, 2)))
        window["-STORAGE-PROGRESS{}-".format(DriveNumber)].UpdateBar(current_count = drive[4])
        window["-STORAGE-PERCENT{}-".format(DriveNumber)].update(str(drive[4]) + "%")
        DriveNumber += 1
        
window.close()