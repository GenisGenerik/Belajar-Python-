
def read_data()->list[str] :

    with open('Data/data.txt','r') as file :
        isi = file.read().splitlines()
    
    return isi