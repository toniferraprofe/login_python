"""
    Funciones de Orden Superior
    ---------------------------
    LAMBDA
    Funciones de Python pueden tomar funciones como parámetros y devolver funciones como resultado.
    Función de Orden Superior, es hacer ambas cosas.
    Pradigma: "Programación Funcional"
"""

""" FILTER """
# Es capaza de devolver una nueva colección de elementos filtrados que cumplan una condición.

# Practica, número pares
# función que compruebe número pares y "return" "True"
# def par(num):
#     if num % 2 == 0:
#         return True

numeritos = [23,45,8,99,12]

# filter, primer argumento es la función(condición), segundo es la lista
# filtro_pares = filter(par,numeritos)

# print(list(filtro_pares))

# LAMBDA
print(list(filter(lambda par: par % 2 == 0, numeritos)))