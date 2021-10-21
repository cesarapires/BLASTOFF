palavra = input("Digite a palavra: ")
verifica = ''
tamanho = len(palavra)-1
for x in range(len(palavra)):
    verifica+=(palavra[tamanho]) 
    tamanho-=1
if(verifica == palavra):
    print("É palíndromo")
else:
    print("Não é palíndromo")
    
