class tipo_funcionario():
    def __init__(self, numero, nome,salario_ano, salario_mes = []):
        self.__numero = numero
        self.__nome = nome
        self.__salario_mes = []
        self.__salario_ano = salario_ano
        
    #getters and setters
    
    def getNumero(func):
        return func.__numero
    def getNome(func):
        return func.__nome
    def getSalMes(func, i):
        return func.__salario_mes[i]
    def getSalAno(func):
        return func.__salario_ano
    def setSalario(func, newSalario):
        func.__salario_mes.append(newSalario)
    def setSalariAno(func, newSalario):
        func.__salario_ano = newSalario
    def setCod(func, newCod):
        func.__numero = newCod
    def setNome(func, newNome):
        func.__nome = newNome
        
sal_ano = 0
    
     
func1 = tipo_funcionario(1, 'andredev dias', 1200000000, 1200000000000)
func2 = tipo_funcionario(2, 'queila', 1200000000, 1200000000000)
func3 = tipo_funcionario(3, 'trevis', 1200000000, 1200000000000)
func4 = tipo_funcionario(0, '0', 0, 0)


cod = input("digite o código do funcionario\n--")
cod = int(cod)
func4.setCod(cod)
nome  = input("informe o nome do funcionario\n--")
func4.setNome(nome)
for i in range(12):
    salMes  = input(f"informe o salario por mes {i} do funcionario\n--")
    salMes = float(salMes)
    func4.setSalario(salMes)
    sal_ano += func4.getSalMes(i)

func4.setSalario(sal_ano)

print("*************************************************************\n");
print("*************************************************************\n");

print(f"O codigo do funcion�rio e {func4.getNome()} \n");
print(f"O nome do funcion�rio e {func4.getNome()} \n");

for i in range(12):
    print(f"Recebe no mes {i} {func4.getSalMes(i)}: \n");
    func4.setSalariAno(float(func4.getSalAno()) + func4.getSalMes(i))

print(f"O salario anual é {func4.getSalAno()}")

# class Livro(): 
#     def __init__(self, titulo, autor, qtd_paginas, guardado=True): 
#         self.__titulo = titulo 
#         self.__autor = autor 

#         self.__qtd_paginas = qtd_paginas 
#         self.__guardado = guardado

#     # getters and setters

#     def setTitle(book, newTitle):
#         l1.__titulo = newTitle
#         print(f"Novo titulo atualizado : {l1.__titulo}")

#     def setAuthor(book, newAuthor):
#         l1.__autor = newAuthor
#         print(f"Novo autor atualizado : {l1.__autor}")

#     def setPag(book, newPag):
#         l1.__qtd_paginas = int(newPag)
#         print(f"Quatidade de páginas atualizada: {l1.__qtd_paginas}")

#     def setStatus(book, newStatus):
#         l1.__guardado = newStatus
#         print(f"Status atualizado: {l1.__guardado}")

#     def getTitle(book):
#         return book.__titulo
    
#     def getAuthor(book):
#         return book.__autor
    
#     def getPag(book):
#         return book.__qtd_paginas
    
#     def getStatus(book):
#         return book.__guardado
    
#     # métodos

#     def getBook(book):
#         if book.getStatus() == True:
#             book.setStatus(False) 
#             print(f"Ação realizada com sucesso! Status do livro {book.__guardado}")
#         else:
#             print("Não é possível realizar ação. Esse livro já foi emprestado")

#     def giveBackBook(book):
#         if book.getStatus() == False:
#             book.setStatus(True) 
#             print(f"Ação realizada com sucesso! Status do livro {book.__guardado}")
#         else:
#             print("Não é possível realizar ação. Esse livro já está guardado")
            
#     def turnPag(book):
#         global count
#         if count < book.__qtd_paginas:
#             count += 1 
#             print(f"\nvocê está na página : {count} de {book.__qtd_paginas}")
#         else:
#             print("\nVocê chegou ao final do livro")

#     def turnNPag(book, n):
#         global count
#         if count < book.getPag():
#             temp = count
#             count += int(n)
#             if count > book.getPag():
#                 print(f"Essa quantidade de páginas ultrapassa as páginas totais do livro.\nQuantidade de páginas totais {book.__qtd_paginas}")
#                 count = temp
#             else:
#                 print(f"você está na página : {count} de {book.__qtd_paginas}")
#         elif count >= book.__qtd_paginas:
#             print(f"Essa quantidade de páginas ultrapassa as páginas totais do livro.\nQuantidade de páginas totais {book.__qtd_paginas}")

#     def goBackPag(book):
#         global count
#         if count < 1:
#             print(f"você chegou a primeira página, não é possível virar mais.\nQuantidade de páginas totais {book.__qtd_paginas}")
#         else:
#             count -= 1
#             print(f"você está na página {count} de {book.__qtd_paginas}")

#     def goBackNPag(book, n):
#         global count
#         if count < 1:
#             print(f"você chegou a primeira página, não é possível virar mais.\nVocê está na página {count} de {book.__qtd_paginas}")
#         else:
#             temp = count
#             count -= n
#             if count < 0:
#                 count = temp
#                 print(f"essa quantidade de páginas excede a quantidade máxima!\nVocê está na página {count} de {book.__qtd_paginas}")
#             else:
#                 print(f"você está na página : {count} de {book.__qtd_paginas}")

#     def readBook(book):
#         print("Você está lendo {} de {}".format(l1.getTitle(), l1.getAuthor()))

        
# l1 = Livro('aaa', 'bbbb', 4, True)
# l2 = Livro('ccc', 'dddd', 600)

# option = 0

# login = int(input("ENTER DE USER:\n1 - USER\n2 - ADMIN\n---"))

# if login == 1 or login == 2:

#     try:

#         if login == 1:

#             while True:

#                 option = input("\n1 - Pegar livro\n2 - Devolver livro\n3 - Virar pag\n4 - Virar n páginas\n5 - Voltar página\n6 - Voltar n páginas\n7 - Ler livro\n0 - Sair\n---")

#                 if option == '1':
#                     l1.getBook()

#                 elif option == '2':
#                     l1.giveBackBook()

#                 elif option == '3':
#                     if l1.getStatus() == False:
#                         l1.turnPag()
#                     else:
#                         print("Não é possível realizar ação. Esse livro está guardado")

#                 elif option == '4':

#                     if l1.getStatus() == False:
#                         n = input("Quantas páginas você deseja virar?\n---")
#                         l1.turnNPag(n)
#                     else:
#                         print("Não é possível realizar ação. Esse livro está guardado")
                    
#                 elif option == '5':

#                     if l1.getStatus()== False:
#                         l1.goBackPag()
#                     else:
#                         print("Não é possível realizar ação. Esse livro está guardado")

#                 elif option == '6':

#                     if l1.getStatus() == False:
#                         n = input("Quantas páginas você deseja voltar?\n---")
#                         l1.goBackNPag(int(n))
#                     else:
#                         print("Não é possível realizar ação. Esse livro está guardado")

#                 elif option == '7':
#                     print("Você está lendo {} de {}".format(l1.getTitle(), l1.getAuthor()))
#                     # l1.readBook()

#                 elif option == '0':
#                     break
#         else:
#                 while True:

#                     option = input("\n1 - Pegar livro\n2 - Devolver livro\n3 - Virar pag\n4 - Virar n páginas\n5 - Voltar página\n6 - Voltar n páginas\n7 - Ler livro\n8  - Mudar titulo\n9 - Mudar autor\n10 - mudar quantidade de páginas\n11 - Mudar status\n0 - Sair\n---")

#                     if option == '1':
#                         l1.getBook()

#                     elif option == '2':
#                         l1.giveBackBook()

#                     elif option == '3':

#                         if l1.getStatus() == False:
#                             l1.turnPag()
#                         else:
#                             print("Não é possível realizar ação. Esse livro está guardado")

#                     elif option == '4':

#                         if l1.getStatus() == False:
#                             n = input("Quantas páginas você deseja virar?\n---")
#                             l1.turnNPag(n)
#                         else:
#                             print("Não é possível realizar ação. Esse livro está guardado")
                        
#                     elif option == '5':

#                         if l1.getStatus()== False:
#                             l1.goBackPag()
#                         else:
#                             print("Não é possível realizar ação. Esse livro está guardado")

#                     elif option == '6':

#                         if l1.getStatus() == False:
#                             n = input("Quantas páginas você deseja voltar?\n---")
#                             l1.goBackNPag(int(n))
#                         else:
#                             print("Não é possível realizar ação. Esse livro está guardado")

#                     elif option == '7':
#                         if l1.getStatus() == False:
#                             print("Você está lendo {} de {}".format(l1.getTitle(), l1.getAuthor()))
#                         else:
#                             print("você ainda não está lendo nenhum livro")
#                         # l1.readBook()
#                     elif option == '8':
#                         new = input("Enter the new title:\n---")
#                         l1.setTitle(new)
#                     elif option == '9':
#                         new = input("Enter the new author:\n---")
#                         l1.setAuthor(new)
#                     elif option == '10':
#                         new = input("Enter the new quantity of pages:\n---")
#                         l1.setPag(new)
#                     elif option == '11':
#                         new = input("Enter the new status:\n---")
#                         l1.setStatus(bool(new))
#                     elif option == '0':
#                         break
#     except ValueError as e:
#         print(f"erro {e}")