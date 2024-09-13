inicio = 0
presidente = []
governador = 0
voto = 0

for cont in range(15):
    presidente[cont].append(0)
    if (cont < 12):
        governador[cont].append(0)
inicio = input("digite s para votar e n para sair")

while (inicio.lower() != 'n') :
    if (inicio.lower() == 's') :

        # Vota��o para presidente.
        voto = input("\nInforme seu voto para a presid�ncia:\n--")

        match voto: 
            case 0:
                presidente[0].append(presidente[0] + 1)
                print("\nVoc� votou branco.")
                break
            case 1:
                presidente[1].append(presidente[1] + 1)
                print("\nVoc� votou em Alvaro Dias (Podemos).")
                break
            case 2:
                presidente[2].append(presidente[2] + 1)
                print("\nVoc� votou em Cabo Daciolo (Patriota).")
                break
            case 3:
                presidente[3].append(presidente[3] + 1)
                print("\nVoc� votou em Ciro Gomes (PDT).")
                break
            case 4:
                presidente[4].append(presidente[4] + 1)
                print("\nVoc� votou em Eymael (DC).")
                break
            case 5:
                presidente[5].append(presidente[5] + 1)
                print("\nVoc� votou Fernando Haddad (PT).")
                break
            case 6:
                presidente[6].append(presidente[6] + 1)
                print("\nVoc� votou em Geraldo Alckmin (PSDB).")
                break
            case 7:
                presidente[7].append(presidente[7] + 1)
                print("\nVoc� votou em Guilherme Boulos (PSOL).")
                break
            case 8:
                presidente[8].append(presidente[8] + 1)
                print("\nVoc� votou em Henrique Meirelles (MDB).")
                break
            case 9:
                presidente[9].append(presidente[9] + 1)
                print("\nVoc� votou em Jair Bolsonaro (PSL).")
                break
            case 10:
                presidente[10].append(presidente[10] + 1)
                print("\nVoc� votou em Jo�o Amoedo (Novo).")
                break
            case 11:
                presidente[11].append(presidente[11] + 1)
                print("\nVoc� votou em Jo�o Vicente Goulart (PPL).")
                break
            case 12:
                presidente[12].append(presidente[12] + 1)
                print("\nVoc� votou em Marina Silva (REDE).")
                break
            case 13:
                presidente[13].append(presidente[13] + 1)
                print("\nVoc� votou em Vera L�cia (PSTU).")
                break
            case 14:
                presidente[14].append(presidente[14] + 1)
                print("\nVoc� votou nulo.")
                break
            case _:
                print("\nN�mero invalido.")
                break
            

        # Vota��o para governador.
        voto - input("\nInforme seu voto para governador(a): ")

        match voto:
            case 0:
                governador[0] = governador[0] + 1
                print("\nVoc� votou branco.")
                break
            case 1:
                governador[1] = governador[1] + 1
                print("\nVoc� votou em Cida Borghetti (Progressista).")
                break
            case 2:
                governador[2] = governador[2] + 1
                print("\nVoc� votou em Doutor Rosinha (PT).")
                break
            case 3:
                governador[3] = governador[3] + 1
                print("\nVoc� votou em Geon�sio Marinho (PRTB).")
                break
            case 4:
                governador[4] = governador[4] + 1
                print("\nVoc� votou em Jo�o Arruda (MDB).")
                break
            case 5:
                governador[5] = governador[5] + 1
                print("\nVoc� votou Jorge Bernardi (REDE).")
                break 
            case 6:
                governador[6] = governador[6] + 1
                print("\nVoc� votou em Ogier Buchi (PSL).")
                break
            case 7:
                governador[7] = governador[7] + 1
                print("\nVoc� votou em Priscila Ebara (PCO).")
                break
            case 8:
                governador[8] = governador[8] + 1
                print("\nVoc� votou em Professor Ivan Bernardo (PSTU).")
                break
            case 9:
                governador[9] = governador[9] + 1
                print("\nVoc� votou em Professor Piva (PSOL).")
                break
            case 10:
                governador[10] = governador[10] + 1
                print("\nVoc� votou em Ratinho Junior (PSD).")
                break
            case 11:
                governador[11] = governador[11] + 1
                print("\nVoc� votou nulo.")
                break
            case _:
                print("\nN�mero invalido.")
                break
            

        # Repeti��o do La�o
        inicio = input("\nDigite 'S' para votar ou 'N' para sair e exibir os resultados.")
       
    else:
        # Para entradas diferentes de 'S', 's', 'N' e 'n'
        incio = input("\nDigite 'S' para votar ou 'N' para sair e exibir os resultados.")
      


        # Exibi��o da contagem de votos para a presid�ncia
        print(f"\n\nContagem de votos para a presid�ncia:")
        print(f"\n     - Alvaro Dias (Podemos): {presidente[1]}", )
        print(f"\n     - Cabo Daciolo (Patriota): {presidente[2]}")
        print(f"\n     - Ciro Gomes (PDT): {presidente[3]}")
        print(f"\n     - Eymael(DC): {presidente[4]}")
        print(f"\n     - Fernando Haddad (PT): {presidente[5]}" )
        print(f"\n     - Geraldo Alckmin (PSDB): {presidente[6]}")
        print(f"\n     - Guilherme Boulos (PSOL): {presidente[7]}")
        print(f"\n     - Henrique Meirelles (MDB): {presidente[8]}")
        print(f"\n     - Jair Bolsonaro (PSL): {presidente[9]}")
        print(f"\n     - Jo�o Amo�do (Novo): {presidente[10]}")
        print(f"\n     - Jo�o Vicente Goulart (PPL): {presidente[11]}")
        print(f"\n     - Marina Silva (Rede): {presidente[12]}")
        print(f"\n     - Vera L�cia (PSTU): {presidente[13]}")
        print(f"\n")
        print(f"\n     - Votos Brancos: {presidente[0]}")
        print(f"\n     - Votos Nulos: {presidente[14]}")



        # C�lculo e exibi��o do(a) vencedor(a) para a presid�ncia
        max = 1
        empate = 0

        for cont in range(14): # cont=1 e cont<14 para deixar de lado votos brancos e nulos

            if (presidente[cont] > presidente[max]) :
                max = cont
            else :
                if (presidente[cont] == presidente[max]):
                    empate = cont

        # Para vencedor �nico:
        if (max > empate) :
            match max:
                case 1:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Alvaro Dias (Podemos), com {presidente[1]} votos." )
                    break
                case 2:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Cabo Daciolo (Patriota) com { presidente[2]} votos.")
                    break
                case 3:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Ciro Gomes (PDT) com {presidente[3]} votos." )
                    break
                case 4:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Eymael (DC) com {presidente[4]} votos." )
                    break
                case 5:
                    print(f"\n\nVoc� votou Fernando Haddad (PT) com {presidente[5]} votos." )
                    break
                case 6:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Geraldo Alckmin (PSDB) com {presidente[6]} votos." )
                    break
                case 7:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Guilherme Boulos (PSOL) com {presidente[7]} votos." )
                    break
                case 8:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Henrique Meirelles (MDB) com {presidente[8]} votos." )
                    break
                case 9:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Jair Bolsonaro (PSL) com {presidente[9]} votos.")
                    break
                case 10:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Jo�o Amoedo (Novo) com {presidente[10]} votos." )
                    break
                case 11:
                    print(f"\n\nO pr�ximo presidente da rep�blica ser� Jo�o Vicente Goulart (PPL) com {presidente[11]} votos." )
                    break
                case 12:
                    print(f"\n\nA pr�xima presidenta da rep�blica ser� Marina Silva (REDE) com {presidente[12]} votos." )
                    break
                case 13:
                    print(f"\n\nA pr�xima presidenta da rep�blica ser� Vera L�cia (PSTU) com {presidente[13]} votos." )
                    break
        
        # Em caso de empate
        else:
            if (max == empate):
                print("a")
                print("b")


    #trabalho_vetor reposit 2