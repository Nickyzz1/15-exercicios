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
    salMes  = input(f"informe o salario por mes {i+1} do funcionario\n--")
    salMes = float(salMes)
    func4.setSalario(salMes)
    sal_ano += func4.getSalMes(i)

func4.setSalario(sal_ano)

print("*************************************************************\n");
print("*************************************************************\n");

print(f"O codigo do funcion�rio e {func4.getNumero()} \n");
print(f"O nome do funcion�rio e {func4.getNome()} \n");

for i in range(12):
    print(f"Recebe no mes {i +1} {func4.getSalMes(i)}: \n");
    func4.setSalariAno(float(func4.getSalAno()) + func4.getSalMes(i))

print(f"O salario anual é {func4.getSalAno()}")

#estruturacomvetorarraylapratica reposit 2