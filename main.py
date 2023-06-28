import customtkinter as ctk

ctk.set_appearance_mode("dark")


def Encriptar():
    print("Sirvo")


def Desencriptar():
    print("Sirvo")


root = ctk.CTk()
# ancho x alto
root.geometry("800x700")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Cesar Cypher System")
label.pack(pady=12, padx=10)

textoParaCifrar = ctk.CTkEntry(master=frame, placeholder_text="Ingrese frase")
textoParaCifrar.pack(pady=12, padx=10)
numeroSaltos = ctk.CTkEntry(master=frame, placeholder_text="Ingrese # de saltos para Cesár")
numeroSaltos.pack(pady=12, padx=10)

numeroSaltosOctal = ctk.CTkEntry(master=frame, placeholder_text="Ingrese # de saltos para Octal")
numeroSaltosOctal.pack(pady=12, padx=10)

botonE = ctk.CTkButton(master=frame, text="Encriptar frase", command=Encriptar)
botonE.pack(pady=12, padx=10)

botonD = ctk.CTkButton(master=frame, text="Desencriptar frase", command=Desencriptar)
botonD.pack(pady=12, padx=10)

root.mainloop()
