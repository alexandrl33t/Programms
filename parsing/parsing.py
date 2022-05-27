

from copy import copy
from dataclasses import replace
from distutils.filelist import findall
from doctest import OutputChecker
from genericpath import exists
from logging import exception
from ntpath import join
import string
from turtle import right
from unicodedata import digit
import re
import right_part as rp

import re

memory = {}

<<<<<<< HEAD
class Check():
=======
def peremError(perem, number_of_command):
    return f"zОшибка. Переменная {perem} должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)

def complited_right_part(right,number_of_command):
    right = "".join(right.split())
    new_right = ''
    k = 0
    for i in range(len(right)):
        if k > 0:
            k -=1
            continue
        if right[i].isalpha() == False:
            new_right += right[i]
            continue 
        try:
            perem = right[i:i+5]
            regex = '[\+|\-|\*|\/|\&|\||\(|\)|\[|\]|\^]'
            if len(perem) == 5:
                m = re.search(f'[а-я][0-7][0-7][0-7]{regex}', perem)
                if not m:
                    return peremError(perem, number_of_command)   
                perem = right[i:i+4]
            elif len(perem) == 4:
                m = re.search(f'[а-я][0-7][0-7][0-7]', perem)   
                if not m:
                    return peremError(perem, number_of_command)     
            new_right += memory[perem]
            k = 3                
        except:
            return peremError(perem, number_of_command) 
    right = " ".join(new_right.split())
    right = cf.check_quad(right)
    if right.find('z') > -1:
        return right + str(number_of_command)                   
    isRight = cf.check(right)
    if isRight == True:
        try:   
            return eval(right)
        except ZeroDivisionError:
                return "zОшибка. Деление на ноль. f" + str(number_of_command)      
    else: return isRight + str(number_of_command)

def right_part(commands, number_of_command):
    #отсечение правой части 
>>>>>>> bf03fa43b14f82180dae8e83e1795d1f29dcee1f
    
    command = ''
    data = ''
    glubina = 0
    skobka_is_opened = False
    def __init__(self, data):
        self.command = ''
        self.data = data
        self.glubina = 0
        self.skobka_is_opened = False

    def calculate(self, command:str, last_word):
        if len(command) == 0:
            if last_word == 'metka' or last_word == 'metka space':
                return f"zОшибка. После метки должно стоять \':\''f{self.command}f1"
            if last_word == ':' or last_word == ': space' :
                return f"zОшибка. После \':\' должна идти переменная'f{self.command}f1"  

        for i in range(len(command)):
            if last_word == 'metka space':
                if command[i] == ":":
                    return self.calculate(command[i+1:len(command)], ':')
                else:
                    return f"zОшибка. После метки должно стоять \':\''f{self.command}f1" 

            if last_word == 'metka':
                if command[i].isdigit():
                        return self.calculate(command[i+1:len(command)], 'metka') 
                elif command[i] != ":" and not command[i].isspace():
                    return f"zОшибка. Метка должна быть целочисленной'f{self.command}f1"                 
                elif command[i].isspace():
                    return  self.calculate(command[i+1:len(command)], 'metka space')              
                elif command[i] == ":":
                    return  self.calculate(command[i+1:len(command)], ':') 
            elif last_word == ':' or last_word == ': space':
                if command[i].isalpha():
                    perem = command[i:i+4]
                    m = re.search('[а-я][0-7][0-7][0-7]', perem)   
                    if not m:
                        return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f{self.command}f1"
                    try:
                        if command[i+4] == " ":
                            if command [i+5] == '=':
                                memory[perem] =  rp.right_calculate(command[i+6:len(command)], memory)
                                if memory[perem].find("z")>-1:
                                    return memory[perem][memory[perem].find("z"):memory[perem].find("f")+1] + self.command + "f1"   
                                return ""
                            else: 
                                return f"zОшибка. После переменной должно стоять \'=\'f{self.command}f1" 
                        elif command[i+4] == '=':
                            memory[perem] = rp.right_calculate(command[i+5:len(command)], memory)
                            if memory[perem].find("z")>-1:
                                return memory[perem][memory[perem].find("z"):memory[perem].find("f")+1] + self.command + "f1" 
                            return ""
                        else: 
                            return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f{self.command}f1"    
                    except:
                        return f"zОшибка. После переменной должно стоять \'=\'f{self.command}f1" 
                elif command[i].isspace():
                     return  self.calculate(command[i+1:len(command)], ': space')
                elif command[i] == ':':
                        return 'zОшибка. Дублируется \':\'f'      
                else: 
                    return f"zОшибка. Переменная должна быть формата \'БЦЦЦ\', где Б = А!Б!...!Я, Ц = 0!1!...!7'f{self.command}f1"  
        return ""         
                    

<<<<<<< HEAD
    def command_processing(self, command:str):
        if not command.startswith("ввод "):
            return f"zОшибка. Звено должно начинаться со слова \'Ввод\'f{command}f1"
        command = command[command.find("ввод ")+5:len(command)]
        
        return self.calculate(command, 'metka') 

    def check_for_errors(self):
        self.data = self.data.lower()
        self.data = " ".join(self.data.split())
        #начинается со слов программа и конец
        if not self.data.startswith("программа"):
            return "zОшибка. Программа должна начинаться со слова \'Программа\'f"
        if not re.search('.*[\s|\\n]*(конец)$', self.data):
            return "zОшибка. Программа должна заканчиваться словом \'Конец\'f"
        #проверка наличия разделителя
        self.data = " ".join(self.data.split()[1:-1])
        if len(re.findall('ввод', self.data)) - len(re.findall(';', self.data)) > 1:
            place = re.findall('\S*[\w|\)|\]]\s*ввод', self.data)[0]
            return "zОшибка. Отсутствует \';\' между \"" + place + "\""
        
        #разделение на массив команд и обработка каждой
        command_list = re.split(';', self.data)        
=======
    try:
        commands[1] = str(int(commands[1]))
    except:
        return "zОшибка. Метка должна быть целым числом.f" + str(number_of_command)    
   #проверка переменной
    
    try:
        if " ".join(commands).find("=") > -1:
            commands = " ".join(commands)
            commands = re.split("=", commands)
        else:
            return "zОшибка. После переменной должно стоять \"=\"f" + str(number_of_command)
    except:
        return "zОшибка. Неполная командаf" + str(number_of_command)   
    left = commands[0].split()
    perem = str(left[len(left)-1])
    try:
        m = re.search('[а-я][0-7][0-7][0-7]', perem)
        if not m.group():
            return peremError(perem, number_of_command)    
    except:
        return peremError(perem, number_of_command)  
    
    memory[perem] = right_part(commands, number_of_command)
    try: 
        memory[perem] = str(int(memory[perem]))
    except:
        pass  
    return str(perem) + " = " +str(memory[perem]) + "\n"

def check_for_errors(data):
    data = data.lower()
    data_list = data.split()
    try:
        if data_list[0] != "программа":
            return  "Ошибка. Программа должна начинаться со слова ""Программа"""
        elif data_list[len(data_list)-1] != "конец":
            return  "Ошибка. Программа, должна заканчиваться словом ""Конец""" 
    except: return  "Программа пуста."  
>>>>>>> bf03fa43b14f82180dae8e83e1795d1f29dcee1f

        answer = 'Результат выполнения команд: \n'
        for i in range(len(command_list)):
            command_list[i] = " ".join(command_list[i].split())
            self.command = command_list[i]
            if len(command_list[i]) == 0:
                try:
                    len(command_list[i+1])
                    return "zОшибка. Дублируется \';\'f;;f1"
                except:    
                    continue
            answer += self.command_processing(command_list[i])

        for item in memory.keys():
            answer += item + " = " + str(memory[item]) + " " 
        if answer.find("z") > -1:
            return answer[answer.find("z"):answer.find('f1')+2]                          
        return  answer


    


if __name__ == '__main__':
<<<<<<< HEAD
    #print(check_for_errors('Программа 42:а455 = [[455 + 3]] + 350 конец'))    
    #a = Check('Программа Ввод 42:А565 = (61 конец')
    a = Check('Программа Ввод 55 : А565 = 5 / 5; ввод 55 : ф455 =а565 + 5 ; ввод 6: к666 = 7 + [а565 + ф455] + 100 конец')
    #a = Check('Программа ввод 42:а455 = 455 + 3 + ~350; ввод 55:ы222 = [а455+4] + 5 ; конец')
    #a = Check('Программа ввод 42: а666 = s   конец')
    print(a.check_for_errors())
=======
    #print(check_for_errors('Программа ввод 42:а455 = [[455 + 3]] ^ 350 конец'))    
   # print(check_for_errors('Программа Ввод 42:А565 = 5 * 5 + 20 конец'))
    print(check_for_errors('Программа Ввод 55:А565 = 5 / 5; ввод 55: ф455 = 6 + а565; ввод 6: к666 = 7 + а565 + ф455 + 100; конец'))
>>>>>>> bf03fa43b14f82180dae8e83e1795d1f29dcee1f
