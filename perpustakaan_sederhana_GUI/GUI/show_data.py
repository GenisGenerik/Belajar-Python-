from tkinter import ttk
import tkinter as tk
from Data.variabel import data
def show_data(frame1:ttk.Frame,isi:list[str]) :
    iterrow = 0
    for i in isi :
        itercol = 0
        split = i.split(",")
        data.append(split)
        for j in split :
            dat = tk.Label(frame1,text=j)
            dat.grid(row=2+iterrow,column=itercol,padx=30)
                
            itercol+=1
                
        iterrow+=1