from dataclasses import replace
from doctest import OutputChecker
from logging import exception
from ntpath import join
import string
from unicodedata import digit
import re
import check_fo_errors_eval as cf





class Parsing():
    metka = ''
    perem = ''
    memory = {}
    number_of_command = 1

    def peremError(self, perem):
        return f"zОшибка. Переменная {perem} должна быть формата бццц, где б это А!...!Я, ц это 0!...!7f" + str(self.number_of_command)

    def isOk(self, right):   
        isRight = cf.check(right)
        if isRight == True:
            try:   
                return int(eval(right))
            except ZeroDivisionError:
                    return "zОшибка. Деление на ноль. f" + str(self.number_of_command)      
        else: return isRight + str(self.number_of_command)

    #замена переменных в правой части
    def perem_exchange(self, right):
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
                regex = '[\+|\-|\*|\/|\&|\||\(|\)|\[|\]|\^]'
                if len(perem) == 5:
                    m = re.search(f'[а-я][0-7][0-7][0-7]{regex}', perem)   
                elif len(perem) == 4:
                    m = re.search(f'[а-я][0-7][0-7][0-7]', perem)   
                if not m:
                    return self.peremError(perem) 
                try:
                    if len(perem) == 4:
                        return new_right + str(int(self.memory[perem]))
                    else:
                        perem = right[i:i+4]
                        new_right += str(int(self.memory[perem]))
                        k = 3    
                except:
                    return f"zОшибка. Переменная {perem} не инициализировна.f"
                                                 
            except:     
                    return self.peremError(perem) 
        return new_right        

    #проверка левой части
    def command_processing(self, data, last_word):
        for i in range(len(data)):
            if last_word == ';':
                self.number_of_command +=1
            if last_word == '' or  last_word == ';':
                if data[i:i+4] != 'ввод':
                    return "zОшибка. Звено должно начинаться со слова вводf" + str(self.number_of_command)
                else:
                    return self.command_processing(data[i+4:len(data)], 'ввод')
            elif last_word == 'ввод': 
                if data[i].isdigit():
                    if int(data[i]) < 8:
                        self.metka += data[i]
                        return self.command_processing(data[i+1:len(data)], 'ввод')
                    else:
                        return "zОшибка. В метке используется цифра не воьсмиричной системы.f" + str(self.number_of_command)     
                elif data[i] == ':':
                    return self.command_processing(data[i+1:len(data)], self.metka)
                else:
                    return "zОшибка. Метка должна быть целочисленной.f"
            elif last_word == self.metka:
                self.perem = data[i:i+5]
                m = re.search(f'[а-я][0-7][0-7][0-7]\=', self.perem)
                if not m:
                    m = re.search(f'[а-я][0-7][0-7][0-7]', self.perem)
                    if not m:
                        return self.peremError(self.perem)
                    else: 
                        return "zОшибка. После перемнной должно идти \'=\'f" + str(self.number_of_command)     
                else:
                    self.perem = self.perem[0:4]
                    try:
                        self.memory[self.perem] 
                        return f"zОшибка. Переменная {self.perem} уже инициализировнаf" + str(self.number_of_command) 
                    except KeyError: 
                        data = data[data.find('=')+1:len(data)]
                        tochka = data.find(';')
                        if tochka > -1:
                            right = self.perem_exchange(data[0:tochka])
                            self.memory[self.perem] = self.isOk(right)
                            return self.command_processing(data[tochka+1:len(data)], ';')
                        else: 
                            tochka = data.find('ввод')
                            if tochka > -1:
                                return f"zОшибка. Отсутствует \';\'f" + str(self.number_of_command)
                            right = self.perem_exchange(data[0:len(data)]) 
                            self.memory[self.perem] = self.isOk(right)
                            answer = ''
                            for item in self.memory.values():
                                print(item)
                            return self.memory

    def preparation(self, data):
        data = data.lower()
        data_list = data.split()
        try:
            if data_list[0] != "программа":
                return  "Ошибка. Программа должна начинаться со слова ""Программа"""
            elif data_list[len(data_list)-1] != "конец":
                return  "Ошибка. Программа, должна заканчиваться словом ""Конец""" 
        except: return  "Программа пуста."

        data = "".join(data_list[1:len(data_list)-1])
        data_list = data_list[1:len(data_list)-1]
        if len(data_list) == 0:
            return  "Программа пуста. "    
        
        return self.command_processing(data, '')
        
if __name__ == '__main__':
    a = Parsing()
    #print(a.preparation('Программа ввод 42:а455 = [[455 + 3]] ^ 350 конец'))    
#print(a.preparation('Программа Ввод 42:А565 = 5 * 5 + 20 конец'))
    print(a.preparation('Программа Ввод 55:А565 = 5 / 5; ввод 55: ф455 = 6 + а565; ввод 6: к666 = 7 + а565 + ф455 + 100 конец'))  