def mostra_velha():
    # mostra o status atual do jogo na tela
    print("\n\n")
    print(" 0     1     2 ")
    print("\n")
    print("      |   |   ")
    print(f"0   {tab[0][0]} | {tab[0][1]} | {tab[0][2]}")
    print("   ___|___|___")
    print("      |   |   ")
    print(f"1   {tab[1][0]} | {tab[1][1]} | {tab[1][2]}")
    print("   ___|___|___")
    print("      |   |   ")
    print(f"2   {tab[2][0]} | {tab[2][1]} | {tab[2][2]}")
    print("      |   |   \n\n\n")

def jogadorX(p_jogador):
    while True:
        print(f"{p_jogador}, informe a linha e a coluna da jogada: ")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        if validador(linha, coluna):
            tab[linha][coluna] = 'X'
            mostra_velha()
            if vencedor():
                print(f"{p_jogador} venceu o jogo.")
                return True
            return False

def jogadorO(p_jogador):
    while True:
        print(f"{p_jogador}, informe a linha e a coluna da jogada: ")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        if validador(linha, coluna):
            tab[linha][coluna] = 'O'
            mostra_velha()
            if vencedor():
                print(f"{p_jogador} venceu o jogo.")
                return True
            return False

def validador(p_linha, p_coluna):

    if tab[p_linha][p_coluna] in ['X', 'O']:
        print("\nLugar ocupado. ")
        return False
    elif p_linha > 2 or p_coluna > 2 or p_linha < 0 or p_coluna < 0:
        print("Valor incorreto. ")
        return False
    else:
        return True

def vencedor():
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] and tab[i][0] != 0:
            return True
        if tab[0][i] == tab[1][i] == tab[2][i] and tab[0][i] != 0:
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] != 0:
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] and tab[0][2] != 0:
        return True
    return False

def zerarmatriz():
    global tab
    tab = [[0]*3 for _ in range(3)]

if __name__ == "__main__":
    import locale
    locale.setlocale(locale.LC_ALL, "")

    zerarmatriz()

    jogadorx = input("Informe o nome do jogador 1 (X): ")
    jogadoro = input("Informe o nome do jogador 2 (O): ")

    mostra_velha()

    for cont in range(5):
        if jogadorX(jogadorx):
            break
        if jogadorO(jogadoro):
            break

    if not vencedor():
        print("O jogo empatou.")
