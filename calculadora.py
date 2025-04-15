def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

if __name__ == "__main__":
    print("Calculadora básica")
    while True:
        entrada = input("Ingresa operación (ej. 2 + 2) o 'c' para limpiar, 'q' para salir: ")

        if entrada.lower() == 'q':
            break
        elif entrada.lower() == 'c':
            continue

        try:
            resultado = eval(entrada)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)
