# Function that gives the n first prime numbers
def primos(n):
    prim=[2]
    l=3
    while len(prim)<n:
        pri=1
        for j in prim:
            if l%j==0:
                pri=0
        if pri==1:
            prim.append(l)
        l+=1
    return prim
