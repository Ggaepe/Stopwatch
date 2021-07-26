import threading 
import time 
import tkinter as tk 
from tkinter import ttk 

def timerFunction():
    time.sleep(1)
    global winLabel

    hour = 0 
    minute = 0
    second = 0
    while True:
        winLabel.configure(text=str(hour) + ":" + str(minute) + ":" + str(second)) #시간 표시
        time.sleep(1)
        second += 1

        if second >= 60:
            minute += 1
            second = 0
        if minute >= 60:
            hour += 1
            minute = 0

def main():
    mainWindow = tk.Tk() 
    mainWindow.title("Timer") 
    mainWindow.geometry("220x35") #창 넓이
    mainWindow.resizable(True, True) 

    global winLabel 
    winLabel = ttk.Label(mainWindow, text=" ")
    winLabel.grid(column=0, row=0) 

    timer = threading.Thread(target=timerFunction)
    timer.daemon = True
    timer.start() 

    mainWindow.mainloop() #def main 부분 반복

main()
