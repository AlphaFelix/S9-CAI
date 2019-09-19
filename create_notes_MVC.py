from modules.Model import Model
from modules.Screen import Screen
from modules.Controller import Controller
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    root.resizable(False, False)
    root.title('Generate Notes')
    root.geometry('900x800')

    model   = Model()
    view    = Screen(root)
    ctrl    = Controller(model, view)
    
    root.mainloop()