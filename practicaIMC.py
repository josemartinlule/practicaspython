


print("Hola vamos a medir tu IMC")
Nombres = str(input("¿Introduce tu nombre?\n"))
Apellido_1 = str(input("introduce tu primer apellido \n"))
Apellido_2 = str(input("Introduce tu segundo Apellido \n"))


Nombre_completo = print(f"hola" , Nombres , Apellido_1 , Apellido_2,"\n")

Nombre_completo = Nombres + " " + Apellido_1 + " " + Apellido_2

print("Me puedes ayudar dandome tu estatura y tu peso. \n")

Estatura = float(input("Ingresa tu estatura por favor. \n"))

Peso = float(input("Introduce tu peso por favor.\n"))

Imc = Estatura / (Peso ** 2)

print(f"Hola", Nombre_completo,  "tu Imc es \n", Imc)













