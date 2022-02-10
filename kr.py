import tkinter as tk
from tkinter import Button, Entry, Label, Place, StringVar, Text, Tk, mainloop, ttk
from tkinter import font
from tkinter import messagebox
from tkinter.constants import ANCHOR, BOTTOM, COMMAND, END, LEFT, RIGHT, TOP, X, Y
from tkinter.font import BOLD
from tkinter import filedialog as fd

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main() 


    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def sort_by_price(self, tv, col):
        return 0     

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=5, height=35)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        down = tk.Frame(bg='#d7d8e0', bd=5)
        down.pack(side=tk.BOTTOM, fill=tk.X) 

        btn_save = tk.Button(down, text='Сохранить таблицу', command=self.save_data, bg='#d7d8e0', bd=0)
        btn_save.pack(side=LEFT)

        btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='#d7d8e0', bd=0)   
        btn_open_dialog.pack(side=tk.LEFT)
        btn_open_dialog = tk.Button(toolbar, text='Редактировать', command=self.open_edit_window, bg='#d7d8e0', bd=0)   
        btn_open_dialog.pack(side=tk.LEFT)

        btn_sort = tk.Button(toolbar, text='Сортировать', command=lambda: self.sort_by_price(self.tree, 1), bg='#d7d8e0', bd=0)
        btn_sort.pack(side=LEFT)
        
        self.tree = ttk.Treeview(self, columns=('name', 'price', 'ammount', 'ed'), height=20, show='headings')
        self.tree.column('name', width=200, anchor=tk.CENTER)
        self.tree.column('price', width=350, anchor=tk.CENTER)
        self.tree.column('ammount', width=100, anchor=tk.CENTER)
        self.tree.column('ed', width=80, anchor=tk.CENTER)

        self.tree.heading('name', text='Название', command=lambda: self.treeview_sort_column(self.tree, 0, False))
        self.tree.heading('price', text='Стоимость(руб)')
        self.tree.heading('ammount', text='Количество')
        self.tree.heading('ed', text='Ед. измереения')
        self.tree.pack(side=tk.LEFT)

        self.scroll = ttk.Scrollbar(self, command=self.tree.yview)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scroll.set)

        lbl1 = tk.Label(down, text='Показать продукт с названием: ', background='#d7d8e0')
        self.entry_name = ttk.Entry(down, width=20)
        btn_show = tk.Button(down, text='Показать', command=self.show_product)
        btn_show.pack(side=RIGHT, padx=7)
        self.entry_name.pack(side=RIGHT)
        lbl1.pack(side=RIGHT)

    def newWord(self):
        word = self.string[0:self.string.find(' ')+1]
        self.string = self.string[self.string.find(' ')+1:len(self.string)]
        s = " ".join(word.split())
        return word
        
    def newLine(self, string):
        " ".join(string.split())
        if (len(string) > 1 ):
            self.string = string
            self.first = self.newWord()
            self.second = self.newWord()
            self.thirt = self.newWord()
            self.fourth = self.string[0:len(self.string)]
       

    def fillData(self):
        for row in self.tree.get_children():
                self.tree.delete(row)
        self.data = open('C:\\Users\\Vinda\\Desktop\\Programms\\products.txt', mode='r', encoding='utf8').readlines()
        for i in range (len(self.data)):
            s = self.data[i]
            ' '.join(s.split())
            self.newLine(s)
            self.tree.insert('', 'end', values=(self.first, self.second, self.thirt, self.fourth))

    def save_data(self):
        data_to_write = ''
        for line in self.tree.get_children():
            for value in self.tree.item(line)['values']:
                value = " ".join(str(value).split())
                data_to_write = data_to_write + str(value) + " "    
            data_to_write +='\n'    
        filepath = fd.asksaveasfilename(title='Сохранить', filetypes=((".txt", "*.txt"),))
        filepath = filepath.replace('\\', '\\\\')
        if (filepath.find('.txt') == False):
            filepath += '.txt'    
        with open(filepath, "w", encoding='utf8') as file:
            for i in range(len(data_to_write)):
                file.write(data_to_write[i])

    def addData(self, string):
        self.newLine(string)
        self.tree.insert('', 'end', values=(self.first, self.second, self.thirt, self.fourth))

    def updateData(self, string):
        self.newLine(string)
        row_id = self.tree.focus()
        self.tree.item(row_id, values=(self.first, self.second, self.thirt, self.fourth))

    def show_product(self):
        if (len(self.entry_name.get()) > 1):
            l = [(self.tree.set(k, 0), k) for k in self.tree.get_children('')]
            find_name = self.entry_name.get()
            find_name = " ".join(find_name.split())
            find_name.strip()
            for index, row_id in enumerate(self.tree.get_children(), 0):
                s = l[index][0]
                s = " ".join(s.split())
                s = s.lower()
                if (find_name == s):
                    continue
                self.tree.delete(row_id)

    def open_dialog(self):
        addWindow()

    def open_edit_window(self):
        Update()     

class addWindow(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def addData(self):
        if (len(self.entry_name.get()) == 0 or len(self.entry_ammount.get()) == 0 or len(self.entry_price.get()) == 0):
            from tkinter import messagebox
            messagebox.showinfo('Ошибка', 'Строка пустая')
        else:    
            allString = str(self.entry_name.get()) + " " + str(self.entry_price.get()) + " " + str(self.entry_ammount.get()) + " " + str(self.add_ed.get())
            if (type(self).__name__ == 'addWindow'):    
                app.addData(allString)
            elif (type(self).__name__ == 'Update'):
                app.updateData(allString)    
            
            self.destroy()

    def init_child(self):
        self.title('Добавить запись')
        self.geometry('820x100+300+100')
        self.resizable(False,False)

        self.lbl = ttk.Label(self, text="Название товара", font=("Times New Roman", 13, BOLD)) 
        self.lbl.place(relx=.05, rely=.1)
        self.lbl = ttk.Label(self, text="Цена", font=("Times New Roman", 13, BOLD)) 
        self.lbl.place(relx=.3, rely=.1)
        self.lbl = ttk.Label(self, text="Кличество", font=("Times New Roman", 13, BOLD)) 
        self.lbl.place(relx=.5, rely=.1)
        self.lbl = ttk.Label(self, text="Ед. измерения", font=("Times New Roman", 13, BOLD)) 
        self.lbl.place(relx=.7, rely=.1)
        self.entry_name = ttk.Entry(self, width=20)
        self.entry_name.place(relx=.05, rely=.34)
        self.entry_price = ttk.Entry(self, width=10)
        self.entry_price.place(relx=.3, rely=.34)
        self.entry_ammount = ttk.Entry(self, width=15)
        self.entry_ammount.place(relx=.5, rely=.34)
     
        self.add_ed = ttk.Combobox(self, width=4)
        self.add_ed.place(relx=.73,rely=.34)
        self.add_ed['values'] = ['шт', 'л', 'кг']


        self.btn_add = tk.Button(self, text='Добавить запись', command=self.addData, bg='#d7d8e0', bd=0)
        self.btn_add.place(relx=.4, rely=.7)
        self.grab_set()
        self.focus_set()   

class Update(addWindow):
        def __init__(self):
            super().__init__()
            self.init_edit()

        def init_edit(self):
            self.title('Редактировать')
            self.btn_add['text'] = 'Редактировать'

if __name__ == "__main__":
    root = tk.Tk()
   
    app = Main(root)
    app.pack()
    root.title("Продукты")
    root.geometry("820x250+250+80")
    root.resizable(True, False)
    app.fillData()
    root.mainloop()    