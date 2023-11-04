from layout_functions import *
from monitor import *

Gpu = Get_Nvidia_GPU_Info()

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
        sg.Frame("", 
        layout = [Component_Data_Layout_ProgressBar("Load", "-GPU-LOAD-PROGRESS-", "-GPU-LOAD-PERCENT-"),
                [sg.HorizontalSeparator()], 
                Component_Data_Layout_ProgressBar("Memory Usage", "-GPU-MEMORY-PROGRESS-", "-GPU-MEMORY-PERCENT-")],
        size = (555, 232))
    ]
]

layoutStorage = [
    [   
        sg.Frame("", 
        layout = 
            Storage_Layout(Get_Storage_Info())
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