def inputData():
    n = int(input("nhap n= "))
    return n


def Giaithua(n):
    s = 1
    for i in range(1, n+1):
        s = s*i
    return s


def main():
    n = int(input("n= "))
    s = Giaithua(n)
    print("%d" % n, "!= %d" % s)


if __name__ == "__main__":
    main()
