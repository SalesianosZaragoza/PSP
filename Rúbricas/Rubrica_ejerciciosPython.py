"""Ejercicio 1: Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y) y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos, con el siguiente formato:
                      x + y = …
                      x – y = …
                      x * y = …
                      x / y = …
                      x % y = …
Ejercicio 2:  Escribe un programa Python que pregunte al usuario por 10 números enteros y muestre por pantalla el número total de veces que el usuario ha introducido el 0, el número total de enteros mayores que 0 introducidos y el número total de enteros menores que 0 introducidos.
Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número. El programa generará un número aleatorio entre 0 y 20 y luego irá pidiendo números al usuario indicando “mayor” o “menor” según sea mayor o menor con respecto al número generado aleatoriamente. El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones junto al número de intentos que ha necesitado el usuario.
Ejercicio 4:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y muestre por pantalla la longitud de esta.
Ejercicio 5:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y muestre por pantalla el número de veces que aparece la sub-cadena “aaa” dentro de dicho String.
Ejercicio 6:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y muestre por pantalla dicha cadena, pero con el primer y último carácter cambiados de posición.
Ejercicio 7:  Implementa un programa Python que solicite al usuario una cadena de caracteres y devuelva dicha cadena, pero al revés.
Ejercicio 8:  Implementa un programa Python con un método llamado sum(int [] tabla) que muestre por pantalla el resultado de sumar todos los elementos de la tabla pasada como parámetro.
Ejercicio 9:  Implementa un programa Python con un método llamado indexContains(String[] tabla, String cadena) que devuelva el índice de la tabla cuyo valor es igual al valor de “cadena”. En caso de no haber ningún valor igual, devuelve -1
Ejercicio 10:  Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro una tabla de Strings y muestra por pantalla el String con mayor longitud y el String con menor longitud.
Ejercicio 11: Tenemos la siguiente tabla multidimensional, la cual almacena por cada una de sus filas el salario trimestral de cada uno de los empleados de la empresa.
int salarios[][] = { {700, 900, 1300} , {1000, 950, 1080}, {1300, 930, 1200} }
A su vez, disponemos también de una tabla empleados, con los nombres de los trabajadores:
String empleados[] = {Javier María, Antonio Muñoz, Isabel Allende}
Implementa un programa Python que muestre por pantalla lo siguiente:
Javier Marías -> 700 + 900 + 1300 = 2900€
Antonio Muñoz -> 1000 + 950 + 1080 = 3030€
Isabel Allende -> 1300 + 930 + 1200 = 3430€
Ejercicio 12: Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crea sus métodos get, set y toString. Tendrá dos métodos especiales:
                 - ingresar(double cantidad): se ingresa una cantidad a la cuenta si la cantidad introducida es negativa, no se hará nada.
                 - retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0.
Ejercicio 13: Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix, que contenga los siguientes métodos: 
                - getNumberRows(): devuelve el número de filas de la matriz.
                - getNumberColumns(): devuelve el número de columnas de la matriz.
                - setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el valor de [element].
                - addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los elementos de [matrix], y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial, la operación no se puede realizar (notificalo).
                - multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual a los elementos de [matrix], y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial, la operación no se puede realizar (notificalo).
Ejercicio 14: Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
                - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
                - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
                - 3. Salir del Programa.
Ejercicio 15: Crea un fichero de texto con el nombre y contenido que tú desees. Por ejemplo, Ejercicio15.txt. Realiza un programa en Python que lea el fichero <<Ejercicio15.txt>> y muestre su contenido por pantalla sin espacios. Por ejemplo, si el fichero contiene el siguiente texto “Hola que haces”, deberá mostrar “Holaquehaces”.
"""


