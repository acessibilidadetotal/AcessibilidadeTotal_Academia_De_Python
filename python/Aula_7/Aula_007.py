
def faicha_Etaria(idade):
    if 0 <= idade < 18:
        return "Menor de idade"
    elif idade in range(18, 65):
        return 'maior idade'
    elif idade in range(65, 100):
        return 'melhor idade'
    elif idade > 100:
        return 'idade centenárea'
    else:
        return 'idade inválida'



#idade = int(input("Digite sua idade: "))
#print(f"Sua idade é: {idade} você está na faicha etárea da {faicha_Etaria(idade)}.")