import PySimpleGUI as sg
from monitor import *

WindowBackgroundColor = "#9BBEC8"
ButtonColor = "#427D9D"
ButtonColorActive = "#195170"
ButtonTextColor = "#FFFFFF"

def Navigation_Button(title):
    return sg.Button(title, size = (12,2), tooltip = title, border_width = 0)

def Component_Data_Layout(Title, Data):
    return [sg.Text(Title), sg.Push(), sg.Text(Data)]

def Component_Data_Layout_Dynamic(Title, Key):
    return [sg.Text(Title), sg.Push(), sg.Text("", key = Key)]

def Component_Data_Layout_ProgressBar(Title, ProgressBarKey, PercentKey):
    return [sg.Text(Title), sg.Push(), sg.ProgressBar(max_value= 100, orientation = "h",size_px = (380, 20), key = ProgressBarKey), sg.Text("", key = PercentKey)]

ButtonLayout = [Navigation_Button("CPU"), Navigation_Button("Memory"), Navigation_Button("GPU"), Navigation_Button("Storage"), Navigation_Button("Network")]

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
            Component_Data_Layout("Physical CPU Cores", Get_CPU_Cores()),
            Component_Data_Layout("Logical CPU Cores", Get_CPU_Cores(True)),
            Component_Data_Layout("Base Frequency", Get_CPU_Base_Freq()),
            Component_Data_Layout("Architecture", Get_CPU_Architecture())
        ],
        size = (555, 232))
    ],

    [
        sg.Frame("", layout = [
            Component_Data_Layout_ProgressBar("CPU Usage", "-CPU-PROGRESS-", "-CPU-PROGRESS-PERCENT-"),
            Component_Data_Layout_Dynamic("System Uptime", "-UPTIME-")
        ],
        size = (555, 232))
    ]
]

layoutMemory = [
    [   
        sg.Frame("", layout = [
            Component_Data_Layout("Total Installed Memory", Get_Memory_Info()[0]),
            Component_Data_Layout_Dynamic("Used Memory", "-USED-MEMORY-"),
            Component_Data_Layout_Dynamic("Free Memory", "-FREE-MEMORY-"),
            Component_Data_Layout_ProgressBar("Memory usage", "-MEMORY-PROGRESS-", "-MEMORY-PROGRESS-PERCENT-")
        ],
        size = (555, 464))
    ]
]

layoutGPU = [
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

layoutStorage = [
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