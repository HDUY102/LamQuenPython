# Mảng 1 chiều
def ViewArr(M, n):
    for i in range(n):
        print("%d\t" % M[i], end=' ')
    print()


def SumArr(M, n):
    s = 0
    for i in range(n):
        s = s+int(M[i])
    return s


def SumLe(M, n):
    s = 0
    for i in range(n):
        if int(M[i]) % 2 != 0:
