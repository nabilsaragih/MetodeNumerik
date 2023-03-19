def f(x):
    return (x ** 3 + x + 1) / (x ** 4 + 1)

def riemann(a, b, N):
    h = (b - a) / N

    xCurr = 0
    FxCount = 0

    for i in range(N):
        xCurr += h
        FxCount += f(xCurr)

    L = h * FxCount

    print(f"Luas: {format(L, '.3f')}")

a = float(input("Masukkan batas atas: "))
b = float(input("Masukkan batas bawah: "))
N = int(input("Masukkan jumlah pembagi area: "))

riemann(a, b, N)
