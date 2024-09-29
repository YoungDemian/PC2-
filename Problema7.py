def es_perfecto(numero):
  suma_divisores = 0
  for i in range(1, numero):
    if numero % i == 0:
      suma_divisores += i
  return suma_divisores == numero

for numero in range(1, 1000):
  if es_perfecto(numero):
    print(numero, "es un número perfecto")