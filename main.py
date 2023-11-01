import PySimpleGUI as sg
from layouts import *


window = sg.Window('System Monitor', layout, size = (600, 600), background_color = WindowBackgroundColor, icon = "icon.ico", element_justification = "center")

layout = "CPUL"

while True:
    
    event, values = window.read(timeout = 1000)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "CPU":
        window[layout].update(visible = False)
        layout = "CPUL"
        window[layout].update(visible = True)
    if event == "Memory":
        window[layout].update(visible = False)
        layout = "MemoryL"
        window[layout].update(visible = True)
    if event == "GPU":
        window[layout].update(visible = False)
        layout = "GPUL"
        window[layout].update(visible = True)
    if event == "Storage":
        window[layout].update(visible = False)
        layout = "StorageL"
        window[layout].update(visible = True)
    if event == "Network":
        window[layout].update(visible = False)
        layout = "NetworkL"
        window[layout].update(visible = True)
        

window.close()