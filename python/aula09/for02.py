

palavra = "melancia"
for letra in palavra:
    print(letra, end="")
print("\n fim")


aprovados = ["Luiza", "Paulo", "Ana", "Maria"]
for nome in aprovados:
    print(nome)
for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)
    print(f"({posicao + 1}):", nome)


dias_semana = ('Domingo', 'Segunda', 'Terça',
                'quarta', 'Quinta', 'Sexta',
                'Sábado')
for dia in dias_semana:
    print(f'Hoje é: {dia}')

