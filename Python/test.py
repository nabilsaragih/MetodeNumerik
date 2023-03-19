import re

persamaan = input("Masukkan persamaan, misal (2x^2 + 3x - 1): ")
# x1 = float(input("Masukkan x1: "))
# x3 = float(input("Masukkan x3: "))
# e = input("Masukkan error: ")
# x2 = (x1 + x3) / 2

fx1 = 0
fx3 = 0
fx2 = 0

persamaan = re.sub(r'([\^])', r'**', persamaan)
search = re.search('(\dx)', persamaan)

print(search)

# def bisection(x, exp):
#     return eval(exp)

# print(bisection(x1, persamaan))

# print(2*1**2 + 3*1 - 1)




