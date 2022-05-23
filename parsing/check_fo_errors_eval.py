import re

def check_quad(string_for_eval):
    if string_for_eval.find('[') >-1:
        if string_for_eval.rfind(']') > string_for_eval.find('['):
            string2 = string_for_eval[string_for_eval.find('[')+1:string_for_eval.rfind(']')]
            if string2.find('[') >-1:
                if string2.rfind(']') > string2.find('['):
                    string2 = string2[string2.find('[')+1:string2.rfind(']')]
                    if string2.find('[') >-1:
                        return "zОшибка. Максимальная глубина вложенности у квадратных скобок - 2f"
                    elif string2.find(']') >-1:
                        return "zОшибка. Отсутствует открывающая скобка \'[\'f"    
                    else: 
                        string_for_eval = string_for_eval.replace('[', '(')
                        string_for_eval = string_for_eval.replace(']', ')')
                else: return "zОшибка. Отсутствует закрывающая скобка \']\'f"
            elif string2.find(']') >-1:
                 return "zОшибка. Отсутствует открывающая скобка \'[\'f"
            else:
                string_for_eval = string_for_eval.replace('[', '(')
                string_for_eval = string_for_eval.replace(']', ')') 
        elif string2.find(']') >-1:
             return "zОшибка. Отсутствует открывающая скобка \'[\'f"                        
        else: return "zОшибка. Отсутствует закрывающая скобка \']\'f"
    return string_for_eval       

def check(string_for_eval):
    string_for_eval = " ".join(string_for_eval.split())
    string2 = "".join(string_for_eval.split())
    regex = '[0-9\+|\-|\*|\/|\&|\||\(|\)|\[|\]|\^]'
    pattern = re.compile(regex)
    for letter in string2:
        if not pattern.search(letter):
            return "zОшибка. Строка не должна содеражть \'" + letter + "\'f" 
    del string2   

      
    #проверка правильно ли расставлены скобки
    if string_for_eval.find('(')>-1:
        if string_for_eval.find(')')>-1 and string_for_eval.find(')') > string_for_eval.find('('):
            string_inside = string_for_eval[string_for_eval.find('('):string_for_eval.rfind(')')+1] 
            if len(string_inside) > 2:
                if check(string_inside[1:len(string_inside)-1]) == True: 
                    string_for_eval = string_for_eval.replace(string_inside, " 0 ")
                    string_for_eval = " ".join(string_for_eval.split())
                    return check(string_for_eval)
                else: return check(string_inside[1:len(string_inside)-1] ) 
            else: return "zОшибка. Пустое выражение внутри скобок \'()\'f"        
        else: return "zОшибка. Отсутствует закрывающая скобка \')\'f"
    elif string_for_eval.find('(') == -1 and string_for_eval.find(')')>-1:
        return "zОшибка. Лишняя скобка \')\'.f"

    regex = '[0-9\-]'
    pattern = re.compile(regex)
    if len(string_for_eval) >0:
        if not pattern.search(string_for_eval[0:1]):
            return "zОшибка. Выражение в правой части не должно начинаться с \'" + string_for_eval[0:1] + "\' . f"
    else: 
        return "zОшибка. В правой части ничего нет.f"       
    regex = '[0-9]'
    pattern = re.compile(regex)
    if not pattern.search(string_for_eval[len(string_for_eval)-1:len(string_for_eval)]):
        return "zОшибка. Выражение в правой части не должно заканчиваться с \'" + string_for_eval[len(string_for_eval)-1:len(string_for_eval)] + "\' . f"
    
    #проверка есть ли две операции вместе
    without_signs = re.split('\+|\-|\*|\/|\&|\|', string_for_eval)   
    for i in range(1,len(without_signs)-1):
        without_signs[i] = "".join(without_signs[i].split())
        if len(without_signs[i]) == 0:
            return "zОшибка. Две оперции не могут идти подряд. f"     
    del without_signs        
    #проверка есть ли две цифры подряд           
    string_for_eval_massive = string_for_eval.split()
    try:
        for i in range(1,len(string_for_eval_massive)):
            if string_for_eval_massive[i-1].isdigit() and string_for_eval_massive[i].isdigit():
                return "zОшибка. Два числа не могут идти подряд. f"    
    except:
        return True                     
    return True 


if __name__ == '__main__':
    print(check('6 + [[1+2]+30]'))