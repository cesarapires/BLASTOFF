a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if(a>b):
    if(b>c):
        print("O menor número é [c]:",c)
    else:
        print("O menor número é [b]:",b)
elif(a>c):
    if(b>c):
        print("O menor número é [c]:",c)
    else:
        print("O menor número é [b]:",b)
else:
    print("O menor número é [a]:",a)
