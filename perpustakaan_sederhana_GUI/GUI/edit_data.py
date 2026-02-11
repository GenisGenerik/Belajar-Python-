import tkinter as tk
from tkinter import ttk
from Data.variabel import data,head,inputan
from Data.edit_data import edit_data


def edit(frame1:ttk.Frame,id:int)->None :
    t_data = tk.Toplevel()
    t_data.geometry("300x300")
    t_data.title("edit data")
    frame2 = ttk.Frame(t_data)
    frame2.pack(fill="x")
    
    data_ubah = data[id].copy()


    count = 1
    for i in head[1:-1]  :
        isi = data_ubah[count]
        var = tk.StringVar(value=isi)
        label = tk.Label(frame2,text=i)
        label.pack(anchor='w',padx=10,pady=10)
        im = tk.Entry(frame2,textvariable=var) 
        im.pack(anchor='w',padx=10,pady=10)
        inputan.append(im)
        count+=1
    button_simpan =tk.Button(frame2,text="Simpan",command=lambda : edit_data(t_data,id,frame1))
    button_simpan.pack(anchor='w',padx=10,pady=10)