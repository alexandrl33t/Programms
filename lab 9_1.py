from tkinter.constants import BOTTOM, CENTER, E, LEFT, N, NE, NS, NW, RIGHT, SE, TOP
from tkinter.font import BOLD
from tkinter.ttk import Button
import complex
import tkinter as tk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    
    class Toolbar():
        def __init__(self):
            self.toolbar1 = tk.Frame(bg='#d7d8e0', bd=5, height= 100)
            self.toolbar1.pack(side=tk.LEFT, fill=tk.Y, anchor=NW)

            self.lbl1 = tk.Label(self.toolbar1, text='Первое число', font=(15), bg='#d7d8e0')
            self.lbl1.pack(side=TOP)
            self.lbl = tk.Label(self.toolbar1, text='Введите а:', font=(15), bg='#d7d8e0')
            self.lbl.pack(side=TOP,pady=1)

            self.entry_a = tk.Entry(self.toolbar1, width=15)
            self.entry_a.pack(side=TOP, pady=5, padx=5)
            self.lbl = tk.Label(self.toolbar1, text='Введите b:', font=(15), bg='#d7d8e0')
            self.lbl.pack(side=TOP,pady=5)
            self.entry_b = tk.Entry(self.toolbar1, width=15)
            self.entry_b.pack(side=TOP, pady=5, padx=5)

    class Toolbar2(Toolbar): 
        def __init__(self):
            super().__init__()
            self.init_child()

        def init_child(self):
            self.lbl1['text'] = 'Второе число'
            self.toolbar1.pack(side=LEFT)
    def Toolbar_options(self):
        self.toolbar1 = tk.Frame(bg='#d7d8e0', bd=5, height= 100)
        self.toolbar1.pack(side=tk.LEFT, fill=tk.Y, anchor=NW)

        self.btn = Button(self.toolbar1, text='+', command=self.plus)
        self.btn.pack(side=BOTTOM, anchor=CENTER)
        self.btn = Button(self.toolbar1, text='-', command=self.minus)
        self.btn.pack(side=BOTTOM,pady=15, anchor=CENTER)
        self.btn = Button(self.toolbar1, text='*', command=self.mult)
        self.btn.pack(side=BOTTOM, anchor=CENTER)

    def plus(self):
        self.a = int(self.first.entry_a.get())
        self.b = int(self.first.entry_b.get())
        self.first_a = complex.Complex(self.a, self.b)
        self.a = int(self.second.entry_a.get())
        self.b = int(self.second.entry_b.get())
        self.second_b = complex.Complex(self.a, self.b)
        self.answer.lbl_answer['text'] = self.first_a + self.second_b
    def minus(self):
        self.a = int(self.first.entry_a.get())
        self.b = int(self.first.entry_b.get())
        self.first_a = complex.Complex(self.a, self.b)
        self.a = int(self.second.entry_a.get())
        self.b = int(self.second.entry_b.get())
        self.second_b = complex.Complex(self.a, self.b)
        self.answer.lbl_answer['text'] = self.first_a - self.second_b
    def mult(self):
        self.a = int(self.first.entry_a.get())
        self.b = int(self.first.entry_b.get())
        self.first_a = complex.Complex(self.a, self.b)
        self.a = int(self.second.entry_a.get())
        self.b = int(self.second.entry_b.get())
        self.second_b = complex.Complex(self.a, self.b)
        self.answer.lbl_answer['text'] = self.first_a * self.second_b

    class Answer():                 
        def __init__(self):
            self.toolbar1 = tk.Frame(bg='#d7d8e0', bd=5, height= 100)
            self.toolbar1.pack(side=tk.LEFT, fill=tk.Y, anchor=NW, padx=5)
            self.lbl1 = tk.Label(self.toolbar1, text='   Ответ   ', font=(BOLD,15), bg='#d7d8e0')
            self.lbl1.pack(side=TOP)
            self.lbl_answer = tk.Label(self.toolbar1, text='', font=(BOLD,14), bg='#d7d8e0')
            self.lbl_answer.pack(side=TOP, anchor=CENTER)
    def init_main(self):
        self.first = self.Toolbar()
        self.options = self.Toolbar_options()
        self.second = self.Toolbar2()
        self.answer = self.Answer() 


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    root.title('Комплексные числа (a + bi)')
    root.geometry('480x180+300+250')
    root.resizable(False, False)
    app.pack()
    root.mainloop()