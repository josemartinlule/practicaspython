# Programa para verificar la longitud de una palabra

# Solicitar al usuario que ingrese una palabra y validamos que no ingrese numeros
while True:
    palabra = input("Ingresa una palabra: \n")
    if palabra.replace(" ", "").isalpha():
        break
    else:
        print("Caracter no valido, porfavor ingrese una palabra \n")

# Obtener la longitud de la palabra
longitud = len(palabra)

# Verificar la longitud y mostrar el mensaje correspondiente
if 4 <= longitud <= 8:
    print("La palabra es correcta.\n")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.\n")
else:  # longitud > 8
    print(f"Sobran letras. Tiene {longitud} letras.\n")
    
    
#---------------------------------------------------------------------------

# Programa para identificar el cuadrante de un punto

# Función para validar la entrada numérica 
def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Debes ingresar un número válido por favor.")

# Solicitar coordenadas al usuario
x = pedir_numero("Ingrese X: ")
y = pedir_numero("Ingrese Y: ")

# Verificar que ninguna coordenada sea 0
if x == 0 or y == 0:
    print("Ninguna coordenada puede ser 0.")
else:
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV")
        
    

