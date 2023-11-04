import PySimpleGUI as sg
from monitor import *

Gpu = Get_Nvidia_GPU_Info()
Drives = Get_Storage_Info()

def Navigation_Button(title):
    return sg.Button(title, size = (12,2), tooltip = title, border_width = 0)

def Component_Data_Layout(Title, Data):
    return [sg.Text(Title), sg.Push(), sg.Text(Data)]

def Component_Data_Layout_Dynamic(Title, Key):
    return [sg.Text(Title), sg.Push(), sg.Text("", key = Key)]

def Component_Data_Layout_ProgressBar(Title, ProgressBarKey, PercentKey):
    return [sg.Text(Title), sg.Push(), sg.ProgressBar(max_value= 100, orientation = "h",size_px = (380, 20), key = ProgressBarKey), sg.Text("", key = PercentKey)]

def Storage_Layout():
    layout = []
    TotalStorage = 0
    DriveNumber = 0
    for drive in Drives:
        TotalStorage += drive[1]
        layout.append(Component_Data_Layout("Drive", drive[0]))
        layout.append(Component_Data_Layout("Total Storage Capacity", str(round(drive[1] / 1024 / 1024 / 1024, 2)) + " GB"))
        layout.append(Component_Data_Layout_Dynamic("Used Storage", "-USED-STORAGE{}-".format(DriveNumber)))
        layout.append(Component_Data_Layout_Dynamic("Free Storage", "-FREE-STORAGE{}-" .format(DriveNumber)))
        layout.append([sg.HorizontalSeparator()])
        DriveNumber += 1
    layout.insert(0, Component_Data_Layout("Total Capacity(All Drives)", str(round(TotalStorage / 1024 / 1024 / 1024, 2)) + " GB"))
    layout.insert(1, [sg.HorizontalSeparator()])
    DriveNumber = 0
    for drive in Drives:
        layout.append(Component_Data_Layout_ProgressBar("{} Drive Usage".format(drive[0]), "-STORAGE-PROGRESS{}-".format(DriveNumber), "-STORAGE-PERCENT{}-".format(DriveNumber)))
        DriveNumber += 1
    return layout

def SettingsPopup():
    layout = [
        [sg.Text("List of themes.\nRESTART THE APP TO SEE THE CHANGES!")],
        [sg.Listbox(values = sg.theme_list(), size = (150, 11), key = "-THEME-LIST-", enable_events = True)],
        [sg.B("Confirm"),sg.B("Exit")]
    ]

    window = sg.Window("Settings", layout = layout, size = (300, 270), modal = True)
    
    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Confirm":
            theme = open("theme.py", "r")
            lines = theme.readlines()
            theme.close()
            theme = open("theme.py", "w")
            theme.truncate()
            theme.writelines(lines[:-1])
            theme.write("theme('{}')".format(values['-THEME-LIST-'][0]))
            break
    
    window.close()

ButtonLayout = [Navigation_Button("CPU"), Navigation_Button("Memory"), Navigation_Button("GPU"), Navigation_Button("Storage"), Navigation_Button("Network")]

GPULayout = []
GPULayout.append(Component_Data_Layout_ProgressBar("Load", "-GPU-LOAD-PROGRESS-", "-GPU-LOAD-PERCENT-"))
GPULayout.append([sg.HorizontalSeparator()])
GPULayout.append(Component_Data_Layout_ProgressBar("Memory Usage", "-GPU-MEMORY-PROGRESS-", "-GPU-MEMORY-PERCENT-"))

StorageLayout = Storage_Layout()

NavigationLayout = sg.Frame(
            title = "",
            layout = [ButtonLayout],
            relief = "flat",
            size = (600, 50),
            element_justification = "center"
            )

layoutCPU = [
    [   
        sg.Frame("", layout = [
            Component_Data_Layout("CPU", Get_CPU_Name()),
            [sg.HorizontalSeparator()],
            Component_Data_Layout("Physical CPU Cores", Get_CPU_Cores()),
            [sg.HorizontalSeparator()],
            Component_Data_Layout("Logical CPU Cores", Get_CPU_Cores(True)),
            [sg.HorizontalSeparator()],
            Component_Data_Layout("Base Frequency", Get_CPU_Base_Freq()),
            [sg.HorizontalSeparator()],
            Component_Data_Layout("Architecture", Get_CPU_Architecture())
        ],
        size = (555, 232))
    ],

    [
        sg.Frame("", layout = [
            Component_Data_Layout_ProgressBar("CPU Usage", "-CPU-PROGRESS-", "-CPU-PROGRESS-PERCENT-"),
            [sg.HorizontalSeparator()],
            Component_Data_Layout_Dynamic("System Uptime", "-UPTIME-")
        ],
        size = (555, 232))
    ]
]

layoutMemory = [
    [   
        sg.Frame("", layout = [
            Component_Data_Layout("Total Installed Memory", Get_Memory_Info()[0]),
            [sg.HorizontalSeparator()],
            Component_Data_Layout_Dynamic("Used Memory", "-USED-MEMORY-"),
            [sg.HorizontalSeparator()],
            Component_Data_Layout_Dynamic("Free Memory", "-FREE-MEMORY-"),
            [sg.HorizontalSeparator()],
            Component_Data_Layout_ProgressBar("Memory usage", "-MEMORY-PROGRESS-", "-MEMORY-PROGRESS-PERCENT-")
        ],
        size = (555, 464))
    ]
]

layoutGPU = [
    [   
        sg.Frame("", layout = [
            Component_Data_Layout("GPU", Gpu[0]),
            [sg.HorizontalSeparator()],
            Component_Data_Layout("Total Memory", Gpu[1]),
            [sg.HorizontalSeparator()],
            Component_Data_Layout_Dynamic("Used Memory", "-GPU-USED-MEMORY-"),
            [sg.HorizontalSeparator()],
            Component_Data_Layout_Dynamic("Free Memory", "-GPU-FREE-MEMORY-")
        ],
        size = (555, 232))
    ],

    [
        sg.Frame("", layout = GPULayout,
        size = (555, 232))
    ]
]

layoutStorage = [
    [   
        sg.Frame("", 
        layout = 
            StorageLayout
        ,
        size = (555, 464))
    ]
]

layoutNetwork = [
    [   
        sg.Frame("", layout = [
            
        ],
        size = (555, 232))
    ],

    [
        sg.Frame("", layout = [
            
        ],
        size = (555, 232))
    ]
]

layout = [
    [
        NavigationLayout
    ],

    [
        sg.Column(layoutCPU, key = 'CPUL', size = (600, 480)), 
        sg.Column(layoutMemory, key = "MemoryL", visible = False, size = (600, 480)), 
        sg.Column(layoutGPU, key = "GPUL", visible = False, size = (600, 480)),
        sg.Column(layoutStorage, key = "StorageL", visible = False, size = (600, 480)), 
        sg.Column(layoutNetwork, key = "NetworkL", visible = False, size = (600, 480))
    ],

    [
        sg.Frame("", layout = [
            [
                sg.B("", image_filename = "images/github.png", image_size = (30, 30), border_width = 0, button_color = sg.theme_element_background_color(), mouseover_colors = sg.theme_element_background_color(), key = "-github-"),
                sg.B("", image_filename = "images/settings.png", image_size = (30, 30), border_width = 0, button_color = sg.theme_element_background_color(), mouseover_colors = sg.theme_element_background_color(), key = "-settings-"),
                sg.B("", image_filename = "images/exit.png", image_size = (30, 30), border_width = 0, button_color = sg.theme_element_background_color(), mouseover_colors = sg.theme_element_background_color(), key='-exit-')
            ]
        ],
        size = (600, 50),
        relief="flat",
        element_justification="right")
    ]
]