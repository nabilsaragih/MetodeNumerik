def f(x):
    return (x ** 3 + x + 1) / (x ** 4 + 1)

def Df(x):
    return ((-1 * x) ** 6 + (-3 * x) ** 4 + (-4 * x) ** 3 + (3 * x) ** 2 + 1) / (x ** 4 + 1) ** 2

def newtonRaphson(a, e):
    iterCount = 1

    while True:
        fa = f(a)
        Dfa = Df(a)
        b = a - (fa / Dfa)

        eCurrent = abs((b - a) / b)

        print(f"{iterCount} {format(a, '.5f')} {format(b, '.5f')} {format(eCurrent, '.5f')}")

        if eCurrent <= e:
            break

        a = b
        iterCount += 1
    
    print(f"Akar dari persamaan adalah {format(b, '.5f')}")

a = float(input("Masukkan a: "))
e = float(input("Masukkan e: "))

newtonRaphson(a, e)
