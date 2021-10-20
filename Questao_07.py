#Entrada passando uma lista 
A = list(input().split())

#Loop para percorrer toda a lista
for x in A:
    #Compara se o elemento da lista tiver o resto da divisão
    #por zero ele é par
    if(int(x)%2 == 0):
        #Mostra na tela se ele for par
        print(x)
