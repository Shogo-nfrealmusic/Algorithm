def GCD(A, B):
    if B == 0:
        return A
    return GCD(B, A % B)

A, B = map(int, input.split())

L = A * B // GCD(A, B)

if L > 10**18:
    print("Large")
else:
    print(L)
    
