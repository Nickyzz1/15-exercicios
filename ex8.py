# Inicialização
presidente = [0] * 15
governador = [0] * 12

inicio = input("Digite 'S' para votar e 'N' para sair: ")

while inicio.lower() != 'n':
    if inicio.lower() == 's':
        try:
            voto = int(input("\nInforme seu voto para a presidência (0 a 14): "))
            if 0 <= voto < 15:
                presidente[voto] += 1
                print(f"\nVocê votou em candidato número {voto}.")
            else:
                print("\nNúmero inválido.")
        except ValueError:
            print("\nEntrada inválida. Por favor, insira um número.")

        try:
            voto = int(input("\nInforme seu voto para governador(a) (0 a 11): "))
            if 0 <= voto < 12:
                governador[voto] += 1
                print(f"\nVocê votou em candidato número {voto}.")
            else:
                print("\nNúmero inválido.")
        except ValueError:
            print("\nEntrada inválida. Por favor, insira um número.")
        
        inicio = input("\nDigite 'S' para votar ou 'N' para sair e exibir os resultados: ")
    else:
        inicio = input("\nDigite 'S' para votar ou 'N' para sair e exibir os resultados: ")

print(f"\n\nContagem de votos para a presidência:")
for i in range(15):
    print(f"\n     - Candidato {i}: {presidente[i]}")
print(f"\n     - Votos Brancos: {presidente[0]}")
print(f"\n     - Votos Nulos: {presidente[14]}")

max_votos_presidente = max(presidente[1:14])  
vencedor_presidente = [i for i in range(1, 14) if presidente[i] == max_votos_presidente]

if len(vencedor_presidente) == 1:
    print(f"\nO próximo presidente da república será o candidato número {vencedor_presidente[0]} com {max_votos_presidente} votos.")
else:
    print(f"\nHouve empate entre os candidatos: {vencedor_presidente} com {max_votos_presidente} votos.")

print(f"\n\nContagem de votos para governador(a):")
for i in range(12):
    print(f"\n     - Candidato {i}: {governador[i]}")

max_votos_governador = max(governador)
vencedor_governador = [i for i in range(12) if governador[i] == max_votos_governador]

if len(vencedor_governador) == 1:
    print(f"\nO próximo governador(a) será o candidato número {vencedor_governador[0]} com {max_votos_governador} votos.")
else:
    print(f"\nHouve empate entre os candidatos: {vencedor_governador} com {max_votos_governador} votos.")
