import PySimpleGUI as sg
from layouts import *
from webbrowser import open

window = sg.Window('System Monitor', layout, size = (600, 600), background_color = WindowBackgroundColor, icon = "images/icon.ico", element_justification = "center", no_titlebar = False, grab_anywhere = True)

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
        pass
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

    window["-CPU-PROGRESS-"].UpdateBar(current_count = CPUUsage)
    window["-CPU-PROGRESS-PERCENT-"].update(str(CPUUsage) + "%")
    window["-UPTIME-"].update(Uptime)
        
window.close()