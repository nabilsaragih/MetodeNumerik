def f(x):
    return (x ** 3 + x + 1) / (x ** 4 + 1)

def trapezoid(a, b, N):
    h = (b - a) / N

    xCurr = h
    FxCount = 0

    for i in range(N-1):
        FxCount += f(xCurr)
        xCurr += h

    L = (h / 2) * ((2 * FxCount) + b)

    print(f"Luas: {format(L, '.3f')}")

a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
N = int(input("Masukkan jumlah pembagi area: "))

trapezoid(a, b, N)