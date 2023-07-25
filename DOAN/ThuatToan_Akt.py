def ThapHN(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {B}")
        return
    ThapHN(n - 1, A, C, B)
    print(f"Move disk {n} from {A} to {B}")
    ThapHN(n - 1, C, B, A)


def Check(M, n, u):
    for i in range(1, n + 1):
        if M[i] == u:
            return True
    return False


def Print(P, n, s, g):
    Path = []
    for i in range(0, n + 1):
        Path.append(0)
    print("\nĐường đi từ %d đến %d là\n" % (s, g), end=' ')
    Path[0] = g
    i = P[g]
    k = 1
    while i != s:
        Path[k] = i
        k = k + 1
        i = P[i]
    Path[k] = s
    for j in range(0, k + 1):
        i = k - j


def main():
    try:
        num_disks = int(input("Nhập đĩa: "))
        if num_disks <= 0:
            print("Number of disks should be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of disks.")
        return

    n = num_disks
    G = []
    P = [0]

    s = 1
    g = n
    ThapHN(n, 'A', 'C', 'B')


if __name__ == '__main__':
    main()
