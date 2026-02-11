from Data.variabel import inputan
import tkinter as tk
from tkinter import ttk
from GUI.variabel import frame_body
from GUI.clear import clear_data,frame_destroy

def simpan()->str :
    data_baru:str =""
    for i in inputan :
        data_baru+=i.get()
        data_baru+=","
    return data_baru[:-1]


def update_id (isi:list[str]) ->list[str] :
    
    count = 1
    hasil:list[str] = []
    for i in isi :
        split = i.split(",")
        split[0] = str(count)
        count+=1
        hasil.append(gabung(split))


    return hasil

def gabung(split:list[str])->str :
    data_baru:str =""
    for i in split :
        data_baru += i + ","
    return data_baru[:-1]

def edit_data(frame2:tk.Toplevel,id:int,frame1:ttk.Frame)->None :
    
    from GUI.body import body
    read:list[str] = []
    cek:list[str]=[]
    
    if all(x =="," for x in simpan()) : print("Iya kosong")
    else :
        data_baru = str(id+1) +"," + simpan()
        with open('Data/data.txt','r') as file :
            read = file.readlines()
        cek =  read.copy()
       
        cek[id] = data_baru 
        if id != len(cek)-1 :
            cek[id]+='\n'

        cek = update_id(cek)

        
        with open('Data/data.txt','w') as file :
            file.writelines(cek)


    clear_data()
    frame_destroy(frame2)
    body(frame_body)
   