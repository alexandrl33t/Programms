from email.mime import audio
from enum import auto
from re import S
from textwrap import fill
import tkinter as tk
from tkinter import ALL, CENTER, DISABLED, SW, Button, Entry, Label, Place, StringVar, Text, Tk, mainloop, ttk
from tkinter import font
from tkinter import messagebox
from tkinter.constants import ANCHOR, BOTTOM, COMMAND, END, LEFT, RIGHT, TOP, X, Y
from tkinter.font import BOLD
from tkinter import filedialog as fd
from turtle import left
import parsing as pr


class Main(tk.Frame):
    
    def __init__(self, root):
        super().__init__(root)
        self.init_main() 

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=5, height=35) #фрейм для заголовка
        toolbar.pack(side=tk.TOP, fill=tk.X)
        root["bg"] = "#d7d8e0"

        empty1 = tk.Frame(bg='#FAEEDD', bd=5, height=450) #фрейм для ввода
        empty1.pack(side=tk.TOP, fill=tk.BOTH)

        output = tk.Frame(bg='#d7d8e0', bd=5, height=100) #фрейм для вывода
        output.pack(side=tk.TOP, fill=tk.X)

        self.lbl1 = tk.Label(toolbar,text="Программа", padx=170, background="#d7d8e0",  font=('Times New Roman', 14, BOLD))
        self.lbl1.pack(side=LEFT)
        self.lbl1 = tk.Label(toolbar,text="Форма языка БНФ", padx=170, background="#d7d8e0",  font=('Times New Roman', 14, BOLD))
        self.lbl1.pack(side=RIGHT)

        self.entry1 = tk.Text(empty1,font="Courier 13", width=70, border=2)
        self.entry1.place(x=0, y=0, height=440, width=440)

        self.entry2 = tk.Text(empty1, font="Courier 13", width=70, border=2)
        self.entry2.place(x=450, y=0, height=440, width=440)
        
        self.lbl1 = tk.Label(output, text="Вывод:", padx=30, background="#d7d8e0",  font=('Times New Roman', 14))
        self.lbl1.place(x=0,y=0)

        self.output_field = tk.Text(output, font="Courier 13",width=900, border=2, pady=4)
        self.output_field.place(x=0, y=25, height=70, width=890)

        self.apply_btn = tk.Button(root, text="Выполнить", font=("Courier", 13, BOLD), width=10, command=self.apply)
        self.apply_btn.place(relx=0.85, rely= 0.938)

        self.dataText = ''
        self.fillData()
        self.entry2["state"] = DISABLED
        

    def fillData(self):
        self.data = open('bnf.txt', mode='r', encoding='utf8').readlines()
        for id,string in enumerate(self.data):
            string = str(string)
            self.entry2.insert(float(id+1), string)

    def apply(self):
        self.output_field.delete(1.0, END)
        self.output_field.insert(1.0, pr.check_for_errors(self.entry1.get(1.0, END)))         
                

    



            

if __name__ == "__main__":
    root = tk.Tk()
   
    app = Main(root)
    app.pack()
    root.title("Programm")
    root.geometry("900x630+250+80")
    root.resizable(False, False)
    root.mainloop()    