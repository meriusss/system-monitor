import PySimpleGUI as sg

WindowBackgroundColor = "#9BBEC8"
ButtonColor = "#427D9D"
ButtonColorActive = "#195170"

def Navigation_Button(title):
    return sg.Button(title, size = (12,2), tooltip = title, button_color = ("#FFFFFF", ButtonColor) , mouseover_colors = "#164863", border_width = 0)

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
    [sg.Text("CPU")]
]

layoutMemory = [
    [sg.Text("Memory")]
]

layoutGPU = [
    [sg.Text("GPU")]
]

layoutStorage = [
    [sg.Text("Storage")]
]

layoutNetwork = [
    [sg.Text("Network")]
]

layout = [
    [
        NavigationLayout
    ],

    [
        sg.Column(layoutCPU, key = 'CPUL', size = (600, 475)), 
        sg.Column(layoutMemory, key = "MemoryL", visible = False, size = (600, 475)), 
        sg.Column(layoutGPU, key = "GPUL", visible = False, size = (600, 475)), 
        sg.Column(layoutStorage, key = "StorageL", visible = False, size = (600, 475)), 
        sg.Column(layoutNetwork, key = "NetworkL", visible = False, size = (600, 475))
    ],

    [
        sg.Frame("", layout = [
            [
                sg.B("", image_filename = "images/github.png", image_size = (26, 26), border_width = 0, button_color = WindowBackgroundColor, mouseover_colors = WindowBackgroundColor, key = "-github-"),
                sg.B("", image_filename = "images/settings.png", image_size = (26, 26), border_width = 0, button_color = WindowBackgroundColor, mouseover_colors = WindowBackgroundColor, key = "-settings-"),
                sg.B("", image_filename = "images/exit.png", image_size = (26, 26), border_width = 0, button_color = WindowBackgroundColor, mouseover_colors = WindowBackgroundColor, key='-exit-')
            ]
        ],
        size = (600, 50),
        relief="flat",
        background_color= WindowBackgroundColor,
        element_justification="right")
    ]
]