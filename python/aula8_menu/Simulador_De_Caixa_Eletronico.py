print("Bem vindo ao banco academia de Python!")

valor = int(input("Que valor você quer sacar? R$"))
total = valor
cedula = 100
totalcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedula +=1
    else:
        if totalcedula > 0:
            print(f"O total de {totalcedula} cédulas de {cedula} reais")
            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 2
            totalcedula = 0
            if total == 0:
                break
print("-"*40)
print("Obrigado por ter utilizado nossos serviços de \n saque eletrônico! \n Seja sempre bem vindo!")
