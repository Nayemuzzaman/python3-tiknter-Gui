import tkinter as tk
from tkinter import ttk

def clicked():
    print("Button clicked")

def hitReturn(*args):
    print("user pressed return")


root = tk.Tk()
root.title("GUI Tabs")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")

ent1t1 = tk.Entry(tab1)
ent1t1.pack()
ent1t1.bind("<Return>", hitReturn)

btn1t2 = tk.Button(tab2, text="Button 2", command=lambda:clicked)
btn1t2.pack()

root.mainloop()