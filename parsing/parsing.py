
from doctest import OutputChecker
from logging import exception
import string
from unicodedata import digit
import re

output = "" 

def toInt(command):
    try:
        command = int(command)
        return str(command)
    except: 
        return "zОшибка. Метка должна быть целым числом. f"

def command_processing(commands, number_of_command):
    if commands[0] != "ввод":
        output =  "zОшибка. Звено должно содержать слово ввод. f" + str(number_of_command)
    

    if commands[1].find(":") > 0:
        commands = " ".join(commands)
        commands = re.split(":", commands)
        commands = " ".join(commands)
        commands = commands.split()
    else:
        return "zОшибка. После метки должно стоять \":\"f " + str(number_of_command)
    m = re.search('[0-9]*', str(commands[1]))
    try:
        m.group(0)
    except:
        return "zМетка должа быть целым числомf"
   
    commands = " ".join(commands)
    commands = commands.split()  
    m = re.search('[а-я][0-7][0-7][0-7]', str(commands[2]))
    try:
        if m.group() and len(commands[2]) != 4:
            return "zОшибка. Переменная должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)    
    except:
        return "zОшибка. Переменная должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)    
    
    return " ".join(commands)    

def check_for_errors(data):
    data = data.lower()
    data_list = data.split()
    try:
        if data_list[0] != "программа":
            return  "Ошибка. Программа должна начинаться со слова ""Программа"""
        elif data_list[len(data_list)-1] != "конец":
            return  "Ошибка. Программа, должна заканчиваться словом ""Конец""" 
    except: return  "Программа пуста. "  
    output =""
    first_command = 1
    number_of_command = 1
    for i in range(1,len(data_list)-1):
        last_command = len(data_list)-2
        if set(';+$').intersection(data_list[i]):
            data_list[i] = data_list[i][0:len(data_list[i])-1]
            last_command = i
            output += command_processing(data_list[first_command:last_command+1], number_of_command) + " "
            first_command = i+1  
            number_of_command +=1
            continue
        if i == len(data_list)-2:
            output += command_processing(data_list[first_command:len(data_list)-1], number_of_command) + " "
            number_of_command +=1  
    if output.find("z") > -1:
        print(output[output.find("f"):len(output)])
        output = output[output.find("z")+1:output.find("f")]
    return " ".join(output.split())


    


if __name__ == '__main__':
    print(check_for_errors('Программа Ввод 42s: А565 = ; ввод 55: ф455; ввод 6: к666 конец'))    
    