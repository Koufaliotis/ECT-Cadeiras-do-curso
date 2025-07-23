def fibonacci(n):

    varType = type(1) 
    
    if type(n) != type(1):
        print("ERROR THE NUBER ISNT INT TYPE")
        return "ERROR THE NUBER ISNT INT TYPE"
    else:
        print("VAR TYPE VALID")
        
    res = [0,1]
    if n < 0:
        print("chose betwin the first elemant of fibonacvi is 0")
        return res[0]
    elif n == 0 :
        return res
    res.append(1)
    while len(res) < n + 2:
        nextElement = res[-1] +res[-2]
        res.append(nextElement)

    return res
    
def teste1():
    if fibonacci(0) == [0] and fibonacci(-1) == []:
        print("Teste OK")
        
    else:
        print("Teste Falhou")   
       # print(fibonacci(0),fibonacci(-1))

#teste1()