A = list(input("Digite a lista A: ").split())
B = list(input("Digite a lista B: ").split())
C = []
for x in range(len(A)):
    if(A[x] == B[x]):
        C.append(A[x])
print(C)
    
