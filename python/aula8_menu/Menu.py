
from time import sleep

print("-"*40)
print("Seja bem vindo ao nosso menu interativo! ")
print("-"*40)
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

opcao = 0

while opcao != 5:
    print("""
    [1] somar,
    [2] multiplicar,
    [3] maior valor,
    [4]novo número,
    [5] sair do programa
    """)
    print("-"*30)
    opcao = int(input("Qual é sua opção? "))
    print("-"*30)
    if opcao == 1:
        soma = n1 + n2
        print(f"a soma entre {n1} + {n2} = {soma}")
    elif opcao == 2:
        multiplica = n1 * n2
        print(f"A multiplicação entre {n1} x {n2} = {multiplica}")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f"entre {n1} e {n2} o maior é {maior}")
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Saindo do programa, até logo!")
    else:
        print("Opção inválida, tente novamente.")
print("-"*30)
sleep(2)

