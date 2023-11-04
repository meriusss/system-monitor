import PySimpleGUI as sg

def Navigation_Button(title):
    return sg.Button(title, size = (12,2), tooltip = title, border_width = 0)

def Component_Data_Layout(Title, Data):
    return [sg.Text(Title), sg.Push(), sg.Text(Data)]

def Component_Data_Layout_Dynamic(Title, Key):
    return [sg.Text(Title), sg.Push(), sg.Text("", key = Key)]

def Component_Data_Layout_ProgressBar(Title, ProgressBarKey, PercentKey):
    return [sg.Text(Title), sg.Push(), sg.ProgressBar(max_value= 100, orientation = "h",size_px = (380, 20), key = ProgressBarKey), sg.Text("", key = PercentKey)]

def Storage_Layout(Drives):
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
