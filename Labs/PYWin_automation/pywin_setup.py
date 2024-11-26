import win32com.client
import win32gui

print("windows version :", win32api.GetVersion())
print("Computer Name :", win32api.GetComputerName())
print("system Metrics:", win32api.GetSystemMetrices(0))


def custom_message_box():
    result = win32gui.MessageBox(0,"Do you like python?","Cutsome question",1)
    print(result)
    if(result==1):
        win32gui.MessageBox(0,str(result),"your Output",1)

custom_message_box()