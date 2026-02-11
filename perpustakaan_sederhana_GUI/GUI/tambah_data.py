import tkinter as tk
from tkinter import ttk
from Data.variabel import head,inputan
from Data.tambah_data import simpan_data


def tambah_data(frame1:ttk.Frame) :
    t_data = tk.Toplevel()
    t_data.geometry("300x300")
    t_data.title("Tambah Data")
    frame2 = ttk.Frame(t_data)
    frame2.pack(fill="x")
    
    
    for i in head[1:-1]  :
        label = tk.Label(frame2,text=i)
        label.pack(anchor='w',padx=10,pady=10)
        im = tk.Entry(frame2) 
        im.pack(anchor='w',padx=10,pady=10)
        inputan.append(im)
    button_simpan =tk.Button(frame2,text="Simpan",command=lambda : simpan_data(t_data,frame1))
    button_simpan.pack(anchor='w',padx=10,pady=10)


    
