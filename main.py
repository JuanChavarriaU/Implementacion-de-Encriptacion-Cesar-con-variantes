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
    """
    Este código realiza un cifrado César básico en el que cada letra del texto original se desplaza un
    número determinado de posiciones hacia adelante en el alfabeto para obtener la letra cifrada.
    El número de posiciones a desplazar se especifica mediante la variable numeroSaltos
    """
    # Convierte la cadena de texto original en una lista de caracteres
    texto = list(textoParaCifrar.get())
    # Inicializa una cadena vacía para almacenar el texto cifrado
    texto_cifrado = ""
    # Imprime información sobre el proceso de encriptación
    print("Proceso de encriptación:")
    print("La cadena de texto a encriptar es", texto)
    # Itera sobre cada carácter en la lista de texto
    for letra in texto:
        # Busca la posición de la letra actual en el alfabeto
        posicion = abecedario.find(letra)
        # Verifica si la letra no está en el alfabeto
        if posicion == -1:
            # Verifica si es un espacio en blanco
            if letra == ' ':
                # Agrega un espacio en blanco a la cadena cifrada
                texto_cifrado += ' '
        else:
            # Calcula la posición final de la letra cifrada
            posicion_final = posicion + int(numeroSaltos.get())
            # Agrega la letra cifrada correspondiente a la cadena cifrada
            texto_cifrado += (abecedario[posicion_final])

    texto_cifrado = list(texto_cifrado)  # texto cifrado cesar
    # Imprime el texto cifrado resultante
    print("La cadena encriptada es:",texto_cifrado)
    """
    Este código realiza una etapa adicional de cifrado después del cifrado César básico. 
    Toma el texto cifrado resultante y lo convierte en una lista de números octales que representan 
    los valores decimales Unicode de cada carácter.
    Esta etapa adicional del cifrado convierte el texto cifrado en una secuencia de números octales, 
    lo que puede proporcionar una representación diferente y más difícil de detectar para el texto cifrado."""
    cifradoDoble = []
    # Itera sobre cada carácter en el texto cifrado
    for caracter in texto_cifrado:
        # Obtiene el valor decimal Unicode del carácter
        valorDecimalUnicode = ord(caracter)
        # Convierte el valor decimal en un número octal
        valorOctal = oct(valorDecimalUnicode)
        # Agrega el número octal a la lista de cifrado doble
        cifradoDoble.append(valorOctal)
    # Quita el prefijo '0o' de los números octales en la lista
    cifradoDoble = [valor_octal.lstrip('0o') for valor_octal in cifradoDoble]
    # Convierte los números octales en la lista en enteros
    lista_octales_enteros = [int(valor) for valor in cifradoDoble]
    print("La cadena en el sistema octal es:", lista_octales_enteros)
    """
    Esta sección del código realiza una operación adicional en los números octales enteros obtenidos en la etapa anterior del cifrado. 
    Toma cada número octal entero, lo suma con un valor numérico proporcionado por numeroSaltosOctal, 
    y almacena los nuevos números cifrados en la lista nuevoCifrado.
    Esta etapa adicional del cifrado agrega otro nivel de transformación numérica a los números octales enteros, 
    lo que puede aumentar la complejidad y dificultar la reversión del cifrado.
    """
    # Itera sobre los índices de la lista de números octales enteros
    for i in range(len(lista_octales_enteros)):
        # Obtiene el número octal entero en el índice actual
        num = lista_octales_enteros[i]
        # Suma el número octal con el valor numérico de numeroSaltosOctal
        num = num + int(numeroSaltosOctal.get())
        # Agrega el nuevo número cifrado a la lista nuevoCifrado
        nuevoCifrado.append(num)
    print("La cadena en el sistema octal desplazada es:", nuevoCifrado)

    labelCifrado = ctk.CTkLabel(master=frame, text=str(texto_cifrado), fg_color="transparent")
    labelCifrado.pack(pady=10, padx=10)

    labelCifrado = ctk.CTkLabel(master=frame, text=str(lista_octales_enteros), fg_color="transparent")
    labelCifrado.pack(pady=11, padx=11)

    labelCifrado = ctk.CTkLabel(master=frame, text=str(nuevoCifrado), fg_color="transparent")
    labelCifrado.pack(pady=13, padx=13)


def Desencriptar():
    print("Proceso de desencriptación:")
    """
    Esta última sección del código realiza la etapa de descifrado del proceso que se llevó a cabo anteriormente. 
    Toma los números cifrados, los transforma nuevamente en números enteros octales, y los convierte en cadenas con el prefijo '0o'.
    """
    lista_entero_octal = []
    print("La cadena en el sistema octal desplazado es:", nuevoCifrado)
    # Itera sobre los índices de la lista nuevoCifrado
    for i in range(len(nuevoCifrado)):
        # Obtiene el número cifrado en el índice actual y resta el valor numérico de numeroSaltosOctal
        num = nuevoCifrado[i] - int(numeroSaltosOctal.get())
        # Agrega el nuevo número entero octal a la lista lista_entero_octal
        lista_entero_octal.append(num)
    print("La cadena en el sistema octal es:", lista_entero_octal)
    # Convierte los números enteros octales en la lista en cadenas con prefijo '0o'
    lista_octales = [str(valor) for valor in lista_entero_octal]
    descifradoDoble = ['0o' + valor_octal for valor_octal in lista_octales]

    """
    Esta sección adicional del código realiza la etapa final del descifrado del texto original. 
    Toma los números octales cifrados en la etapa anterior, los convierte en valores decimales enteros y, 
    finalmente, los convierte en los caracteres correspondientes.
    """
    descifradoOctal = []
    # Itera sobre cada número octal cifrado en descifradoDoble
    for octales in descifradoDoble:
        # Convierte el número octal en un valor decimal entero
        valorOctal = int(octales, 8)
        # Convierte el valor decimal en el carácter ASCII correspondiente
        caracter = chr(valorOctal)
        # Agrega el carácter descifrado a la lista descifradoOctal
        descifradoOctal.append(caracter)
    print("La cadena desencriptada de Octal a Cesar es:",descifradoOctal)
    """
    Esta sección final del código realiza la etapa de descifrado César básico utilizando el resultado del descifrado del sistema octal.
    """
    texto_descifrado = ""
    # Itera sobre cada letra en descifradoOctal
    for letra in descifradoOctal:
        # Busca la posición de la letra en el alfabeto
        posicion = abecedario.find(letra)
        # Verifica si la letra no está en el alfabeto
        if posicion == -1:
            # Verifica si es un espacio en blanco
            if letra == ' ':
                # Agrega un espacio en blanco al texto descifrado
                texto_descifrado += ' '
        else:
            # Calcula la posición final de la letra descifrada
            posicion_final = posicion - int(numeroSaltos.get())
            # Agrega la letra descifrada correspondiente al texto descifrado
            texto_descifrado += (abecedario[posicion_final])
    print("La cadena de texto descifrada es:",texto_descifrado)

    labelDescifrado = ctk.CTkLabel(master=frame, text=texto_descifrado, fg_color="transparent")
    labelDescifrado.pack(pady=14, padx=14)
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

root.mainloop()
