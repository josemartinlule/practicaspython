import requests
import os
import json

# Crear carpeta pokedex si no existe
if not os.path.exists("pokedex"):
    os.makedirs("pokedex")

def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"❌ Error: El Pokémon '{nombre}' no existe.")
        return None

    data = response.json()

    # Extraer información relevante
    pokemon_info = {
        "nombre": data["name"],
        "peso": data["weight"],
        "tamaño": data["height"],
        "tipos": [tipo["type"]["name"] for tipo in data["types"]],
        "habilidades": [habilidad["ability"]["name"] for habilidad in data["abilities"]],
        "movimientos": [mov["move"]["name"] for mov in data["moves"]],
        "imagen": data["sprites"]["front_default"]
    }

    # Mostrar información
    print("\n✅ Pokémon encontrado:")
    print(f"Nombre: {pokemon_info['nombre'].capitalize()}")
    print(f"Peso: {pokemon_info['peso']}")
    print(f"Tamaño: {pokemon_info['tamaño']}")
    print(f"Tipos: {', '.join(pokemon_info['tipos'])}")
    print(f"Habilidades: {', '.join(pokemon_info['habilidades'])}")
    print(f"Total de movimientos: {len(pokemon_info['movimientos'])}")
    print(f"Imagen: {pokemon_info['imagen']}")

    # Guardar como archivo JSON
    archivo = f"pokedex/{nombre.lower()}.json"
    with open(archivo, "w") as f:
        json.dump(pokemon_info, f, indent=4)

    print(f"\n📁 Información guardada en '{archivo}'")
    return pokemon_info


# Programa principal
if __name__ == "__main__":
    nombre = input("🔍 Ingresa el nombre de un Pokémon: ")
    obtener_datos_pokemon(nombre)