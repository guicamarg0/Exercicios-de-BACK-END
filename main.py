lado1=int(input("Adicione o valor do primeiro lado: "))
lado2=int(input("Adicione o valor do segundo lado: "))
lado3=int(input("Adicione o valor do terceiro lado: "))
if lado1>0 and lado2>0 and lado3>0:
    if lado1+lado2>lado3:
        if lado1+lado3>lado2:
            if lado2+lado3>lado1:
                if lado1==lado2==lado3:
                    print("O triângulo é Equilátero.")
                elif lado1!=lado3!=lado2!=lado1: 
                    print("O triângulo é Escaleno.")
                elif lado1==lado2 or lado2==lado3 or lado3==lado1:
                    print("O triângulo é Isósceles.")
else: 
    print("O triângulo não existe.")
