from dataclasses import replace
from doctest import OutputChecker
from logging import exception
from ntpath import join
import string
from unicodedata import digit
import re
import check_fo_errors_eval as cf



memory = {}

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
            print(perem)
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