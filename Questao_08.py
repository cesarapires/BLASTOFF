A = int(input("Digite um número: "))
verificaPrimo = 0
for x in range(A):
    if(A%(x+1)==0):
        verificaPrimo+=1
if(verificaPrimo <= 2):
    print("Esse número é primo")
else:
    print("Esse número não é primo")
    
