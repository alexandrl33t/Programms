def check_for_errors(data):
    data = data.lower()
    data_list = data.split()
    try:
        if data_list[0] != "программа":
            return "Ошибка. Программа должна начинаться со слова ""Программа"""
        elif data_list[len(data_list)-1] != "конец":
            return "Ошибка. Программа, должна заканчиваться словом ""Конец""" 
    except: return "Программа пуста. "  

    for i in (1,len(data_list)-1):
        last_command = 1
        if data_list[i].find(";") > -1:
            last_command = i
            


    return ""      


if __name__ == '__main__':
    print(check_for_errors('Программа ыЫы ЫЫфФмвыЫВ'))    
    