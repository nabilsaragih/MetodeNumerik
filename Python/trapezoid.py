def f(x):
    return x * (4 * x + 1) ** 0.5

def trapezoid(a, b, N):
    h = (b - a) / N

    xCurr = 0
    FxCount = 0

    for i in range(N):
        FxCount += f(xCurr)
        xCurr += h

    L = (h / 2) * (f(a) + (2 * FxCount) + f(b))

    print(f"Luas: {format(L, '.5f')}")

a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
N = int(input("Masukkan jumlah pembagi area: "))

trapezoid(a, b, N)