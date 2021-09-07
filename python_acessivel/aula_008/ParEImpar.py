num = [[], []]

valor = 8
for cont in range(1, 8):
    valor = int(input("Digite um número:"))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].pop()

print(f"todos os valores pares são: {num[0]}")
print(f"todos os valores ímpares são: {num[1]}")

