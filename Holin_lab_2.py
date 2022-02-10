def RAND(a,b,m,x_i): 
    return a*x_i+b // m 


if __name__ == '__main__':
    a = 22695477
    b = 1
    m=pow(2,32)
    x_i = 1
    print(RAND(a, b,m,x_i))


