import math


def input_data():
    a = float(input("Nhập a = "))
    b = float(input("Nhập b = "))
    c = float(input("Nhập c = "))
    return a, b, c


def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            x = -c / b
            print("Phương trình có một nghiệm x = {:.3f}".format(x))
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("Phương trình có hai nghiệm phân biệt:")
            print("x1 = {:.3f}".format(x1))
            print("x2 = {:.3f}".format(x2))
        elif delta == 0:
            x = -b / (2*a)
            print("Phương trình có nghiệm kép x = {:.3f}".format(x))
        else:
            print("Phương trình vô nghiệm")


def main():
    a, b, c = input_data()
    solve_quadratic(a, b, c)


if __name__ == "__main__":
    main()
