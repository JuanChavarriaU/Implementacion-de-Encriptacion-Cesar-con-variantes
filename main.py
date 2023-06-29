"""
Autores:
@Daav92
@johannpoty
@Jclark083
@gsantimate
@JuanChavarriaU

"""


import customtkinter as ctk

ctk.set_appearance_mode("dark")

abecedario = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

nuevoCifrado = []
texto_descifrado = ""


def Encriptar():
    texto = list(textoParaCifrar.get())
    texto_cifrado = ""
    print(texto)
    for letra in texto:
        # desplazas esa letra en un numero de posiciones n(saltosCesar); si es -1 es por que es espacio blanco u otra
        # cosa fuera del alfabeto
        posicion = abecedario.find(letra)
        print(posicion)
        if posicion == -1:
            if letra == ' ':
                texto_cifrado += ' '
        else:
            posicion_final = posicion + int(numeroSaltos.get())
            texto_cifrado += (abecedario[posicion_final])

    print(texto_cifrado)

    texto_cifrado = list(texto_cifrado)  # texto cifrado cesar
    print(texto_cifrado)
    cifradoDoble = []
    for caracter in texto_cifrado:
        valorDecimalUnicode = ord(caracter)
        valorOctal = oct(valorDecimalUnicode)
        cifradoDoble.append(valorOctal)
    print(cifradoDoble)

    cifradoDoble = [valor_octal.lstrip('0o') for valor_octal in
                    cifradoDoble]  # quitandole el prefijo octal a los numeros
    print(cifradoDoble)
    lista_octales_enteros = [int(valor) for valor in cifradoDoble]  # convirtiendo los strings a enteros
    print(lista_octales_enteros)

    for i in range(len(lista_octales_enteros)):
        print(i)
        num = lista_octales_enteros[i]
        num = num + int(numeroSaltosOctal.get())
        nuevoCifrado.append(num)
    print(nuevoCifrado)
    labelCifrado = ctk.CTkLabel(master=frame, text=str(nuevoCifrado), fg_color="transparent")
    labelCifrado.pack(pady=12, padx=10)


def Desencriptar():
    lista_entero_octal = []
    for i in range(len(nuevoCifrado)):
        num = nuevoCifrado[i] - int(numeroSaltosOctal.get())
        lista_entero_octal.append(num)
    print(lista_entero_octal)
    lista_octales = [str(valor) for valor in lista_entero_octal]
    descifradoDoble = ['0o' + valor_octal for valor_octal in lista_octales]
    print(descifradoDoble)

    descifradoOctal = []
    for octales in descifradoDoble:
        valorOctal = int(octales, 8)
        caracter = chr(valorOctal)
        descifradoOctal.append(caracter)
    print(descifradoOctal)

    texto_descifrado = ""
    for letra in descifradoOctal:
        # desplazas esa letra en un numero de posiciones n(saltosCesar); si es -1 es por que es espacio blanco u otra
        # cosa fuera del alfabeto
        posicion = abecedario.find(letra)
        print(posicion)
        if posicion == -1:
            if letra == ' ':
                texto_descifrado += ' '
        else:
            posicion_final = posicion - int(numeroSaltos.get())
            texto_descifrado += (abecedario[posicion_final])
    print(texto_descifrado)

    labelDescifrado = ctk.CTkLabel(master=frame, text=texto_descifrado, fg_color="transparent")
    labelDescifrado.pack(pady=12, padx=10)
    nuevoCifrado.clear()


root = ctk.CTk()
# ancho x alto
root.geometry("800x700")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Cesar Cypher System")
label.pack(pady=12, padx=10)

textoParaCifrar = ctk.CTkEntry(master=frame, placeholder_text="Ingrese frase", width=350)
textoParaCifrar.pack(pady=12, padx=10)
numeroSaltos = ctk.CTkEntry(master=frame, placeholder_text="Ingrese # de saltos para César", width=350)
numeroSaltos.pack(pady=12, padx=10)

numeroSaltosOctal = ctk.CTkEntry(master=frame, placeholder_text="Ingrese # de saltos para Octal", width=350)
numeroSaltosOctal.pack(pady=12, padx=10)

botonE = ctk.CTkButton(master=frame, text="Encriptar frase", command=Encriptar)
botonE.pack(pady=12, padx=10)

botonD = ctk.CTkButton(master=frame, text="Desencriptar frase", command=Desencriptar)
botonD.pack(pady=12, padx=10)

print(nuevoCifrado)
print(texto_descifrado)
root.mainloop()
