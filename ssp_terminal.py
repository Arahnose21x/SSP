import re

def traducir_linea(linea):
    if linea.startswith("Mostrar "):
        contenido = re.findall(r'Mostrar\s+"(.*?)"', linea)
        if contenido:
            return f'print("{contenido[0]}")'
        else:
            return f'print({linea.split("Mostrar", 1)[1].strip()})'

    elif linea.startswith("Leer "):
        variable = linea.split("Leer", 1)[1].strip()
        return f'{variable} = input()'

    elif " es igual a " in linea:
        partes = linea.split(" es igual a ")
        return f'if {partes[0].strip()} == {partes[1].strip()}:'

    elif "Sumar " in linea:
        partes = re.findall(r'Sumar (\w+)\s+y\s+(\w+)', linea)
        if partes:
            a, b = partes[0]
            return f'resultado = {a} + {b}'

    elif linea.strip() == "Sino":
        return "else:"

    elif "Mientras " in linea:
        partes = re.findall(r'Mientras (.+?) es menor que (.+)', linea)
        if partes:
            return f'while {partes[0][0].strip()} < {partes[0][1].strip()}:'

    elif "Repetir " in linea:
        partes = re.findall(r'Repetir (\d+) veces', linea)
        if partes:
            return f'for i in range({partes[0]}):'

    elif linea.startswith("Comentario:"):
        return f"# {linea[10:].strip()}"

    return linea

print("🟢 Bienvenido al intérprete de SSP")
print("Escribe código en SSP. Escribe 'salir' para terminar.\n")

contexto = {}

bloque = []
indentacion = 0

while True:
    try:
        prompt = ">>> " if indentacion == 0 else "... "
        linea = input(prompt)

        if linea.strip().lower() == "salir":
            break

        if linea.strip() == "Fin":
            indentacion = max(0, indentacion - 1)
            continue

        traducida = traducir_linea(linea)
        bloque.append("    " * indentacion + traducida)

        if traducida.endswith(":"):
            indentacion += 1
            continue

        if indentacion == 0:
            codigo = "\n".join(bloque)
            try:
                exec(codigo, contexto)
            except Exception as e:
                print(f"❌ Error: {e}")
            bloque = []

    except KeyboardInterrupt:
        print("\n👋 Cerrando SSP...")
        break
