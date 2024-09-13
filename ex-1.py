cont = 0
idade = 0
totalsexof21 = 0
totalsexof = 0
totalsexom = 0
totalsexom18 = 0
totalidadef = 0
totalidadem = 0
media = 0
mediaf = 0
sexo = ''


for i in range(3) :
    
    age = input("qual a sua idade?\n--")
    sex = input("qual o seu sexo?\n--")
    
    age = int(age)
    
    if age >= 21 and sex.lower() == 'f':
        totalsexof21 += 1
        totalidadef += age
    else:
        if sex.lower() == 'f':
            totalsexof += 1
            totalidadef += age
    if age >= 18 and sex.lower() == 'm':
        totalsexom18 += 1
        totalidadem += age
    else:
        if sex.lower() == 'm':
            totalsexom += 1
            totalidadem += age
            
if int(totalsexof + totalsexof21) == 0:   
    print("a divisão por zero não foi executada no sexo fem")
else:  
    mediaf = totalidadef/(totalsexof + totalsexof21)
if int(totalsexom + totalsexom18) == 0:
    print("a divisão por zero não foi executada no sexo masc")
else:
    mediam = totalidadem/ (totalsexom + totalsexom18)
   

print("\nTotal do sexo feminio e maior que 21 � de:",totalsexof21);
print("\nTotal do sexo masculino e maior que 18 � de:",totalsexom18);
print("\nMedia de idade do sexo feminio � de: ", mediaf);
print("\nMedia de idade do sexo masculino � de:", media);

# aulapraticacomandofor05.c repositoriaoo v1
        
            
    

