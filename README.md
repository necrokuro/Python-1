Requisitos para el programa:

Tener la version de Python 3.9 o superior:

Ejercicio 1:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

logica del programa:

Se utilizo un bucle for para recorrer los numeros del 1 al 100
Despues se ultizo las sentencias de if, elif y else para que comprobara los multiplos
de 3 los multiplos del 5 y los multiplos de ambos juntos usando el operador de "%" para obtener el resultado buscado
despues de combinar el bucle for y los ifs dentro del for con su respectivo operador se mando a emprimir la variable
del for (numero) para que arroje el resultado ya evaluado por los ifs.

Ejercicio 2:

Dado un array de enteros ordenado y sin repetidos,
crear una función que calcule y retorne todos los que faltan entre
el mayor y el menor.
Lanza un error si el array de entrada no es correcto.

logica del programa:

Se utilizo un array el cual se le agregaron enteros no continuos 
despues se utilizo las estructuras de if para hacer una verificacion en este caso por medio de la funcion isinstance 
se verifica si la variable es o no es un tipo de dato list de lo contrario se lanza una excepcion por ValueError utilizando
la sentencia raise. Despues se verifica por len la longitud de la lista original y compara con la longitud de la misma lista
pero utilizando esta vez una funcion set la cual elimina los elementos repetidos de la lista por ende si la longitud cambia 
indicaria que habia elementos repetidos arrojando de esta manera un error con mensaje "Tienes nuemros repetidos".
pasando al otro if el cual utiliza un sorted para verificar si la lista esta organizada.
Despues declare dos variables con la funcion min() y max() las cuales ayudan al for a recorrer la lista y asi obtener los
extremos de la lista del min al max.
Se utilizo un for para obtener el rango de la lista utilizando las variables declaradas anteriormente y entonces por medio de
un if verificar si no se encuentran los numeros dentro de la lista original entonces retornar los en una lista vacia creada anteriormente
por medio de la funcion append() y al final que retorne la lista vacia con esos numeros faltantes.

Ejercicio 3:

Crea un programa que calcule el daño de un ataque durante
una batalla Pokémon.
La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
(buscar su efectividad)
El programa recibe los siguientes parámetros:
Tipo del Pokémon atacante.
Tipo del Pokémon defensor.
Ataque: Entre 1 y 100.
Defensa: Entre 1 y 100.

logica del programa:

Principalmente en la funcion batallapokemon se declararon los paramentros a utilizar
se creo un diccionario anidado para guardar la informacion de las debilidades de los tipos de Pokemon
despues se usa la notacion de los diccionarios anidados para obtener la informacion de las debilidades
segun el tipo de Pokemon por ejemplo agua vs fuego se obtendria el valor 2 indicando que el ataque se
multiplicara por ese valor y dara super efectivo.
Entonces se desarrollo una sentencia de if, elif y else para poder determinar si el ataque ha sido
super efectivo o poco efectivo entonces si la variable de efectividad de ataque ha sido igual a 2 el
ataque a sido super efectivo si ah sido igual a 1 ha sdo normal si ha sido por 0.5 ha sido poco efectivo
de lo contrario ingresar los datos correctos.
por ultimo se declaro una variable calculo la cual tiene el cualculo de 50 * (ataque / defensa) * efectividad
y se manda a imprimir el calculo del daño en enteros con la efectividad del ataque.






