print("Hola vamos a medir tu IMC\n")


#validamos el nombre

while True:
    nombre = input("Ingresa tu nombre.\n")
    if nombre.replace(" ", "").isalpha():
        break
    else:
        print("Por favor de ingresar un nombre valido sin numeros.\n")
        
#validacion del apellido paterno
while True:
    apellido_paterno = input("Por favor ingresa tu apellido paterno.\n")
    if apellido_paterno.replace(" ", "").isalpha():
        break
    else:
        print("Por favor de ingresar un apellido valido sin nuneros.\n")

#validacion apellido materno
while True:
    apellido_materno = input("Por favor ingresa tu apellido materno\n")
    if apellido_materno.replace(" ", "").isalpha():
        break
    else:
        print("Por favor de ingresar una apellido valido sin nuneros\n")
        
 #validamos edad
while True:
    try:
        edad = int(input("Por favor ingresa tu edad.\n"))
        if edad > 0:
            break
        else:
            print("La edad debe de ser mayor a cero.\n")
    except ValueError:
        print("Por favor ingrese un valor numerico.\n")
    
      
        
#mostramos nombre completo
nombre_completo = nombre + " " + apellido_paterno + " " + apellido_materno
print(f"Hola {nombre_completo}\n")
print("Me puedes ayudar con unos datos\n")

#validamos estatura
while True:
    try:
        estatura = float(input("Ingresa tu estatura porfavor.\n"))
        if estatura > 0:
            break
        else:
            print("La estaura debe de ser mayor a cero.\n")
    except ValueError:
        print("Por favor de ingresar un valor numerico.\n")
        
#validamos peso
while True:
    try:
        peso = float(input("Ingresa tu peso por favor\n"))
        if peso > 0:
            break
        else:
            print("El peso debe de ser mayor a cero.\n")
    except ValueError:
        print("Por favor de ingresar un valor numerico.\n")
        
#realizamos las operaciones
    
imc = peso / (estatura ** 2)

#evaluamos el IMC
if imc >= 0 and imc <= 18.49:
    mensaje = "Peso bajo"
elif imc >= 18.50 and imc <= 24.99:
    mensaje = "Peso normal"
elif imc >= 25 and imc <= 29.99:
    mensaje = "Sobrepeso"
elif imc >= 30 and imc <= 34.99:
    mensaje = "Obesidad leve"
elif imc >= 35 and imc <= 39.99:
    mensaje = "Obesidad media"
elif imc >= 40:
    mensaje = "Obesidad mórbida"

#mostramos el resultado al usuario
print(f"Edad: {edad}, {nombre_completo}, tu IMC es el siguiente:")
print(f"{imc:.2f} - {mensaje}")
        
        
        