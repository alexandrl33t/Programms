import tkinter as tk
from tkinter import StringVar, Text, Tk, ttk
from tkinter import font
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
   
    def fillH(self):
        hours=[]
        for i in range (0,24,1):
            hours.append(str(i))
        for i in range(0,10,1):
            hours[i] = "0" + hours[i]    
        self.hCB['values'] = hours

    def fillM(self):
        minutes = []
        for i in range (60):
            minutes.append(str(i))
        for i in range(0,10,1):  
            minutes[i] = "0" + minutes[i]
        self.mCB['values'] = minutes 
    
    def sortTime(self):
        l = [(self.tree.set(k, 2), k) for k in self.tree.get_children('')]
        
        for i in range (len(l)):
            s = l[i][0]
            s = " ".join(s.split())
            if (int(s[0:2]) < int(self.hCB.get())):
                self.tree.delete(l[i][1])
            elif (int(s[0:2]) == int(self.hCB.get())):
                if (int(s[3:len(s)]) < int(self.mCB.get())):   
                    self.tree.delete(l[i][1])         
        

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        down = tk.Frame(bg='#d7d8e0', bd=5)
        down.pack(side=tk.BOTTOM, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='#d7d8e0', bd=0)   
        btn_open_dialog.pack(side=tk.LEFT)

        btn_open_dialog = tk.Button(toolbar, text='Редактировать', command=self.open_edit_window, bg='#d7d8e0', bd=0)   
        btn_open_dialog.pack(side=tk.LEFT, padx=8)

        btn_open_dialog = tk.Button(toolbar, text='Сохранить', command=self.save, bg='#d7d8e0', bd=0)   
        btn_open_dialog.pack(side=tk.LEFT, padx=8)   


        self.tree = ttk.Treeview(self, columns=('distanation', 'pometka', 'time'), height=20, show='headings')
        self.tree.column('distanation', width=250, anchor=tk.CENTER)
        self.tree.column('pometka', width=150, anchor=tk.CENTER)
        self.tree.column('time', width=220, anchor=tk.CENTER)

        self.tree.heading('distanation', text='Пункт назначения', command=lambda: self.treeview_sort_column(self.tree, 0, False))
        self.tree.heading('pometka', text='Пометка', command=lambda: self.treeview_sort_column(self.tree, 1, False))
        self.tree.heading('time', text='Время', command=lambda: self.treeview_sort_column(self.tree, 2, False))

        self.tree.pack(side=tk.LEFT)

        self.scroll = ttk.Scrollbar(self, command=self.tree.yview)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scroll.set)

        lbl1 = tk.Label(down, text='Показать поезда после: ', background='#d7d8e0')
        self.hCB = ttk.Combobox(down,state="readonly", width=4)
        self.fillH()
        self.hCB.current(0)
        lbl2 = ttk.Label(down, text=":", font=("Arial Bold", 13), background='#d7d8e0')
        self.mCB = ttk.Combobox(down,state="readonly", width=4)
        self.fillM()
        self.mCB.current(0)
        btn_SortbyTime = tk.Button(down, text='Показать', command=self.sortTime)
        btn_SortbyTime.pack(side=RIGHT)
        self.mCB.pack(side=RIGHT, padx=8)
        lbl2.pack(side=RIGHT)
        self.hCB.pack(side=RIGHT, padx=8)
        lbl1.pack(side=RIGHT)
        

    def newLine(self, string):
        new_line = string.replace('\n', '')
        if (int(new_line.find('КСВ') != -1)):
            z = new_line.find("КСВ")
        elif (int(new_line.find('СВ') != -1)):
            z = new_line.find("СВ")
        elif (int(new_line.find('ПВ') != -1)):
            z = new_line.find("ПВ")           
        self.first = new_line[0:z-1]  
        new_line = new_line[z:len(new_line)]
        z = new_line.find(" ")
        self.second = new_line[0:z]
        self.thirt = new_line[z+1:len(new_line)]

    def fillData(self):
        data = open('C:\\Users\\Vinda\\Desktop\\Programms\\ras.txt', mode='r', encoding='utf8').readlines()
        for i in range (len(data)):
            s = data[i]
            self.newLine(s)
            self.tree.insert('', 'end', values=(self.first, self.second, self.thirt))

    def addData(self, string):
        self.newLine(string)
        self.tree.insert('', 'end', values=(self.first, self.second, self.thirt))

    def updateData(self, string):
        self.newLine(string)
        row_id = self.tree.focus()
        self.tree.item(row_id, values=(self.first, self.second, self.thirt))
        


    def open_dialog(self):
        addWindow()

    def open_edit_window(self):
        Update()        

    def save(self):
        data_to_write = ''
        for line in self.tree.get_children():
            for value in self.tree.item(line)['values']:
                data_to_write = data_to_write + value + " "
            data_to_write += '\n'
        filepath = fd.asksaveasfilename(title='Сохранить', filetypes=((".txt", "*.txt"),))
        filepath = filepath.replace('\\', '\\\\')
        if (filepath.find('.txt') == False):
            filepath += '.txt'    
        with open(filepath, "w", encoding='utf8') as file:
            for i in range(len(data_to_write)):
                file.write(data_to_write[i])


class addWindow(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def fillH(self):
        hours=[]
        for i in range (0,24,1):
            hours.append(str(i))
        for i in range(0,10,1):
            hours[i] = "0" + hours[i]    
        self.addHour['values'] = hours

    def fillM(self):
        minutes = []
        for i in range (60):
            minutes.append(str(i))
        for i in range(0,10,1):  
            minutes[i] = "0" + minutes[i]
        self.addMinute['values'] = minutes   

    def addData(self):
        s = self.entry.get()
        s = " ".join(s.split())
        s = s.strip()
        if (len(s) == 0):
            from tkinter import messagebox
            messagebox.showinfo('Ошибка', 'Строка пустая')
        else:    
            allString = s + " " +str(self.addPometka.get()) + " " + str(self.addHour.get()) + ":" + str(self.addMinute.get()) 
            if (type(self).__name__ == 'addWindow'):    
                app.addData(allString)
            elif (type(self).__name__ == 'Update'):
                app.updateData(allString)    
            
            self.destroy()

    def init_child(self):
        self.title('Добавить запись')
        self.geometry('600x100+300+100')
        self.resizable(False,False)

        self.lbl = ttk.Label(self, text="Пункт назначения", font=("Times New Roman", 13, BOLD)) 
        self.lbl.place(relx=.05, rely=.1)
        self.lbl = ttk.Label(self, text="Пометка", font=("Times New Roman", 13, BOLD)) 
        self.lbl.place(relx=.48, rely=.1)
        self.lbl = ttk.Label(self, text="Время отправления", font=("Times New Roman", 13, BOLD)) 
        self.lbl.place(relx=.7, rely=.1)
        tex = StringVar()
        self.entry = ttk.Entry(self, textvariable=tex, width=35)
        self.entry.place(relx=.05, rely=.4)

        self.addPometka = ttk.Combobox(self, state="readonly", values=["СВ", "ПВ", "КСВ"], width=5)
        self.addPometka.current(0) 
        self.addPometka.place(relx=.5, rely=.4)

        self.addHour = ttk.Combobox(self,state="readonly", width=4)
        self.addHour.place(relx=.73,rely=.4)
        self.fillH()
        self.addHour.current(0)

        self.lbl = ttk.Label(self, text=":", font=("Arial Bold", 13))
        self.lbl.place(relx=.823,rely=.4)

        self.addMinute = ttk.Combobox(self,state="readonly", values=[], width= 4)
        self.fillM()
        self.addMinute.current(0)
        self.addMinute.place(relx=.85,rely=.4)

        self.btn_add = tk.Button(self, text='Добавить запись', command=self.addData, bg='#d7d8e0', bd=0)
        self.btn_add.place(relx=.45, rely=.7)
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
    root.title("Расписание")
    root.geometry("650x450+300+100")
    root.resizable(False, False)
    app.fillData()
    root.mainloop()    