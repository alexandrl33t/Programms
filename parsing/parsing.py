
from dataclasses import replace
from doctest import OutputChecker
from logging import exception
import string
from unicodedata import digit
import re




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
                return "zОшибка. Переменной " + m.group(0) + " не существует.f" + str(number_of_command)    
       
    try: 
        right = eval(right)
    except:
        return "Ошибка"           
    return right

def right_part(commands, number_of_command):
    #отсечение правой части 
    try:
        if commands[3].find("=") > -1:
            commands = " ".join(commands)
            commands = re.split("=", commands)
        else:
            return "zОшибка. После переменной должно стоять \"=\"f" + str(number_of_command)
    except:
        return "zОшибка. Неполная командаf" + str(number_of_command)

    right = " ".join(commands[1].split())
    answer = ''
  
    return complited_right_part(right, number_of_command)

def toInt(command):
    try:
        command = int(command)
        return str(command)
    except: 
        return "zОшибка. Метка должна быть целым числом. f"

def command_processing(commands, number_of_command):
    if commands[0] != "ввод":
        return  "zОшибка. Звено должно содержать слово ввод. f" + str(number_of_command)
    
    #проверка метки
    try:
        if commands[1].find(":") > 0:
            commands = " ".join(commands)
            commands = re.split(":", commands)
            commands = " ".join(commands)
            commands = commands.split()
        else:
            return "zОшибка. После метки должно стоять \":\"f" + str(number_of_command)
    except:
        return "zОшибка. После слова ввод должна идти метка f" + str(number_of_command)

    try:
        commands[1] = toInt(commands[1])
    except:
        return "zОшибка. Неполная команда.f"    

   #проверка переменной
    try:
        m = re.search('[а-я][0-7][0-7][0-7]', str(commands[2]))
        if m.group() and len(commands[2]) != 4:
            return "zОшибка. Переменная должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)    
    except:
        return "zОшибка. Переменная должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(number_of_command)    
    
    memory[commands[2]] = right_part(commands, number_of_command)
    print(memory)
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

    if data_list[1] != 'ввод' and len(data_list) > 2:
        return 'Звено начинается со слова \"Ввод\"'
    
    del data_list[0], data_list[len(data_list)-1]
    try:
        data_list = re.split(';', " ".join(data_list))
    except:
        data_list = re.split('ввод', " ".join(data_list))
        if len(data_list) > 1:
            return "После команды " + data_list[0] + " должна стоять \';\'"
        else:
            data_list[0] = 'ввод ' + data_list[0]
    output = ''
    for i, command in enumerate(data_list):
        command = " ".join(command.split())
        output += command_processing(command.split(), i) + " "
    
    if output.find("z") > -1:
        output = output[output.find("z")+1:output.find("f")]
    return " ".join(output.split())


    


if __name__ == '__main__':
    #print(check_for_errors('Программа Ввод 42:А565 = 5 * 5 + ф455 ввод 55: ф455 = 6 ввод 6: к666 = 7 конец'))    
    #print(check_for_errors('Программа Ввод 42:А565 = 5 * 5 + ф455 конец'))
    print(check_for_errors('Программа Ввод 4:А565 = 5 + (5 * 5); ввод 55: ф455 = 6 * а565; ввод 6: к666 = 7 конец'))