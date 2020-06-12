t = int(input())
for z in range(t):
    tom = int(input())
    n = 0
    tomOriginal = tom
    while tom % 2 == 0:
        tom = tom / 2;
        n += 1
    print(int(tomOriginal / (2**(n+1))))