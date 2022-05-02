
from doctest import OutputChecker
import string
from unicodedata import digit

output = "" 

def toInt(command):
    try:
        command = int(command)
        return str(command)
    except: 
        output = "zОшибка. Метка должна быть целым числом. f"

def command_processing(commands, number_of_command):
    if commands[0] != "ввод":
        output =  "zОшибка. Звено должно содержать слово ввод. f" + str(number_of_command)
    if commands[1][0:1] == ":" and len(commands[1]) > 2:
        commands[1] = commands[1][0:len(commands[1])-1]
        return toInt(commands[1]) + " " + str(number_of_command)
    elif commands[2][0:1] == ":" and len(commands[2]) > 2: 
        commands[2] = commands[2][1:len(commands[2])-1]
        return toInt(commands[1])+ " " + str(number_of_command)
    elif commands[2] == ":":
        del commands[2]    
    elif set(":").intersection(commands[1]) == False or  set(":").intersection(commands[2]) == False:       
        output = "zОшибка. После метки должно стоять \":\"f" + str(number_of_command)     


   


    
    return " ".join(commands)    

def isTochka_zapyataya(word):
    for num,char in enumerate(word):
            if char == ';':
                return True
    return False

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
        output = output[output.find("z")+1:output.find("f")]
    return " ".join(output.split())


    


if __name__ == '__main__':
    print(check_for_errors('Программа Ввод 4 : строка1; ввод 5 строка2; ввод 6 строка3 конец'))    
    