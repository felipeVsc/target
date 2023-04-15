def fibo(n):
    
    lista = [0,1]
        
    for x in range(2,n+1):
        soma = lista[x-1]+lista[x-2]

        if soma == n:
            return True
            
        lista.append(soma)    

    return False

numero = int(input("Qual o numero desejado? "))
print(f'O numero pertence a fibonacci? {fibo(numero)}')




        
