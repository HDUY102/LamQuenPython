# tìm lời giải trên không gian trạng thái
G = []
P = []
n = 0


def Split(String):
    k = string.index(' ')
    str = string[0:k]
    a = int(str, base=10)
    m = string.index(' ', k+1, -1)
    str = string[k+1:m]
    b = int(str, base=10)
    str = string[m+1:len(string)]
    c = int(str, base=10)
    return a, b, c


def Init(path, G):
    f = open(path)
    string = f.readline()
    string = string.replace('\t', ' ')
    n, a, z = Split(string)
    for i in range(n+1):
        G.append([])
        for j in range(n+1):
            G[i].append(0)
    while True:
        string = f.readline()
        if not string:
            break
        string = string.replace('\t', ' ')
        i, j, x = Split(string)
        G[i][j] = G[j][i] = x
        f.close()
        return n, a, z


def
