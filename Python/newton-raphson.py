import equationRegex
import sympy as sp

def f(x):
    # (x ** 3 + x + 1) / (x ** 4 + 1)
    return eval(equationRegex.parse(persamaan))

def Df(x):
    return eval(str(sp.diff(equationRegex.parse(persamaan))))

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

persamaan = input("Masukkan persamaan, misal (x^2 + 3x - 1): ")

a = float(input("Masukkan a: "))
e = float(input("Masukkan e: "))

newtonRaphson(a, e)
