cod = 0
dep = 0
salB = 0
salL = 0
salIR = 0
valorINSS = 0
valorIR = 0
somaINSS = 0
somaIR = 0
        
cod =input("Digite o c�digo do funcion�rio: ")
cod = float(cod)
while (cod != 0):
    dep = input("Digite o Numero de Dependentes: ")
    dep = int(dep)

    for x in range(12):
        salB=input(f"Digite o {x+1} Salario Bruto\n= ")
        salB = float(salB)

        if(salB<=1399.12):
            valorINSS = salB * 0.08
            somaINSS = somaINSS + valorINSS
            salL = salB - (salB * 0.08)
        
        elif(salB<=2331.88):
            valorINSS = salB * 0.09
            somaINSS = somaINSS + valorINSS
            salL = salB - (salB * 0.09)
                        
        elif(salB<=4663.75):
            valorINSS = salB * 0.11
            somaINSS = somaINSS + valorINSS
            salL = salB - (salB * 0.11)
                        
        else:
            valorINSS = 513.01
            somaINSS = somaINSS + valorINSS
            salL = salB - (513.01) 
        
        if(dep >= 1):
            salIR = salL - (dep * 189.59)           
            
            if(salIR <= 1903.98):
                valorIR = 0
                somaIR = somaIR + valorIR
                
            elif(salIR <= 2826.65):
                valorIR = ((salIR * 0.075) - 142.80)
                somaIR = somaIR + valorIR
                
            elif (salIR <= 3751.05):
                valorIR = ((salIR * 0.15) - 354.80)
                somaIR = somaIR + valorIR
                
            elif (salIR <=4664.68):
                valorIR = ((salIR * 0.225) - 636.13)
                somaIR = somaIR + valorIR
                
            else :
                valorIR = ((salIR * 0.275) - 869.36)
                somaIR = somaIR + valorIR
               
        else: 
            salIR = salL
            
            if(salIR <= 1903.98):
                valorIR = 0
                somaIR = somaIR + valorIR
                
            elif (salIR <= 2826.65):
                valorIR = ((salIR * 0.075) - 142.80)
                somaIR = somaIR + valorIR
                
            elif (salIR <= 3751.05):
                valorIR = ((salIR * 0.15) - 354.80)
                somaIR = somaIR + valorIR
                
            elif (salIR <=4664.68):
                valorIR = ((salIR * 0.225) - 636.13)
                somaIR = somaIR + valorIR
                
            else :
                valorIR = ((salIR * 0.275) - 869.36)
                somaIR = somaIR + valorIR
    
        if(salB<=1399.12):
            salL = (salL - valorIR)
            print(f"Salario Liquido= {salL}\n" )
            print(f"Valor INSS= {valorINSS}\n" )
            print(f"Valor IR= {valorIR}\n\n" )

        elif(salB<=2331.88):
            salL = (salL - valorIR)
            print(f"Salario Liquido= {salL}\n" )
            print(f"Valor INSS= {valorINSS}\n" )
            print(f"Valor IR= {valorIR}\n\n" )
            
                        
        elif(salB<=4663.75):
            salL = (salL - valorIR)
            print(f"Salario Liquido= {salL}\n" )
            print(f"Valor INSS= {valorINSS}\n" )
            print(f"Valor IR= {valorIR}\n\n" )
            
                        
        else :
            salL = (salL - valorIR) 
            print(f"Salario Liquido= {salL}\n" )
            print(f"Valor INSS= {valorINSS}\n" )
            print(f"Valor IR= {valorIR}\n\n")
          

    print(f"Funcion�rio: {cod}\n")
    print(f"Valor no ano a pagar de INSS= {somaINSS}\n")
    print(f"Valor no ano a pagar de IR= {somaIR}\n\n")
    cod = input("Digite o c�digo do funcion�rio: ")

#imposto de renda reposit 1




