vetjogo = []
cont = 0
valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
valor6 = 0
	
for cont in range(20):
    print(cont)
    num = input("Informe o n�mero tirado no dado(de 1 a 6):\n--")
    num = int(num)
    vetjogo.append(num)

    if(vetjogo[cont] == 1):
        valor1+=1
        
    elif(vetjogo[cont] == 2):
        valor2+=1
    
    elif(vetjogo[cont] == 3):
        valor3+=1
    
    elif(vetjogo[cont] == 4):
        valor4+=1
    
    elif(vetjogo[cont] == 5):
        valor5+=1
    
    elif(vetjogo[cont] == 6):
        valor6+=1
    
print(vetjogo)
print("N�mero 1 foi tirado",valor1, 'vezes.\n')
print("N�mero 2 foi tirado",valor2, 'vezes.\n')
print("N�mero 3 foi tirado",valor3, 'vezes.\n')
print("N�mero 4 foi tirado",valor4, 'vezes.\n')
print("N�mero 5 foi tirado",valor5, 'vezes.\n')
print("N�mero 6 foi tirado",valor6, 'vezes.\n')