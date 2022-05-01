
def command_processing(commands):
    
    return commands    

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
            return "Ошибка. Программа должна начинаться со слова ""Программа"""
        elif data_list[len(data_list)-1] != "конец":
            return "Ошибка. Программа, должна заканчиваться словом ""Конец""" 
    except: return "Программа пуста. "  


    for i in range(1,len(data_list)-1):
        first_command = 1
        last_command = len(data_list)-2
        if isTochka_zapyataya(data_list[i]):
            data_list[i] = data_list[i][0:len(data_list[i])-1]
            last_command = i
            print(command_processing(data_list[first_command:last_command+1]))

    return data_list    


    


if __name__ == '__main__':
    print(check_for_errors('Программа ввод строка1; ввод строка2 конец'))    
    