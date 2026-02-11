from Data.variabel import head,data
import tkinter as tk
from tkinter import ttk
from Data.read_data import read_data
from Data.delete_data import delete_data
from GUI.show_data import show_data
from Data.variabel import button
from GUI.edit_data import edit
from GUI.clear import clear_frame,clear_data

def body(frame1:ttk.Frame)->None :
    clear_frame(frame1)
    clear_data()
    isi = read_data()
    show_data(frame1,isi)
    len_head = len(head)
    len_data = len(data)
    temp:list[tk.Button] = [] 
    for i in range(len_data) :
        butt = tk.Button(frame1,text="Edit",command= lambda x=i : edit(frame1,x))
        butt.grid(row=2+i,column=len_head-1)
        temp.append(butt)
        butt = tk.Button(frame1,text="Delete",command= lambda x=i:delete_data(frame1,x))
        butt.grid(row=2+i,column=len_head)
        temp.append(butt)
        button.append(temp.copy())
        temp.clear()
    


    

