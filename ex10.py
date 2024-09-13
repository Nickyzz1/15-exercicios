horas_normais = 0
horas_extras = 0
horasnorm_resul = 0
resul = 0
poup = 0
hora = 10.00
horaextra = 15.00

horas_normais = input("Informe o numero de horas normais trabalhadas no ano:\n")
horas_normais = float(horas_normais)
horas_extras = input("Informe o numero de horas extras trabalhadas no ano:\n")
horas_extras = float(horas_extras)
horasnorm_resul = horas_normais * hora
horasext_resul = horas_extras * horaextra
resul = horasnorm_resul + horasext_resul

poup = resul * 0.08

print("______________________________________________________\n");
print(f"Valor de horas normais: {horasnorm_resul} reais\n\n",);
print(f"Valor de horas extras: {horasext_resul} reais\n\n",);
print(f"Total de ganho no ano = resul{resul} reais\n\n");
print(f"Valor a guardar na poupan�a = {poup} reais\n\n",);
print("______________________________________________________\n");

