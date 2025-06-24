import re
import sys

# Traducciones individuales
def traducir_mostrar(linea):
    contenido = re.findall(r'Mostrar\s+"(.*?)"', linea)
    if contenido:
        return f'print("{contenido[0]}")'
    elif 'Mostrar' in linea:
        partes = linea.split("Mostrar")[-1].strip()
        return f'print({partes})'
    return linea

def traducir_leer(linea):
    contenido = re.findall(r'Leer\s+(\w+)', linea)
    if contenido:
        return f'{contenido[0]} = input()'
    return linea

def traducir_sumar(linea):
    contenido = re.findall(r'Sumar\s+(\w+)\s+y\s+(\w+)', linea)
    if contenido:
        a, b = contenido[0]
        return f'resultado = {a} + {b}'
    return linea

def traducir_funcion(linea):
    match = re.match(r'Definir funci[oó]n (\w+)', linea)
    if match:
        return f'def {match.group(1)}():'
    return linea

def traducir_si(linea):
    match = re.match(r'Si (.+?) es igual a (.+)', linea)
    if match:
        return f'if {match.group(1).strip()} == {match.group(2).strip()}:'
    return linea

def traducir_sino(linea):
    if linea.strip() == "Sino":
        return "else:"
    return linea

def traducir_mientras(linea):
    match = re.match(r'Mientras (.+?) es menor que (.+)', linea)
    if match:
        return f'while {match.group(1).strip()} < {match.group(2).strip()}:'
    return linea

def traducir_repetir(linea):
    match = re.match(r'Repetir (\d+) veces', linea)
    if match:
        return f'for i in range({match.group(1)}):'
    return linea

def traducir_comentario(linea):
    match = re.match(r'Comentario:\s+(.*)', linea)
    if match:
        return f'# {match.group(1)}'
    return linea

def traducir_linea(linea):
    for traductor in [
        traducir_comentario,
        traducir_mostrar,
        traducir_leer,
        traducir_sumar,
        traducir_si,
        traducir_sino,
        traducir_mientras,
        traducir_repetir,
        traducir_funcion
    ]:
        traducida = traductor(linea)
        if traducida != linea:
            return traducida
    return linea

def procesar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    codigo_traducido = []
    indentacion = 0
    for linea in lineas:
        linea = linea.strip()
        if linea == "":
            codigo_traducido.append("")
            continue
        traducida = traducir_linea(linea)
        if traducida.endswith(":"):
            codigo_traducido.append("    " * indentacion + traducida)
            indentacion += 1
        elif linea == "Fin":
            indentacion = max(0, indentacion - 1)
        else:
            codigo_traducido.append("    " * indentacion + traducida)

    return "\n".join(codigo_traducido)

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 SSP.py archivo.ssp")
        return

    archivo_ssp = sys.argv[1]
    print("\n=== Traduciendo SSP a Python ===\n")
    codigo_python = procesar_archivo(archivo_ssp)
    print(codigo_python)

    print("\n=== Ejecutando código ===\n")
    try:
        exec(codigo_python)
    except Exception as e:
        print(f"❌ Error al ejecutar el código: {e}")

if __name__ == "__main__":
    main()
