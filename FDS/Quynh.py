#cho 1 số n, tìm các số nto nhỏ hơn n
n = int(input())

def prime(a):
    if a<2:
        return False
    for i in range(2, int(a**0.5)+1):
        if a%i ==0:
            return False
    return True

for i in range (n):
    if prime(i):
        print(i)