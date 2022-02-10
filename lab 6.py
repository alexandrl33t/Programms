from os import path, write
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Combobox
def fillH(addH):
    hours=[]
    for i in range (0,24,1):
        hours.append(str(i))
    for i in range(0,10,1):
        hours[i] = "0" + hours[i]    
    addH['values'] = hours

def fillM(addM):
    minutes = []
    for i in range (60):
        minutes.append(str(i))
    for i in range(0,10,1):  
        minutes[i] = "0" + minutes[i]
    addM['values'] = minutes  

from tkinter import messagebox 
def writeValues(dist, pometka, hour, minute):
    new_line = dist.get()
    new_line = " ".join(new_line.split())
    new_line = new_line.strip()
    if (len(new_line)>0):
        new_line += " " + pometka.get() + " " + hour.get() + ":" + minute.get()
        data.append(new_line)
        messagebox.showinfo("Успех", "Данные добавлены")
        addWindow.destroy()
        main2 = MainWindow()
    else: 
        messagebox.showinfo("Ошибка", "Пункт назначения не заполнен")    

from functools import partial

def pressed():
    global addWindow
    addWindow = Tk()
    addWindow.geometry('600x150')
    drawHead(addWindow)
    tex = StringVar()
    addDist = Entry(addWindow,textvariable=tex, width=30)
    addDist.grid(column=0,row=1)
    addPometka = Combobox(addWindow, state="readonly", values=["СВ", "ПВ", "КСВ"])
    addPometka.current(0)
    addPometka.grid(column=1, row=1)
    addHour = Combobox(addWindow,state="readonly", width=4)
    fillH(addHour)
    addHour.current(0)
    lbl = Label(addWindow, text=":", font=("Arial Bold", 13))
    addMinute = Combobox(addWindow,state="readonly", values=[], width= 4)
    fillM(addMinute)
    addMinute.current(0)
    addHour.place(relx=.72,rely=.5)
    lbl.place(relx=.815,rely=.49)
    addMinute.place(relx=.85,rely=.5)
    confColumns(addWindow)
    add = Button(addWindow, text="Добавить запись", command=partial(writeValues, addDist, addPometka, addHour, addMinute), width=20, bg='#34D1B2')
    add.place(relx=.3, rely=.8)
    addWindow.resizable(0,0)
    addWindow.mainloop()


#create menu

def openF(entry):
    path = entry.get()
    if(len(path)>0):
        path = " ".join(path.split())
        path.strip()
        if (path[len(path)-4:len(path)] != ".txt"):
            messagebox.showerror("Ошибка", "Неверный формат файла")
        else:
            for i in window.winfo_children():
                i.destroy()
            path = path.replace("\\", "\\\\")
            data2 = open(path, "r", encoding='utf-8').readlines()
            pathWindow.destroy()
            data.clear()
            for i in range(len(data2)):
                data.append(data2[i])  
            drawHead(window)
            drawButtons()
            main = MainWindow()
           
            


def openFile():
    global pathWindow
    pathWindow = Tk()
    pathWindow.geometry('500x130')
    pathWindow.title("Открыть файл")
    lbl = Label(pathWindow, text= "Введите путь к файлу")
    lbl.place(relx=0.1, rely=0.1)
    entry = Entry(pathWindow, width=70)
    entry.place(relx=0.1, rely=0.4)
    openBtn = Button(pathWindow, width=10, text="Открыть", command=partial(openF, entry), bg='#34D1B2')
    openBtn.place(relx=0.5, rely=0.7)
    pathWindow.mainloop()

def sFile(entry, entry2):
    path = entry.get()
    name = entry2.get()
    if(len(path)>0 and len(name)>0):
        path = " ".join(path.split())
        path.strip()
        path = path.replace("\\", "\\\\")
        path+="\\\\"+name+".txt"
        with open(path, 'w', encoding='utf8') as file:
            for i in range(len(data)):
                file.write(data[i])

        saveWindow.destroy()
        

def saveFile():
    global saveWindow
    saveWindow = Tk()
    saveWindow.geometry('500x130')
    saveWindow.title("Сохранить файл")
    lbl = Label(saveWindow, text= "Введите папку, куда сохранить файл")
    lbl.place(relx=0.1, rely=0.1)
    entry = Entry(saveWindow, width=70)
    entry.place(relx=0.1, rely=0.3)
    lbl = Label(saveWindow, text= "Введите название файла")
    lbl.place(relx=0.1, rely=0.5)
    entry2 = Entry(saveWindow, width=30)
    entry2.place(relx=0.1, rely=0.7)
    openBtn = Button(saveWindow, width=10, text="Сохранить", command=partial(sFile, entry, entry2), bg='#34D1B2')
    openBtn.place(relx=0.55, rely=0.68)

    saveWindow.mainloop()

class MainWindow:

    def __init__(self):
    #отрисовка расписания
        self.distanation = []
        self.metka = []
        self.time=[]
        for i in range (len(data)):
            new_line = data[i].replace('\n', '')
            z = new_line.find(" ")
            first = new_line[0:z]
            self.distanation.append(first)
            self.lbl = Label(window, text=first, font=("Times New Roman", 10)) 
            self.lbl.grid(column=0, row = i+1, pady=10)
            new_line = new_line[z+1:len(new_line)]
            z = new_line.find(" ")
            second = new_line[0:z]
            self.metka.append(second)
            self.lbl = Label(window, text=second, font=("Times New Roman", 10)) 
            self.lbl.grid(column=1, row = i+1, pady=10)
            thirt = new_line[z+1:len(new_line)]
            self.time.append(thirt)
            self.lbl = Label(window, text=thirt, font=("Times New Roman", 10)) 
            self.lbl.grid(column=2, row = i+1, pady=10)

        

def drawHead(window):
    lbl = Label(window, text="Пункт назначения", font=("Times New Roman", 13, BOLD)) 
    lbl.grid(column=0, row = 0)
    lbl = Label(window, text="Пометка", font=("Times New Roman", 13, BOLD)) 
    lbl.grid(column=1, row = 0)
    lbl = Label(window, text="Время отправления", font=("Times New Roman", 13, BOLD)) 
    lbl.grid(column=2, row = 0)

def drawButtons():
    menu = Menu(window)  
    new_item = Menu(menu, tearoff=0)  
    menu.add_cascade(label='Файл', menu=new_item)
    new_item.add_command(label="Открыть", command=openFile)    
    new_item.add_command(label="Сохранить как", command=saveFile)
    window.config(menu=menu) 
    btn = Button(window, text="Добавить запись", command = pressed, bg='#34D1B2', font=(10, 10, BOLD))
    btn.grid(column=3, row=2)     

def confColumns(window):
    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=100)
        window.rowconfigure(i, weight=1, minsize=10)    
window = Tk()
window.title("Расписание электричек")
window.geometry('600x270')
drawHead(window)
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=100)
global data
data = open('C:\\Users\\Vinda\\Desktop\\Programms\\ras.txt', mode='r', encoding='utf8').readlines()
drawButtons()


main = MainWindow() 


#добавить запись 





window.mainloop()
input()    