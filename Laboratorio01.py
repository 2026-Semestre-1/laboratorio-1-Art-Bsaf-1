"""
Nombre: calculadora
Entrada: 3 Parámetros ( operacion, op1, op2)
Salida: Resultado de la operación
Restricciones: Los parámetros deben ser de tipo entero, el parámetros operacion debe permitir valores 1,2,3 y 4, los operadores deben ser de tipo entero.
"""
def calculadora(operacion, op1, op2): # Esta funcion hace validaciones antes de llamar a la auxiliar que es la que hace las operaciones
    
    if not isinstance(operacion, int):
        return "ERROR:La operacion no es un número entero"

    if 1 < operacion > 4:
        return "ERROR: Los valores de operacion deben de ser 1, 2, 3 o 4"

    if not isinstance(op1, int):
        return "ERROR: op1 no es un número entero"
    
    if not isinstance(op2, int):
        return "ERROR: op2 no es un número entero"

    if operacion == 4 and op2 == 0:
        return "ERROR: No se puede dividir entre 0"

    return calculadora_aux(operacion, op1, op2) # Llama a la funcion auxiliar para que haga la operacion 
    
def calculadora_aux(operacion, op1, op2):

    if operacion == 1: # Si operacion = 1 entonces se suma op1 y op2
        return op1 + op2

    if operacion == 2: # Si operacion = 2 entonces se resta op1 y op2
        return op1 - op2

    if operacion == 3: # Si operacion = 3 entonces se multiplica op1 y op2
        return op1 * op2

    if operacion == 4: # Si operacion = 4 entonces se divide op1 y op2
        return op1 // op2

"""
Nombre:  contadorDigitos
Entrada: Un número y el digito que desea buscar.
Salida: El número de veces que aparece el digito que buscas.
Restricciones: El número y digito deben de ser enteros, Solo se puede buscar un digito a la vez, el digito debe de ser menor a 10 y mayor igual a 0.
"""
def contadorDigitos(num, digito):

    if not isinstance(num, int) or not isinstance(digito, int): # Se valida para que el número y el digito sea enteros
        return "El número o el digito no son enteros."
    
    if digito > 9: # Se valida para que el numero sea menor a 9 y que tenga solo un digito
        return "Error: El parámetro digito debe ser un valor menor a 10"

    return contadorDigitos_aux(num, digito)
    
def contadorDigitos_aux(num, digito):
    count = 0

    if num == 0:
        return contadorDigitos(num)

    while num != 0: # Se mete en el bucle y empieza a buscar el digito en el número de der a izq, si lo encuentra se aumenta el count en 1
        
        if num % 10 == digito:
            count += 1

        num = num // 10

    return count

"""
Nombre: sumatoria_V2
Entrada: inicio, fin, distancia, excepcion
Salida: La suma total de los números desde el parámetro inicio hasta el fina.
Restricciones: Todos parámetros deben ser de tipo entero, Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0,
                        Los valores de inicio y fin deben ser positivos.
"""
def sumatoria_V2(inicio, fin, distancia, excepcion): # Está función hace todas las validaciones y luego llama a la función auxiliar 

    if not isinstance(inicio, int):
        return "ERROR: El valor inicio no es un número entero."

    if not isinstance(fin, int):
        return "ERROR: El valor fin no es un número entero."

    if not isinstance(distancia, int):
        return "ERROR: El valor distancia no es un número entero."

    if not isinstance(excepcion, int):
        return "ERROR: El valor excepcion no es un número entero."

    if 0 <= excepcion > 10:
        return "ERROR=: El valor excepcion debe de ser mayor a 0 y menor a 10."

    if inicio < 0:
        return "ERROR: El valor inicio debe de ser positivo."

    if fin < 0:
        return "ERROR: El valor fin debe de ser positvo."

    if distancia < 0 and not fin < inicio:
        return "ERROR: El parámetro fin debe ser menor o igual a inicio"

    if distancia > 0 and not fin > inicio:
        return "ERROR: El parámetro inicio debe ser menor o igual a fin"

    if distancia < 0:
        distancia = distancia * -1

        if 0 <= distancia >= 10:
            return "ERROR: El valor distancia debe de ser mayor a 0 y menor a 10."

        return sumatoria_V2_aux(inicio, fin, distancia*-1, excepcion)
    

    if 0 <= distancia >= 10:
        return "ERROR: El valor distancia debe de ser mayor a 0 y menor a 10."

    return sumatoria_V2_aux(inicio, fin, distancia, excepcion)

def sumatoria_V2_aux(inicio, fin, distancia, excepcion):

    count = inicio
    res = 0

    if distancia > 0: #se valida para saber si distancia es positivo 
        
        while count <= fin:

            if excepcion == 0 or  count % excepcion != 0: # se hace una verificación para ver si el número en count no sea divisible por la excepción o que excepción sea 0
                res += count

            count += distancia
            
        return res

    else:
        
        while count >= fin:

            if excepcion == 0 or  count % excepcion != 0:
                res += count

            count += distancia
            
        return res
            
                
        

        






























    



