lanche  = 0
bebida = 0
pagar = 0
cod1 = input("QUAL O CODIGO DO SEU SANDUICHE: \n")
cod2 = input("QUAL O CODIGO DA SUA BEBIDA: \n")
cod1 = int(cod1)
cod2 = int(cod2)

match cod1:
    case 100:
        lanche = 1.20	
        print(" \n R$ 1.20 \n")
    case 101:
        lanche = 1.30
        print(" \n R$ 1.30 \n")
    case 102:
        lanche = 1.50
        print(" \n R$ 1.50 \n")
    case 103:
        lanche = 1.70
        print(" \n R$ 1.70 \n")
    case _:
        print("COD INCORRETO \n")

match cod2:
    case 201:
        bebida = 1.20
        print(" \n R$ 1.20 \n")
    case 202:
        bebida = 1.50
        print(" \n R$ 1.50 \n")
    case 203:
        bebida = 0.70
        print(" \n R$ 0.70 \n")
    
    case _:
        print("COD INCORRETO \n")
pagar = lanche+bebida

print("\nTOTAL A PAGAR:\n",pagar)

#exercicio9aulapratica