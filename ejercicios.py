import requests

def fizzbuzz():


    print("Programa que muestra en consola numeros del 1 al 100")

    firstnum = int(input("Ingresa el primer numero: "))
    secondnum = int(input("Ingresa el segundo numero: "))

    for number in range(firstnum, secondnum + 1):

        if number % 3==0 and number % 5==0:
            print("fizzbuzz")

        elif number % 3 == 0:
            print("fizz")

        elif number % 5 ==0:
            print("buzz")

        else:
            print(f"{number}")




def missing_numbers():


    print("Array de enteros ordenado y sin repetir")

    numer_entry = input("Ingresa los valores de entrada Ejemplo: 1,3,6,9,12,15\n")

    try:
        array_int = [int(num.strip()) for num in numer_entry.split(",")]
    except ValueError:
        raise ValueError("Solo se aceptan numeros enteros separados por comas")

    if not isinstance(array_int, list):
        raise ValueError("No es una lista")

    if len(array_int) != len(set(array_int)):
        raise ValueError("Tiene numeros repetidos")

    if array_int != sorted(array_int):
        raise ValueError("La lista no esta ordenada")

    min_int = min(array_int)
    max_int = max(array_int)

    return_num = []

    for num in range(min_int + 1, max_int):
        if num not in array_int:
            return_num.append(num)

    return return_num



def poke_battle():

    print("Calculo de efectividad de ataques Pokemon")
    URL = "https://pokeapi.co/api/v2/type/"

    pokemon1 = input("Ingrese el tipo del atacante: ")
    pokemon2 = input("Ingrese el tipo del defensor: ")
    attack = int(input("Ingrese el ataque del atacante: "))
    defense = int(input("Ingrese la defensa del defensor: "))

    attacker_response = requests.get(URL + pokemon1) 
    defender_response = requests.get(URL + pokemon2)

    attack_data = attacker_response.json()
    defense_data = defender_response.json()

    attack_effective = 1

    for type_pokemon in defense_data["damage_relations"]["double_damage_from"]:
        if type_pokemon["name"] == attack_data["name"]:
            attack_effective = 2
            break

    for type_pokemon in defense_data["damage_relations"]["half_damage_from"]:
        if type_pokemon["name"] == attack_data["name"]:
            attack_effective = 0.5
            break

    for type_pokemon in defense_data["damage_relations"]["no_damage_from"]:
        if type_pokemon["name"] == attack_data["name"]:
            attack_effective = 0
            break


    if attack_effective == 2:
        print("El ataque ha sido Super Efectivo")

    elif attack_effective == 1:
        print("EL ataque ha sido normal")

    elif attack_effective == 0.5:
        print("El ataque parece que no ha sido poco efectivo")

    else:
        print("Ingrese los parametros correctos")

    calculo = 50 * (attack / defense) * attack_effective

    print(f"el daño ha sido {int(calculo)}")



