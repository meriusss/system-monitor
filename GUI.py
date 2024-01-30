from layout import *
import webbrowser
import monitor
import json
from os import path

class GUI:
    def __init__(self, layout: Layout):
        self.layout = layout.layout
        self.theme = layout.theme
        self.window = sg.Window('System Monitor', self.layout, size = (600, 600), icon = "{}/icon.ico".format(path.abspath(path.dirname(__file__)) + "/images"), element_justification = "center", grab_anywhere = True)
        self.isLooping = True
        self.cpu = monitor.CPU()
        self.system = monitor.System()
        self.memory = monitor.Memory()
        self.gpu = monitor.GPU()
        self.storage = monitor.Storage.get_drives()
        self.layoutDictionary = {
            "CPU/System":"-cpu-layout-",
            "Memory":"-memory-layout-",
            "GPU":"-gpu-layout-",
            "Storage":"-storage-layout-",
            "Graphs":"-graphs-layout-"
        }
        self.footerDictionary = {
            "-settings-": self.open_settings_window,
            "-github-": self.open_github
        }
        self.currentLayout = "-cpu-layout-"
        self.graphX = 0
        self.graphY = 0
        self.lastGraphX = 0
        self.lastGraphY = 0
        self.graphStepSize = 9

    @staticmethod
    def open_github():
        webbrowser.open("https://github.com/meriusss/system-monitor", 2)

    def open_settings_window(self):
        layout = [
        [sg.Text("List of themes.\nRESTART THE APP TO SEE THE CHANGES!")],
        [sg.Text(f"Current theme:  {self.theme}")],
        [sg.Listbox(values = sg.theme_list(), size = (150, 11), key = "-THEME-LIST-", enable_events = True)],
        [sg.B("Confirm"),sg.B("Exit")]
    ]
        themefile = path.abspath(path.dirname(__file__)) + "/theme.json"
        window = sg.Window("Settings", layout = layout, size = (300, 300), modal = True)
        
        while True:
            event, values = window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Confirm":
                if values["-THEME-LIST-"] != []:
                    with open(themefile, "r") as file:
                        theme = json.load(file)
                        file.close()
                    theme["theme"] = values["-THEME-LIST-"][0]
                    with open(themefile, "w") as file:
                        file.write(json.dumps(theme))
                        file.close()
                    break
                else: 
                    break
        window.close()

    def change_layout(self, LayoutToChangeTo):
        self.window[self.currentLayout].update(visible = False)
        self.currentLayout = LayoutToChangeTo
        self.window[self.currentLayout].update(visible = True)

    def handle_events(self):
        if self.event in ("Cancel", "Exit", "-exit-", sg.WINDOW_CLOSED):
            self.isLooping = False
        elif self.event in self.layoutDictionary:
            self.change_layout(self.layoutDictionary[self.event])
        elif self.event in self.footerDictionary:
            self.footerDictionary[self.event]()

    def initialize_window(self):
        constantDictionary = {
            "-cpu-name-":self.cpu.name, 
            "-cpu-cores-":self.cpu.cores, 
            "-logical-cpu-cores-":self.cpu.logical_cores, 
            "-cpu-base-frequency-":f"{self.cpu.base_frequency} GHz", 
            "-cpu-architecture-":self.cpu.architecture,
            "-os-": f"{self.system.name} {self.system.release}",
            "-os-version-":self.system.version,
            "-total-memory-":f"{self.memory.total} GB",
            }
        
        if self.gpu.gpu != "Unknown GPU":
            gpuDictionary = {
                "-gpu-name-": self.gpu.name,
                "-gpu-total-memory-": f"{self.gpu.total_memory} GB"
            }
            constantDictionary.update(gpuDictionary)

        totalStorage = 0

        for drive in self.storage:
            index = self.storage.index(drive)
            constantDictionary.update({f"-drive{index}-": drive[0],
                                       f"-drive{index}-capacity-": f"{drive[1]} GB"})
            totalStorage += drive[1]
        
        constantDictionary.update({"-total-storage-":f"{round(totalStorage, 2)} GB"})

        self.window.finalize()
        
        for key in constantDictionary:
            self.window[key].update(constantDictionary[key])

    def update_window(self):
        cpuUsage = self.cpu.get_usage()
        uptime = self.system.get_uptime()
        usedMemory = self.memory.get_used_memory()
        freeMemory = self.memory.get_free_memory()
        memoryUsage = self.memory.get_memory_usage()
        storage = monitor.Storage.get_drives()
        
        dynamicDictionary = {
            "-CPU-BAR-": cpuUsage,
            "-CPU-PERCENT-": f"{cpuUsage} %",
            "-UPTIME-": uptime,
            "-USED-MEMORY-": f"{usedMemory} GB",
            "-FREE-MEMORY-": f"{freeMemory} GB",
            "-MEMORY-BAR-": memoryUsage,
            "-MEMORY-PERCENT-": f"{memoryUsage} %"
        }
        if self.gpu.gpu != "Unknown GPU":
            self.gpu = monitor.GPU()
            gpuUsedMemory = self.gpu.get_used_memory()
            gpuFreeMemory = self.gpu.get_free_memory()
            gpuMemoryUsage = self.gpu.get_memory_usage()
            gpuLoad = self.gpu.get_load()
            gpuTemp = self.gpu.get_temperature()
            gpuDictionary = {
                "-GPU-USED-MEMORY-":f"{gpuUsedMemory} GB",
                "-GPU-FREE-MEMORY-":f"{gpuFreeMemory} GB",
                "-GPU-LOAD-BAR-": gpuLoad,
                "-GPU-LOAD-PERCENT-":f"{gpuLoad} %",
                "-GPU-MEMORY-BAR-":gpuMemoryUsage,
                "-GPU-MEMORY-PERCENT-":f"{gpuMemoryUsage} %",
                "-GPU-TEMPERATURE-":f"{gpuTemp} °C"
            }
            dynamicDictionary.update(gpuDictionary)

        for drive in storage:
            index = storage.index(drive)
            dynamicDictionary.update({f"-USED-STORAGE{index}-": f"{drive[2]} GB",
                                      f"-FREE-STORAGE{index}-": f"{drive[3]} GB",
                                      f"-STORAGE-{index}-BAR-": drive[4],
                                      f"-STORAGE-{index}-PERCENT-": f"{drive[4]} %"})
            
        for key in dynamicDictionary:
            self.window[key].update(dynamicDictionary[key])

        if self.graphX < 540:
            self.window["-memory-graph-"].DrawLine((self.lastGraphX, self.lastGraphY,), (self.graphX, memoryUsage * 2), width=2)
        else:
            self.window["-memory-graph-"].Move(-self.graphStepSize, 0)
            self.window["-memory-graph-"].DrawLine((self.lastGraphX, self.lastGraphY,), (self.graphX, memoryUsage * 2), width=2)
            self.graphX = self.graphX - self.graphStepSize
        self.lastGraphX, self.lastGraphY = (self.graphX, memoryUsage * 2)
        self.graphX += self.graphStepSize

        

    def main_loop(self):
        self.initialize_window()
        while self.isLooping:
            self.event, self.values = self.window.read(timeout = 1000)
            self.handle_events()
            self.update_window()

        self.window.close()