alumnos = []
cantidad = int(input("¿Cuántos alumnos desea ingresar? "))
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1} para {nombre}: "))
        notas.append(nota) 
    alumno = {
        "Nombre": nombre,
        "Notas": notas
    }
    alumnos.append(alumno)
print("\nListado completo de alumnos y sus notas:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Nombre']}, Notas: {alumno['Notas']}")
