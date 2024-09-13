
num_id = 0
idade = 0
cont = 0
nota = 0
media = 0 
somadasnotas = 0
conceito  = ''
alunosA = 0
alunosE = 0
alunos = 0

num_id = input("DIGITE SUA IDENTIFICA��O PARA INFORMAR AS NOTAS OU 0 PARA SAIR\n\n")
num_id = int(num_id)
while(num_id != 0):

    for cont in range(12):
        nota = input(f"Qual sua {cont + 1}� nota( de 0 a 100):\n")
        nota = int(nota)
    
    somadasnotas = somadasnotas + nota
    alunos+= 1
    media = somadasnotas / 12

    print(f"Sua ID � {id}\n")
    print(f"Sua m�dia � = {media}\n")

    if(media >= 90):
        conceito = 'A'
        alunosA+=1
        print(f"Conceito = {conceito}\n\n")

    else:
        if(media >= 75 and media < 90):
            conceito = 'B'
            print(f"Conceito = %{conceito}\n\n")

        else:
            if(media >= 60 and media < 75):
                    conceito = 'C'
                    print(f"Conceito = %{conceito}\n\n")
            
            else:
                if(media >= 40 and media < 60):
                    conceito = 'D'
                    print(f"Conceito = %{conceito}\n\n")
                else:
                    if(media < 40):
                            conceito = 'E'
                            alunosE+=1
                            print(f"Conceito = %{conceito}\n\n")

            num_id = input("DIGITE SUA IDENTIFICA��O PARA INFORMAR AS NOTAS OU 0 PARA SAIR\n")
            num_id = int(num_id)

            somadasnotas = 0	

        print("%d aluno(s) calculados\n",alunos)
        print("%d aluno(s) tiraram A\n",alunosA)
        print("%d aluno(s) tiraram E\n",alunosE)

