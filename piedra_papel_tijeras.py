# programa para jugar piedra pepel o tijeras contra la maquina

import random

print("----------------------------------------------")
print("----------PIEDRA,PAPEL O TIJERA---------------")
print("----------------------------------------------")

#INPUT
print("1. piedra")
print("2. papel ")
print("3. tijeras")

usuario = int(input("escoga una opcion: "))

maquina = random.randint (1 , 3)

#PROCESSING

if usuario == maquina:
    print("EMPATE")
elif usuario == 1 and maquina == 2:
    print("perdio, maquina escoge tijeras")
elif usuario == 1 and maquina == 3:
    print("gano, piedra le gana a tijeras")
elif usuario == 2 and maquina == 1:
    print("gano, papel le gana a piedra")
elif usuario == 2 and maquina == 3:
    print("perdio, tijeras le ganan a papel")
elif usuario == 3 and maquina == 1:
    print("perdio, piedra le gana a tijeras")
elif usuario == 3 and maquina == 2:
    print("gano, tijeras le gana a papel")

else:
    print("--------------------------------------------")
    print("-------------ENTRADA INVALIDA---------------")
    print("--------------------------------------------")




