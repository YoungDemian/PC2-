start = 1500
end = 2700
result = []
for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 == 0:
        result.append(num)

print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:", result)
