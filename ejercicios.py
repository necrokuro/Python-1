
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



def pokemonbattle(tipo_del_atacante,tipo_del_defensor,ataque,defensa):


    print("Calculo de efectividad de ataques Pokemon")
    effectiveness = {

        "agua": {
            "fuego": 2,
            "planta": 1,
            "electrico": 0.5,
            "agua": 1
        },

        "fuego": {
            "fuego": 0.5,
            "planta": 2,
            "electrico": 1,
            "agua": 0.5
        },

        "electrico": {
            "fuego": 1,
            "planta": 0.5,
            "electrico": 0.5,
            "agua": 2
        },

        "planta": {
            "fuego": 0.5,
            "planta": 0.5,
            "electrico": 1,
            "agua": 2
        },
    }
    attack_effective = effectiveness[tipo_del_atacante][tipo_del_defensor]


    if attack_effective == 2:
        print("El ataque ha sido Super Efectivo")

    elif attack_effective == 1:
        print("EL ataque ha sido normal")

    elif attack_effective == 0.5:
        print("El ataque parece que no ha sido poco efectivo")

    else:
        print("Ingrese los parametros correctos")

    calculo = 50 * (ataque / defensa) * attack_effective

    print(f"el daño ha sido {int(calculo)}")



