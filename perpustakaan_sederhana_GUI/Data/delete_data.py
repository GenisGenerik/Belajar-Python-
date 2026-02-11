from GUI.clear import clear_data
from tkinter import ttk




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


def delete_data(frame1: ttk.Frame, id: int) -> None:
    from GUI.body import body

    with open('Data/data.txt', 'r') as file:
        cek = file.readlines()

    panjang_awal = len(cek)

  
    if id == panjang_awal - 1 and panjang_awal > 1:
       
        isi_sebelum = cek[id - 1]
        isi_sebelum = isi_sebelum.rstrip(",\n") 
        cek[id - 1] = isi_sebelum 

    
    cek.pop(id)

    
    cek = update_id(cek)

    with open('Data/data.txt', 'w') as file:
        file.writelines(cek)

    clear_data()
    body(frame1)
