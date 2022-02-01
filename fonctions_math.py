
def polynome(x):
    '''  fonction polynome voir formule de l'énoncé'''
    y= (x**3) - 1.5*(x**2) - 6*x + 5
    return y

# appel de la fonction pour vérification
print(polynome(5))

def factorielle(x):
    '''fonction récursive factorielle'''
    if x==1:
        return 1
    else:
        y=1
        for i in range(1, x+1):
            #print(y)
            y=y*i
        return y
    
# test fonction factorielle
print(factorielle(5))


def fibonacci():
    ''' fonction suite de Fibonacci '''
    print('Saisir un nombre')
    x=int(input())
    fibo=[0,1]  
    for i in range(2,x):
        fibo.append(fibo[-1]+fibo[-2])
    
    print('La suite de Fibonacci pour '+str(x)+' est '+str(fibo))
    
# test de la fonction
fibonacci()
