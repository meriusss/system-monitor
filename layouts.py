import PySimpleGUI as sg
from monitor import *

WindowBackgroundColor = "#9BBEC8"
ButtonColor = "#427D9D"
ButtonColorActive = "#195170"
ButtonTextColor = "#FFFFFF"

def Navigation_Button(title):
    return sg.Button(title, size = (12,2), tooltip = title, button_color = (ButtonTextColor, ButtonColor) , mouseover_colors = "#164863", border_width = 0)

def Component_Data_Layout(Title, Data):
    return [sg.Text(Title), sg.Push(), sg.Text(Data)]

ButtonLayout = [Navigation_Button("CPU"), Navigation_Button("Memory"), Navigation_Button("GPU"), Navigation_Button("Storage"), Navigation_Button("Network")]

NavigationLayout = sg.Frame(
            title = "",
            layout = [ButtonLayout],
            relief = "flat",
            background_color = WindowBackgroundColor,
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
            [
                sg.Text("CPU Usage"),
                sg.Push(),
                sg.ProgressBar(max_value= 100, orientation = "h",size_px = (400, 20), key = "-CPU-PROGRESS-", bar_color= (ButtonColorActive, WindowBackgroundColor), style="clam"),
                sg.Text("", key = "-CPU-PROGRESS-PERCENT-")
            ],
            [   
                sg.Text("System Uptime"),
                sg.Push(),
                sg.Text("", key = "-UPTIME-")
            ]
        ],
        size = (555, 232))
    ]
]

layoutMemory = [
    [   
        sg.Frame("", layout = [
            Component_Data_Layout("Total Available Memory", Get_Total_Available_Memory("GB"))
        ],
        size = (555, 232))
    ],

    [
        sg.Frame("", layout = [
            
        ],
        size = (555, 232))
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
                sg.B("", image_filename = "images/github.png", image_size = (30, 30), border_width = 0, button_color = WindowBackgroundColor, mouseover_colors = WindowBackgroundColor, key = "-github-"),
                sg.B("", image_filename = "images/settings.png", image_size = (30, 30), border_width = 0, button_color = WindowBackgroundColor, mouseover_colors = WindowBackgroundColor, key = "-settings-"),
                sg.B("", image_filename = "images/exit.png", image_size = (30, 30), border_width = 0, button_color = WindowBackgroundColor, mouseover_colors = WindowBackgroundColor, key='-exit-')
            ]
        ],
        size = (600, 50),
        relief="flat",
        background_color= WindowBackgroundColor,
        element_justification="right")
    ]
]