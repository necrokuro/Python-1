
def fizzbuzz():
    print("Programa que muestra en consola numeros del 1 al 100")

    for numero in range(1, 101):

        if numero % 3==0 and numero % 5==0:
            print("fizzbuzz")
        elif numero % 3 == 0:
            print("fizz")
        elif numero % 5 ==0:
            print("buzz")
        else:
            print(f"{numero}")

def array_faltantes():
    print("Array de enteros ordenado y sin repetir")
    array_enteros = [1, 3, 6, 9, 12, 15, 20]

    if not isinstance(array_enteros, list):
        raise ValueError("No es una lista")
    if len(array_enteros) != len(set(array_enteros)):
        raise ValueError("Tiene numeros repetidos")
    if array_enteros != sorted(array_enteros):
        raise ValueError("La lista no esta ordenada")

    entero_menor = min(array_enteros)
    entero_mayor = max(array_enteros)

    return_num = []

    for num in range(entero_menor + 1, entero_mayor):
        if num not in array_enteros:
            return_num.append(num)

    return return_num

def batallapokemon(tipo_del_atacante,tipo_del_defensor,ataque,defensa):
    print("Calculo de efectividad de ataques Pokemon")
    efectividad = {

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
    efectividad_de_ataque = efectividad[tipo_del_atacante][tipo_del_defensor]

    if efectividad_de_ataque ==2:
        print("El ataque ha sido Super Efectivo")
    elif efectividad_de_ataque ==1:
        print("EL ataque ha sido normal")
    elif efectividad_de_ataque ==0.5:
        print("El ataque parece que no ha sido poco efectivo")
    else:
        print("Ingrese los parametros correctos")

    calculo = 50 * (ataque / defensa) * efectividad_de_ataque
    print(f"el daño ha sido {int(calculo)}")


