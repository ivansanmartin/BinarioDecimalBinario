import os
from os import system


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
    append_transformation.write(str(numeroBinario) + " = " + str(suma) + "\n")
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
    append_transformation.write(str(decimal_guardado) + " = " + "".join(map(str, binario)) + "\n")
    append_transformation.close()

    return "".join(map(str, binario)), decimal_guardado


def historial_dec_bin():
    prefix = "-*" * 5
    subprefix = "*-" * 5
    read_history = open("history/decimal_bin_history.txt")
    print(">> Historial\n" + prefix + " Decimales a binarios " + subprefix)
    print(read_history.read())

    if os.stat("history/decimal_bin_history.txt").st_size == 0:
        print("No existen registros.")

    read_history.close()

    back_menu = str(input("\nDesea volver al menu? SI | NO: "))

    if back_menu.casefold() == "si":
        limpiar()
        inicio()
    elif back_menu.casefold() == "no":
        limpiar()
        salir()


def historial_bin_dec():
    prefix = "-*" * 5
    subprefix = "*-" * 5
    read_history = open("history/binary_dec_history.txt")
    print(">> Historial\n" + prefix + " Binarios a decimales " + subprefix)
    print(read_history.read())
    if os.stat("history/binary_dec_history.txt").st_size == 0:
        print("No existen registros.")

    read_history.close()

    back_menu = str(input("\nDesea volver al menu? SI | NO: "))

    if back_menu.casefold() == "si":
        limpiar()
        inicio()
    elif back_menu.casefold() == "no":
        limpiar()
        salir()


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
        \n
        \t [C] Limpiar historial (borra todo los registros)
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
        flag = True
        limpiar()
        decimal = int(input("Ingrese un numero decimal que desea convertir: "))

        resultado, decimal_guardado = decimal_binario(decimal)
        limpiar()

        print(f"El numero {decimal} ha sido transformado correctamente.\n\t Numero decimal a binario: {resultado}")
        while flag:
            new_entry = str(input("Desea convertir otro numero decimal? SI | NO: "))
            if new_entry.casefold() == "si":
                limpiar()
                decimal = int(input("Ingrese un numero decimal que desea convertir: "))
                resultado, decimal_guardado = decimal_binario(decimal)
                print(f"El numero {decimal} ha sido transformado correctamente.\n\t Numero decimal a binario: {resultado}")
            elif new_entry.casefold() == "no":
                limpiar()
                inicio()
                break

    elif numero == "2":
        historial_dec_bin()

    elif numero == "3":
        flag = True
        limpiar()
        binario = str(input("Ingrese el numero binario que desea convertir: "))
        resultado = binario_decimal(binario)
        limpiar()
        print(f" El numero {binario} ha sido transformado correctamente\n\tNumero binario a decimal: {resultado}")
        while flag:
            new_entry = str(input("Desea convertir otro numero binario? SI | NO: "))
            if new_entry.casefold() == "si":
                limpiar()
                binario = str(input("Ingrese un numero binario que desea convertir: "))
                resultado = binario_decimal(binario)
                print(f"El numero {binario} ha sido transformado correctamente.\n\t Numero decimal a binario: {resultado}")
            elif new_entry.casefold() == "no":
                limpiar()
                inicio()
                break
    elif numero == "4":
        historial_bin_dec()

    elif numero == "5":
        salir()


inicio()
