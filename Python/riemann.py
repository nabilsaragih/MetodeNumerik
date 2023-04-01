def f(x):
    return x * (4 * x + 1) ** 0.5

def riemann(a, b, N):
    h = (b - a) / N

    xCurr = 0
    FxCount = 0

    for i in range(N):
        xCurr += h
        FxCount += f(xCurr)

    L = h * FxCount

    print(f"Luas: {format(L, '.5f')}")

a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
N = int(input("Masukkan jumlah pembagi area: "))

riemann(a, b, N)
