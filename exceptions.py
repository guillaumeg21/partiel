
# gestion des exceptions sur la fonction Fibonacci


def fibonacci():
    ''' fonction suite de Fibonacci '''
    try:
        print('Saisir un nombre entier supérieur à 1:')
        x=int(input())
        # l'utilisateur doit saisir un nombre supérieur à 1
        if x<=1:
            raise Exception("Vous devez saisir un nombre supérieur à 1.")
        # l'utilisateur doit saisir un nombre inférieur ou égal à 1000
        if x>1000:
            raise Exception("Vous avez saisi un nombre trop grand.")
        fibo=[0,1]  
        for i in range(2,x):
            fibo.append(fibo[-1]+fibo[-2])
        
        print('La suite de Fibonacci pour '+str(x)+' est '+str(fibo))
    except ValueError:
        #  l'utilisateur doit saisir un nombre entier, les chaînes ne pouvant être converties sont refusées
        print("Vous devez saisir un nombre entier")
   
# test de la fonction
fibonacci()
