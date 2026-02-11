from Data.variabel import inputan,data,button
import tkinter as tk
from tkinter import ttk


def clear_data() :
    inputan.clear()
    data.clear()
    button.clear()

def frame_destroy(frame:tk.Toplevel) : frame.destroy()

def clear_frame(frame: ttk.Frame):
    for widget in frame.winfo_children():
        widget.destroy()

