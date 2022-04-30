
def command_processing(commands):
    if commands[0] != "ввод":
        return Ошибка 

def check_for_errors(data):
    data = data.lower()
    data_list = data.split()
    try:
        if data_list[0] != "программа":
            return "Ошибка. Программа должна начинаться со слова ""Программа"""
        elif data_list[len(data_list)-1] != "конец":
            return "Ошибка. Программа, должна заканчиваться словом ""Конец""" 
    except: return "Программа пуста. "  

    first_command = 1 #левая граница строки с командой
    last_command = len(data_list)-2 #правая граница строки с командной


    """цикл идет до первой встречной точки с запятой и обрабатывает команду до этой точки с запятой 
    методом command_processing"""
    for i in range(1,len(data_list)-1):
        for num,char in enumerate(data_list[i]):
            if char == ';':
                last_command = i
                data_list[i] = data_list[i][0:num]            
        print(command_processing(data_list[first_command:last_command+1]))
        first_command = i+1

    return ""

    


if __name__ == '__main__':
    print(check_for_errors('Программа конец'))    
    