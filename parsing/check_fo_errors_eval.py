import re
def check(string_for_eval):
    string_for_eval = " ".join(string_for_eval.split())
    if string_for_eval.find('(')>-1:
        if string_for_eval.find(')')>-1 and string_for_eval.find(')') > string_for_eval.find('('):
            string_inside = string_for_eval[string_for_eval.find('('):string_for_eval.rfind(')')+1] 
            if len(string_inside) > 2:
                if check(string_inside[1:len(string_inside)-1]) == True: 
                    string_for_eval = string_for_eval.replace(string_inside, " 0 ")
                    string_for_eval = " ".join(string_for_eval.split())
                    print(string_for_eval)
                    return check(string_for_eval)
                else: return check(string_inside[1:len(string_inside)-1] ) 
            else: return "zОшибка. Пустое выражение внутри скобок. f"        
        else: return "zОшибка. Отсутствует закрывающая скобка.f"
    elif string_for_eval.find('(') == -1 and string_for_eval.find(')')>-1:
        return "zОшибка. Лишняя скобка \')\'.f"

    string_for_eval = re.split('\+|\-|\*|\/|\&|\|\|', string_for_eval)
    return string_for_eval      
    return True 


if __name__ == '__main__':
    print(check('5 & || 5'))