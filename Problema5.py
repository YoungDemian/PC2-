def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
suma_primos = 0
for numero in range(2, 100):
    if es_primo(numero):  
        suma_primos += numero
print("La suma de todos los números primos menores que 100 es:", suma_primos)
