import tkinter as tk
from tkinter import ttk
from Data.variabel import head,label
from GUI.tambah_data import tambah_data
def header(frame1:ttk.Frame) ->None :
    iter =0 
    for i in head :

        lab = tk.Label(frame1,text=i)
        lab.grid(row=0,column=iter,padx=20)
        label.append(lab)
        iter+=1

    lab = tk.Button(frame1,text="Tambah Data",command=lambda :tambah_data(frame1) )
    lab.grid(row=0,column=iter+1,padx=20)
    label.append(lab)
    lab = tk.Label(frame1,text="=================================================")
    lab.grid(row=1,column=0,columnspan=5)