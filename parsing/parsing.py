

from dataclasses import replace
from doctest import OutputChecker
from logging import exception
from ntpath import join
import string
from unicodedata import digit
import re
import check_fo_errors_eval as cf



memory = {}


def complited_right_part(right,number_of_command):
    for letter in right:
        if letter.isalpha():
            m = re.search('[а-я][0-7][0-7][0-7]', right)
            if not m:
                return "zОшибка. Переменная в выражении должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)         
            try:
                right = right.replace(m.group(0), str(memory[m.group(0)]))
            except:
                return "zОшибка. Переменная " + m.group(0) + " не объявлена.f" + str(number_of_command)      
    right = " ".join(right.split())
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
    

    right = " ".join(commands[1].split())
  
    return complited_right_part(right, number_of_command)


def command_processing(commands, number_of_command):
    if commands[0] != "ввод":
        return  "zОшибка. Звено должно содержать слово ввод. f" + str(number_of_command)
    
    #проверка метки
    try:
        if commands[1].find(":") > -1:
            commands = " ".join(commands)
            commands = re.split(":", commands)
            for command in commands:
                if len(command) == 0 and i != len(command)-1:
                    return "zОшибка. Дублируется \':\' f" + str(number_of_command)
            commands = " ".join(commands)
            commands = commands.split()
        else:
            try:
                if commands[2].find(":") > -1:
                    commands = " ".join(commands)
                    commands = re.split(":", commands)
                    for i,command in enumerate(commands):
                        if len(command) == 0 and i != len(command)-1:
                            return "zОшибка. Дублируется \':\' f" + str(number_of_command) 
                    commands = " ".join(commands)
                    commands = commands.split() 
            except:
                return "zОшибка. После метки должно стоять \":\"f" + str(number_of_command)
    except:
        return "zОшибка. После слова ввод должна идти метка f" + str(number_of_command)

    try:
        commands[1] = str(int(commands[1]))
    except:
        return "zОшибка. Метка должна быть целым числом.f"     
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
            return "zОшибка. Переменная должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)    
    except:
        return "zОшибка. Переменная должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)    
    
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
    except: return  "Программа пуста. "  

    if len(data_list) == 2:
        return  "Программа пуста. " 

    if data_list[1] != 'ввод' and len(data_list) > 2:
        return 'Звено начинается со слова \"Ввод\"'      
    

    del data_list[0], data_list[len(data_list)-1]

   
    data_list = re.split('ввод', " ".join(data_list))
    if len(data_list) > 1:
        for i in range(1,len(data_list)):
            data_list[i] = "ввод" + data_list[i]
            if data_list[i].find(";") > -1 or i == len(data_list)-1:
                continue
            return "После команды \'" + data_list[i] + "\' должна стоять \';\'"
        del data_list[0]
    else:
        data_list[0] = 'ввод ' + data_list[0]      
    data_list = " ".join(data_list)
    data_list = re.split(";", data_list) 
    for i in range(len(data_list)): 
        data_list[i] = " ".join(data_list[i].split())   
    output = 'Результаты выполнения программы: '
    for i, command in enumerate(data_list):
        command = " ".join(command.split())
        output += command_processing(command.split(), i) + " "
    return " ".join(output.split())


    


if __name__ == '__main__':
    print(check_for_errors('Программа 42:а455 = [[455 + 3]] + 350 конец'))    
   # print(check_for_errors('Программа Ввод 42:А565 = 5 * 5 + 20 конец'))
    #print(check_for_errors('Программа Ввод 55:А565 = 5 / 5; ввод 55: ф455 = 6 + а565; ввод 6: к666 = 7 + а565 + ф455 + 100 конец'))