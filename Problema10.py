def convertir_fecha(fecha):
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }

    # Intentar el formato MM/DD/AAAA
    try:
        mes, dia, año = fecha.split('/')
        return f"{año}-{mes.zfill(2)}-{dia.zfill(2)}"
    except ValueError:
        pass

    # Intentar el formato "Mes DD, AAAA"
    for mes_nombre, mes_numero in meses.items():
        if fecha.startswith(mes_nombre):
            try:
                dia_año = fecha[len(mes_nombre):].strip().split(',')
                dia = dia_año[0].strip()
                año = dia_año[1].strip()
                return f"{año}-{mes_numero}-{dia.zfill(2)}"
            except IndexError:
                continue

    return "Formato de fecha no válido."
fecha_usuario = input("Ingresa una fecha (MM/DD/AAAA): ")
resultado = convertir_fecha(fecha_usuario)
print(f"Fecha en formato AAAA-MM-DD: {resultado}")
