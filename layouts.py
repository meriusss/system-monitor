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
            background_color = WindowBackgroundColor
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
    [NavigationLayout],

    [
    sg.Column(layoutCPU, key = 'CPUL'), 
    sg.Column(layoutMemory, key = "MemoryL", visible = False), 
    sg.Column(layoutGPU, key = "GPUL", visible = False), 
    sg.Column(layoutStorage, key = "StorageL", visible = False), 
    sg.Column(layoutNetwork, key = "NetworkL", visible = False)
    ]
]