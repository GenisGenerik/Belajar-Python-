
from GUI.header import header
from GUI.body import body
from GUI.variabel import utama,frame_header,frame_body

def run_app() :
   
    utama.geometry("700x700")
    utama.title("Halaman Utama")


   
    frame_header.pack(fill="x")

   
    frame_body.pack(fill="both", expand=True)

    header(frame_header)
    body(frame_body)


    
    utama.mainloop()

