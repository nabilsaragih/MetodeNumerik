def f(x):
    persamaan = '(x ** 3 + x + 1) / (x ** 4 + 1)'
    return eval(persamaan)

def bisection(a, b, error):
    iterCount = 1

    while True:
        c = (a + b) / 2

        fa = f(a)
        fb = f(b)
        fc = f(c)
        tempFx = fb * fc

        print(f"{iterCount} {format(c, '.5f')} {format(fc, '.5f')} {format(tempFx, '.5f')}")

        if tempFx < 0:
            a = c
        elif tempFx > 0:
            b = c

        iterCount += 1
        if abs(fc) < error:
            break
        
    print(f"Akar dari persamaan adalah {format(c, '.5f')}")

a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
e = float(input("Masukkan error: "))

bisection(a, b, e)

