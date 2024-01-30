import PySimpleGUI as sg
import json
from os import path
import monitor

class Layout:
    def __init__(self) -> None:
        self.Load_Theme()
        self.imagesPath = path.abspath(path.dirname(__file__)) + "/images"
        self.cpuLayout = [
            [   
            sg.Frame("", layout = 
            [
            self.Component_Data_Layout("CPU", "-cpu-name-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Physical CPU Cores", "-cpu-cores-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Logical CPU Cores", "-logical-cpu-cores-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Base Frequency", "-cpu-base-frequency-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Architecture", "-cpu-architecture-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout_ProgressBar("CPU Usage", "-CPU-"),
            ],
            size = (555, 232))
            ],

            [
            sg.Frame("", layout = [
            self.Component_Data_Layout("OS", "-os-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("OS Version", "-os-version-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("System Uptime", "-UPTIME-")
            ],
            size = (555, 232))]
        ]

        self.GPU_Layout()

        self.memoryLayout = [
            [   
            sg.Frame("", layout = [
            self.Component_Data_Layout("Total Installed Memory", "-total-memory-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Used Memory", "-USED-MEMORY-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Free Memory", "-FREE-MEMORY-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout_ProgressBar("Memory usage", "-MEMORY-")
            ],
            size = (555, 464))
            ]
        ]

        self.Storage_Layout()

        self.Graph_Layout()

        self.navigationLayout = [
            self.Navigation_Button("CPU/System"), 
            self.Navigation_Button("Memory"), 
            self.Navigation_Button("GPU"), 
            self.Navigation_Button("Storage"), 
            self.Navigation_Button("Graphs")
        ]

        self.mainLayout = [
            sg.Column(self.cpuLayout, key = '-cpu-layout-', size = (600, 480)), 
            sg.Column(self.memoryLayout, key = "-memory-layout-", visible = False, size = (600, 480)), 
            sg.Column(self.gpuLayout, key = "-gpu-layout-", visible = False, size = (600, 480)),
            sg.Column(self.storageLayout, key = "-storage-layout-", visible = False, size = (600, 480)), 
            sg.Column(self.graphsLayout, key = "-graphs-layout-", visible = False, size = (600, 480))
        ]

        self.footerLayout = sg.Frame("",layout = [[
            self.Footer_Button("{}/github.png".format(self.imagesPath), "-github-"),
            self.Footer_Button("{}/settings.png".format(self.imagesPath), "-settings-"),
            self.Footer_Button("{}/exit.png".format(self.imagesPath), "-exit-")
            ]],
            size = (600, 50),
            relief = "flat",
            element_justification = "right")

        self.layout = [
            [self.navigationLayout],
            [self.mainLayout],
            [self.footerLayout]
        ]

    def GPU_Layout(self):
        gpu = monitor.GPU()
        if gpu.gpu != "Unknown GPU":
            self.gpuLayout = [
            [   
            sg.Frame("", layout = [
            self.Component_Data_Layout("GPU", "-gpu-name-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Total Memory", "-gpu-total-memory-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Used Memory", "-GPU-USED-MEMORY-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Free Memory", "-GPU-FREE-MEMORY-"),
            [sg.HorizontalSeparator()],
            self.Component_Data_Layout("Temperature", "-GPU-TEMPERATURE-")
            ],
            size = (555, 232))
            ],

            [
            sg.Frame("", 
            layout = [
                self.Component_Data_Layout_ProgressBar("Load", "-GPU-LOAD-"),
                [sg.HorizontalSeparator()], 
                self.Component_Data_Layout_ProgressBar("Memory Usage", "-GPU-MEMORY-")],
            size = (555, 232))
            ]
            ]
        else:
            self.gpuLayout = [
            [
            sg.Frame("",
            layout= [
                [sg.Text(gpu.gpu)]],
            size=(555, 58),
            element_justification="center")
            ]
            ]

    def Storage_Layout(self):
        Drives = monitor.Storage.get_drives()
        layout = []
        DriveNumber = 0
        for drive in Drives:
            layout.append(self.Component_Data_Layout("Drive", f"-drive{DriveNumber}-"))
            layout.append(self.Component_Data_Layout("Total Storage Capacity", f"-drive{DriveNumber}-capacity-"))
            layout.append(self.Component_Data_Layout("Used Storage", f"-USED-STORAGE{DriveNumber}-"))
            layout.append(self.Component_Data_Layout("Free Storage", f"-FREE-STORAGE{DriveNumber}-" ))
            layout.append([sg.HorizontalSeparator()])
            DriveNumber += 1
        layout.insert(0, self.Component_Data_Layout("Total Capacity(All Drives)", "-total-storage-"))
        layout.insert(1, [sg.HorizontalSeparator()])

        DriveNumber = 0
        for drive in Drives:
            layout.append(self.Component_Data_Layout_ProgressBar(f"{drive[0]} Drive Usage", f"-STORAGE-{DriveNumber}-"))
            DriveNumber += 1
        self.storageLayout = [[sg.Frame("", layout = layout, size = (555, 464))]]

    def Load_Theme(self):
        themefile = path.abspath(path.dirname(__file__)) + "/theme.json"
        with open(themefile ,"r") as file:
            self.theme = json.load(file)["theme"]
            sg.theme(self.theme)
    
    def Graph_Layout(self):
        GRAPH_SIZE = (540, 200)

        self.graphsLayout = [
            [sg.Text("Memory usage graph")],
            [sg.Push(), sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key = "-memory-graph-", background_color=sg.theme_button_color_background()), sg.Push()],
            [sg.Text("60 seconds")],
            [sg.HorizontalSeparator()]
        ]

    @staticmethod
    def Navigation_Button(Title):
        return sg.Button(Title, size = (12,2), tooltip = Title, border_width = 0)
    
    @staticmethod
    def Footer_Button(ImageSource, Key):
        return sg.B("", image_filename = ImageSource, image_size = (30, 30), border_width = 0, button_color= sg.theme_element_background_color(), mouseover_colors= sg.theme_element_background_color(), key = Key)
    
    @staticmethod
    def Component_Data_Layout(Title, Key):
        return [sg.Text(Title), sg.Push(), sg.Text("", key = Key)]
    
    @staticmethod
    def Component_Data_Layout_ProgressBar(Title, Key):
        return [sg.Text(Title), sg.Push(), sg.ProgressBar(max_value= 100, orientation = "h",size_px = (380, 20), key = Key + "BAR-"), sg.Text("", key = Key + "PERCENT-")]