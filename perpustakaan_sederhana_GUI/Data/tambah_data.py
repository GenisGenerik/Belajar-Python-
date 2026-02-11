from Data.variabel import inputan,data
from GUI.clear import clear_data,frame_destroy
from tkinter import ttk
import tkinter as tk
from GUI.variabel import frame_body

def simpan()->str :
    data_baru:str =""
    for i in inputan :
        data_baru+=i.get()
        data_baru+=","
    return data_baru[:-1]

def simpan_data(frame2:tk.Toplevel,frame1:ttk.Frame)->None :
    from GUI.body import body
    id_baru = len(data) + 1
    if all(x =="," for x in simpan()) : print("Iya kosong")
    else :
        data_baru = str(id_baru) +"," + simpan()

        
        with open('Data/data.txt', 'a+') as file:
            file.seek(0)
            isi = file.read()
            if isi:
                file.write('\n')
            file.write(data_baru)

    clear_data()
    frame_destroy(frame2)
    body(frame_body)
    
  


    