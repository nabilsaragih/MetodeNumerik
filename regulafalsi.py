def f(x):
    return (x ** 3 + x + 1) / (x ** 4 + 1)

def regulafalsi(a, b, error):
    iterCount = 1

    while True:
        fa = f(a)
        fb = f(b)

        c = b - ((fb * (b - a)) / (fb - fa))

        fc = f(c)

        tempFx = fa * fc

        print(f"{iterCount} {format(c, '.5f')} {format(fc, '.5f')} {format(tempFx, '.5f')}")

        if tempFx < 0:
            b = c
        elif tempFx > 0:
            a = c

        iterCount += 1
        if abs(fc) < error:
            break

    print(f"Akar dari persamaan adalah {format(c, '.5f')}")

a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
e = float(input("Masukkan error: "))

regulafalsi(a, b, e)
