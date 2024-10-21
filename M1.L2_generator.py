import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lengt = int(input("Introduce el tamaño de la contraseña (8 o más):"))

new_password = ""

for i in range(lengt):
    x = random.choice(characters)
    new_password = new_password + x

print(f"Tu nueva contraseña es: {new_password}")
