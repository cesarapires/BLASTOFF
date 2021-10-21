A = []
A.append(list(input().split()))
A.append(list(input().split()))
A.append(list(input().split()))
A.append(list(input().split()))

for x in range(len(A)):
    for y in range(len(A[x])):
        print(A[x][y], end=" ")
    print()
    
