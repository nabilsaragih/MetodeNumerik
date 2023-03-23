import equationRegex

def f(x):
    # x ** 2 + 7 * x + 5
    return eval(equationRegex.parse(persamaan))

def secant(x0, x1, e):
    iterCount = 1

    while True:
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
        fx2 = f(x2)

        print(f"{iterCount} {format(x0, '.5f')} {format(x1, '.5f')} {format(x2, '.5f')} {format(fx0, '.5f')} {format(fx1, '.5f')} {format(fx2, '.5f')}")

        if abs(fx1) <= e:
            break

        x0 = x1
        x1 = x2

        iterCount += 1

    print(f"Akar dari persamaan adalah {format(x1, '.5f')}")

persamaan = input("Masukkan persamaan, misal (x^2 + 3x - 1): ")

x0 = float(input("Masukkan nilai x0: "))
x1 = float(input("Masukkan nilai x1: "))
e = float(input("Masukkan nilai error: "))

secant(x0, x1, e)
