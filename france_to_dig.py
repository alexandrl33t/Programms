digits = {'un' : 1, 'deux' : 2, 'trois' : 3, 
'quatre': 4, 'cinq':5, 'six':6, 'sept':7,'huit':8, 'neuf':9, 'dix':10, 
'onze':11, 'douze':12, 'treize':13, 'quatorze':14, 'quinze':15, 
'seize':16, 'dix-sept':17, 'dix-huit':18, 'dix-neuf':19, 'vingt':20,
'trente':30, 'quarante':40, 'cinquante':50, 'soixante':60,'quatre-vingts':80,
'cent':100}

def to_rim(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result

def razryad(a):
    k = 0
    while (a>0):
        k +=1
        a //=10
    return k    


def to_dig(string):
    words=string.split()
    f_nums = []
    words = [word.lower() for word in words]

    if digits.get(words[-1]) != None:
            f_nums.append(digits.get(words[-1])) 
    else: 
        return 'Синтаксическая ошибка'             
    for i in range(len(words)-2, -1, -1):
        if digits.get(words[i]) == None:
            return 'Синтаксическая ошибка'
        else:
            if razryad(digits.get(words[i])) -  razryad(digits.get(words[i+1])) > 0 and digits.get(words[i]) > 19:
               f_nums.append(digits.get(words[i]))
            else:
                if razryad(digits.get(words[i+1])) == 3 and razryad(digits.get(words[i])) == 1:
                   f_nums[-1] = digits.get(words[i]) * digits.get(words[i+1])
                   if i ==0:
                       return str(sum(f_nums)) + ' или ' + str(to_rim(sum(f_nums)))
                   else:
                       return 'Лексическая ошибка'       
                elif digits.get(words[i+1]) < 20 and (digits.get(words[i]) == 80 or digits.get(words[i]) == 60):
                    f_nums[-1] = digits.get(words[i]) + digits.get(words[i+1])   
                else:
                   return 'Лексическая ошибка'    
    return str(sum(f_nums)) + ' или ' + str(to_rim(sum(f_nums)))               

    
                                                     
                 


if __name__=='__main__':
    print(to_dig('cinq cent quatre-vingts dix'))
