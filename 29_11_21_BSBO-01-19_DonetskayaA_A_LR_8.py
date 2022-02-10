# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('820x300')  

class Node:
    def __init__(self, author,name,year,num,udk=None):
        self.author=author
        self.name=name
        self.year=year
        self.num=num
        self.data = udk
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def contains (self, data):
        lastNode = self.head
        while (lastNode):
          if data == lastNode.data:
            return True
          else:
            lastNode = lastNode.next
        return False
    def append(self, a1,a2,a3,a4,a5):
        newNode = Node(a1,a2,a3,a4,a5)
        if self.head is None:
          self.head = newNode
          return
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode
    def get(self, dataIndex):
        lastNode = self.head
        nodeIndex = 0
        while nodeIndex <= nodeIndex:
          if nodeIndex == dataIndex:
              return lastNode.data
          nodeIndex = nodeIndex + 1
          lastNode = lastNode.next
    def remove(self,data):
        headData = self.head  
        if headData is not None:
          if headData.data==data:
            self.head = headData.next
            headData = None
            return
        while headData is not None:
          if headData.data==data:

              break
          lastData = headData
          headData = headData.next
        if headData == None:
          return
        lastData.next = headData.next
        headData = None
list1 = LinkedList()

def b1():
    root_file = tk.Toplevel(root)
    root_file.geometry('620x300')
    lab1 = tk.Label(root_file,width=15, height=1, fg='black',text='Добавление',font=("Times New Roman", 20))
    lab1.grid(column=1, row=0)
    lab3 = tk.Label(root_file,width=20, height=1, fg='black',text='УДК',font=("Times New Roman", 12))
    lab3.grid(column=0, row=1)
    ent1 = tk.Entry(root_file,width=40)
    ent1.grid(column=1, row=1)
    lab4 = tk.Label(root_file,width=20, height=1, fg='black',text='Название',font=("Times New Roman", 12))
    lab4.grid(column=0, row=2)
    ent2 = tk.Entry(root_file,width=40)
    ent2.grid(column=1, row=2)
    lab5 = tk.Label(root_file,width=20, height=1, fg='black',text='Автор',font=("Times New Roman", 12))
    lab5.grid(column=0, row=3)
    ent3 = tk.Entry(root_file,width=40)
    ent3.grid(column=1, row=3)
    lab6 = tk.Label(root_file,width=20, height=1, fg='black',text='Год издания',font=("Times New Roman", 12))
    lab6.grid(column=0, row=4)
    ent4 = tk.Entry(root_file,width=40)
    ent4.grid(column=1, row=4)
    lab6 = tk.Label(root_file,width=20, height=1, fg='black',text='Количество',font=("Times New Roman", 12))
    lab6.grid(column=0, row=5)
    ent5 = tk.Entry(root_file,width=40)
    ent5.grid(column=1, row=5)
    but4 = tk.Button(root_file,width=20,height=1,text="Добавить",font=("Times New Roman", 10),command=lambda: [b4(ent2,ent1,ent3,ent4,ent5),root_file.destroy()])
    but4.grid(column=1, row=6)
    root_file.mainloop()

def b2(ivent):
    flag=0
    lastNode = list1.head
    while (lastNode):
          if ent6.get() == lastNode.data:
              list1.remove(ent6.get())  
              flag=1
              break
          else:
            lastNode = lastNode.next
    if flag==0:
        messagebox.showinfo("Неверный ввод", "Такого УДК нет")

def b3(ivent):
    list_sort=[]
    lastNode = list1.head
    while (lastNode):
        list_sort.append(lastNode)
        lastNode = lastNode.next
    list_sort.sort(key=lambda x: x.year)
    root_sort = tk.Toplevel(root)
    root_sort.geometry('820x300') 
    scroll2 = tk.Scrollbar(root_sort)
    listbox2 = tk.Listbox(root_sort, font=("Courier New", 12), yscrollcommand=scroll1.set,width=80)
    for index in list_sort:
        listbox2.insert("end", str(index.data)+int(10-len(index.data))*" "+str(index.name)+int(30-len(index.name))*" "+str(index.author)+int(20-len(index.author))*" "+str(index.year)+int(7-len(str(index.year)))*" "+str(index.num)+int(7-len(str(index.num)))*" ")
    listbox2.pack(side="left", fill="both")
    scroll2.pack(side="right", fill="y")
    scroll2.config(command=listbox2.yview)
    root_sort.mainloop()
      
def b4(ent2,ent1,ent3,ent4,ent5):
    if list1.contains(ent1.get()):
        messagebox.showinfo("Неверный ввод", "Уже есть такой УДК")
    elif len(ent2.get())>30:
        messagebox.showinfo("Неверный ввод", "Длина названия книги не должна превышать 30 символов")
    elif ent1.get().isdigit()==0:
        messagebox.showinfo("Неверный ввод", "УДК должен быть в интервале от 0 до 99999999")
    elif int(ent1.get())<0 or int(ent1.get())>99999999:
        messagebox.showinfo("Неверный ввод", "УДК должен быть в интервале от 0 до 99999999")
    elif len(ent3.get())>20:
        messagebox.showinfo("Неверный ввод", "Фамилия и инициалы автора не должны превышать 20 символов")
    elif ent4.get().isdigit()==0:
        messagebox.showinfo("Неверный ввод", "Некорректный код издания")
    elif int(ent4.get())>2021 or int(ent4.get())<1564:
        messagebox.showinfo("Неверный ввод", "Некорректный код издания")
    elif ent5.get().isdigit()==0:
        messagebox.showinfo("Неверный ввод", "Количество книг должно быть от 0 до 100")
    elif int(ent5.get())>100 or int(ent5.get())<0:
        messagebox.showinfo("Неверный ввод", "Количество книг должно быть от 0 до 100")
    else:
        list1.append(ent3.get(),ent2.get(),ent4.get(),ent5.get(),ent1.get()) 

def b5(ivent):   
    listbox1.delete(0,listbox1.size()-1)
    lastNode = list1.head
    while (lastNode):
        listbox1.insert("end", str(lastNode.data)+(10-len(lastNode.data))*" "+str(lastNode.name)+(30-len(lastNode.name))*" "+str(lastNode.author)+(20-len(lastNode.author))*" "+str(lastNode.year)+(7-len(str(lastNode.year)))*" "+str(lastNode.num)+(7-len(str(lastNode.num)))*" ")
        lastNode = lastNode.next

f_top = tk.Frame(root)
f_cen = tk.Frame(root)
f_bot = tk.Frame(root)
lab1 = tk.Label(root,width=15, height=1, fg='black',text='Меню',font=("Times New Roman", 20))
lab1.pack()
scroll1 = tk.Scrollbar(f_top)
listbox1 = tk.Listbox(f_top,font=("Courier New", 12), yscrollcommand=scroll1.set,width=80)
listbox1.insert("end", 'Книг нет')

but1 = tk.Button(f_cen,width=20,text="Добавить книгу",font=("Times New Roman", 14),command = b1)
but2 = tk.Button(f_bot,width=20,height=1,text="Списать",font=("Times New Roman", 10))
ent6 = tk.Entry(f_bot,width=40)
but3 = tk.Button(f_cen,width=20,height=1,text="Сортировка",font=("Times New Roman", 14))
but5 = tk.Button(f_cen,width=20,height=1,text="Обновить таблицу",font=("Times New Roman", 14))
f_top.pack()
f_cen.pack()
f_bot.pack()
listbox1.pack(side="left", fill="both")
scroll1.pack(side="right", fill="y")
scroll1.config(command=listbox1.yview)
but5.pack(side="left")
but1.pack(side="left")
but3.pack(side="left")
but2.pack(side="left")
ent6.pack(side="left")

but2.bind('<Button-1>',b2)
but3.bind('<Button-1>',b3)
but5.bind('<Button-1>',b5)

root.mainloop()