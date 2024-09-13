id = 0
n1=0
n2=0
n3=0
media=0
conceito = ''

ident =input("QUAL NUMERO DA IDENTIFICA��O DO ALUNO:")
n1 =input("QUAL A PRIMEIRA NOTA:")
n2 =input("QUAL A SEGUNDA NOTA:")
n3 =input("QUAL A TERCEIRA NOTA:")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

media = (n1+n2+n3 )/ 3

if media >= 90:
    conceito = 'A'
    print(f"APROVADO conceito:{conceito} \n COM O ID: {id} \n COM AS NOTAS: {n1}, {n2} ,{n3} \n COM A MEDIA: {media} \n")

else:
    if media >=75:
        conceito = 'B'
        print(f"APROVADO conceito:{conceito} \n COM O ID: {id} \n COM AS NOTAS: {n1}, {n2} ,{n3} \n COM A MEDIA: {media} \n")

    else:
        if media >=60:
            conceito = 'C'
            print(f"APROVADO conceito:{conceito} \n COM O ID: {id} \n COM AS NOTAS: {n1}, {n2} ,{n3} \n COM A MEDIA: {media} \n")
        
        else:
            if media>=40:
                conceito = 'D'
                print(f"REPROVADO conceito:{conceito} \n COM O ID: {id} \n COM AS NOTAS: {n1}, {n2} ,{n3} \n COM A MEDIA: {media} \n")
            
            else:
                conceito = 'E'
                print(f"REPROVADO conceito:{conceito} \n COM O ID: {id} \n COM AS NOTAS: {n1}, {n2} ,{n3} \n COM A MEDIA: {media} \n")
                
# iflista6 reposit 1