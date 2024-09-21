coisa = int(input("Digite um valor inteiro positivo: "))

impares = []

if X % 2 == 0:
    X += 1  

for i in range(6):
    impares.append(X)
    X += 2 

for numero in impares:
    print(numero)