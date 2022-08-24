import os
from os import system
from pathlib import Path


def potencias():
    potencias_de_dos = (128, 64, 32, 16, 8, 4, 2, 1)
    return potencias_de_dos


def binario_decimal(numeroBinario):
    potencias_de_dos = potencias()
    binarios = []
    suma = 0

    for i in numeroBinario:
        binarios.append(int(i))

    for recorrer_binarios in range(0, len(binarios)):
        if binarios[recorrer_binarios] == 1:
            suma += potencias_de_dos[recorrer_binarios]

    append_transformation = open("history/binary_dec_history.txt", "a")
    append_transformation.write("\n" + str(numeroBinario) + " = " + str(suma))
    append_transformation.close()

    return suma


def decimal_binario(numeroDecimal):
    potencias_de_dos = potencias()
    binario = []
    decimal_guardado = numeroDecimal
    decimal_nuevo = numeroDecimal

    for recorrer in potencias_de_dos:
        if decimal_nuevo >= recorrer:
            decimal_nuevo = decimal_nuevo - recorrer
            binario.append(1)
        else:
            binario.append(0)
    append_transformation = open("history/decimal_bin_history.txt", "a")
    append_transformation.write("\n" + str(decimal_guardado) + " = " + "".join(map(str, binario)))
    append_transformation.close()

    return "".join(map(str, binario)), decimal_guardado


def historial_dec_bin():
    prefix = "-*" * 5
    subprefix = "*-" * 5
    read_history = open("history/decimal_bin_history.txt")
    print(">> Historial\n" + prefix + " Decimales a binarios " + subprefix)
    print(read_history.read())
    read_history.close()


def historial_bin_dec():
    prefix = "-*" * 5
    subprefix = "*-" * 5
    read_history = open("history/binary_dec_history.txt")
    print(">> Historial\n" + prefix + " Binarios a decimales " + subprefix)
    print(read_history.read())
    read_history.close()


def salir():
    print("Programa finalizado.")


def limpiar():
    system("cls")


def menu():
    print('''
        Elija una opcion.
        \t [1] Pasar de decimal a binario
        \t\t [2] Mostrar historial
        \t [3] Pasar de binario a decimal
        \t\t [4] Mostrar historial
        \t [5] Salir
        ''')


def inicio():
    menu_lista = ["1", "2", "3", "4", "5"]
    menu()
    numero = str(input("Ingrese la opcion: "))
    limpiar()

    while numero not in menu_lista:
        limpiar()
        print("ERROR! Ingresa un opcion correcta \n")
        menu()
        numero = str(input("ERROR! Ingrese la opcion: "))

    if numero == "1":
        limpiar()
        decimal = int(input("Ingrese un numero decimal que desea convertir: "))
        resultado, decimal_guardado = decimal_binario(decimal)
        limpiar()

        print(f"El numero {decimal} ha sido transformado correctamente.\n\t Numero decimal a binario: {resultado}")
    elif numero == "2":
        historial_dec_bin()

    elif numero == "3":
        limpiar()
        binario = str(input("Ingrese el numero binario que desea convertir: "))
        resultado = binario_decimal(binario)
        limpiar()
        print(f" El numero {binario} ha sido transformado correctamente\n\tNumero binario a decimal: {resultado}")
    elif numero == "4":
        historial_bin_dec()

    elif numero == "5":
        salir()


inicio()
