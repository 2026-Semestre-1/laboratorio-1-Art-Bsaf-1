[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/0KXffURN)
# LABORATORIO 01 

## Descripción General
- El siguiente laboratorio consiste en una serie de ejercicios para el desarrollo de programación en **sintaxis de Python**, además de evaluación de conceptos vistos en clases anteriores.
- El objetivo de este laboratorio está en el uso de la **condicional IF**, **creación de funciones**, **validación de los parámetros** y recuerde que en cada función que desarrollen agregar los **comentarios** (nombre, parámetros entrada, salida y restricciones).
- Finalizado el laboratorio subir el archivo con el nombre de **Laboratorio01.py**, la entrega cierra a las **3pm del 11 de marzo del 2026** y será a través del Github Classroom.
- Deben ser muy claros con los mensajes de error que programen en su código.
- Como observación, no solo se califica el correcto funcionamiento del código sino también las validaciones, comentarios y el uso correcto de las funciones o bloques de código permitidos


## calculadora(operacion, op1, op2)
Escriba una calculadora, que reciba 3 parámetros, el primero consiste en la operación y después los dos operadores, y que calcule el resultado y posteriormente lo imprima en pantalla. Las operaciones soportadas son **suma=1, resta=2, multiplicación=3 y división entera=4** (no es posible la división entre 0). Los parámetros deben ser de tipo entero, el parámetros **operacion** debe permitir valores 1,2,3 y 4, loa operadores deben ser de tipo entero.
``` python
>>> calculadora (1, 4, 8)
12
>>> calculadora (2, 4, 8)
-4
>>> calculadora (3, 4, 8)
32
>>> calculadora (4, 10, 8)
1
```

## contadorDigitos(num, digito)
Implemente una función llamada **contadorDigitos(num, digito)** donde se espera que la salida retorne el número de veces que el dígito aparece en el número. Ambos parámetros deben ser de tipo entero, el párametro llamado **digito** debe ser menor a 10 y mayor igual a 0. Ejemplo:
``` python
>>> contadorDigitos(102039480, 0)
3
>>> contadorDigitos(132033483, 3)
4
```

## sumatoria_V2(inicio, fin, distancia, excepcion)
Implemente una función llamada **sumatoria_V2(inicio, fin, distancia, excepcio)** donde se espera que la salida la suma totoal de los números desde el parámetro inicio hasta el final.  
Existen varias restricciones: 
- Todos parámetros deben ser de tipo entero,
- Los párametros **distancia y excepcion** debe ser menor a 10 y mayor a 0.
- Los valores de **inicio** y **fin** deben ser positivos
- Si la **distancia** es un número negativo, el valor de **fin** debe ser menor a **inicio**
- Si la **distancia** es un número positivo, el valor de **fin** debe ser mayor a **inicio**
- Si **excepcion** es igual a cero, se debe ignorar este valor, lo contrario, todo número dentro de la secuencia entre **inicio** y ** final** sea divisible por esta **excepcion** debe omitirse en la suma

``` python
>>> sumatoria_V2(1, 5, 1, 0)  #1 + 2 + 3 + 4 + 5
15
>>> sumatoria_V2(1, 5, 1, 2)  #1 + 3 + 5
9
>>> sumatoria_V2(1, 5, 3, 2)  #1
1
>>> sumatoria_V2(10, 8, -1, 0)  #10 + 9 + 8
27
>>> sumatoria_V2(10, 5, 3, 2)  #1
"Error: el parámetro inicio debe ser menor o igual a fin"

```
