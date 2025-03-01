age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You can drive")
else:
    print("You can´t drive")

fruit = input("Which fruit do you want? ")

fruits = ["banana", "strawberry", "orange", "kiwy", "mango", "tomato"]

if fruit in fruits:
    print(f"Here´s your {fruit}")
else:
    print(f"We don´t have {fruit}")

#Estruturas de repetição

texto = input("insira o texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "")
    
    print()

for numero in range(0, 21, 2):
    print(numero)

while