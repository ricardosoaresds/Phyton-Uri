NOME = input()
SALARIO = float(input())
QUANTIDADEVENDAS = float(input())

BONUS = float(QUANTIDADEVENDAS*(15/100))
total = SALARIO + BONUS
print("TOTAL = R$ %0.2f" %total)

