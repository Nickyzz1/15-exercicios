codtime = 0
nome = []
idadesoma = 0
cont = 0
media = 0
numtimes = 0

codtime = input("Qual o C�digo do seu Time:\n")
codtime = int(codtime)

while(codtime > 0):
    
    for cont in range(3):
        
        nome = input("Qual seu Nome:\n")
        
        idade = input("Qual sua idade:\n")
        idade = int(idade)
        
        print(f"Obrigado pelo cadastro {nome}\n\n")
        idadesoma = idadesoma + idade
    
    numtimes+=1
    media = idadesoma / 3
    print(f"A media de idade deste time � de {media} anos.\n")
    print(f"{numtimes}� time calculado.\n\n")
    
    idadesoma = 0
    
    print(f"\nO n�mero de times cadastrados � de : {numtimes} times.\n\n")
