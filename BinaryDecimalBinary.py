from os import system


def binario_decimal(numeroBinario):
    potencias_de_dos = (128, 64, 32, 16, 8, 4, 2, 1)
    binarios = []
    suma = 0
    for i in numeroBinario:
        binarios.append(int(i))

    for recorrer_binarios in range(0, len(binarios)):
        if binarios[recorrer_binarios] == 1:
            suma += potencias_de_dos[recorrer_binarios]

    return suma


def decimalB_binario(numeroDecimal):
    potencias_de_dos = (128, 64, 32, 16, 8, 4, 2, 1)
    binario = []
    decimal_nuevo = numeroDecimal
    for recorrer in potencias_de_dos:
        if decimal_nuevo >= recorrer:
            decimal_nuevo = decimal_nuevo - recorrer
            binario.append(1)
        else:
            binario.append(0)
    return "".join(map(str, binario))

def salir():
    print("Programa finalizado.")


def inicio():
    lista = ["1", "2", "3"]
    print('''
    Elija una opcion.
    \t [1] Pasar de decimal a binario
    \t [2] Pasar de binario a decimal
    \t [3] Salir
    ''')

    numero = str(input("Ingrese la opcion (1 o 2): "))
    system("cls")

    while numero not in lista:
        print("ERROR! Ingresa un opcion correcta \n")
        numero = str(input("Ingrese la opcion (1, 2 o 3): "))

    if numero == "1":
        decimal = int(input("Ingrese un numero decimal que desea convertir: "))
        resultado = decimalB_binario(decimal)
        system("cls")
        print(f"""
        El numero {decimal} ha sido transformado correctamente. 
        Numero decimal a binario: {resultado}
        """)

    elif numero == "2":
        binario = str(input("Ingrese el numero binario que desea convertir: "))
        resultado = binario_decimal(binario)
        system("cls")
        print(f"""
        El numero {binario} ha sido transformado correctamente
        Numero binario a decimal: {resultado}
        """)
    elif numero == "3":
        salir()


inicio()

