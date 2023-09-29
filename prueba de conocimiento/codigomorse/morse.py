import tkinter as tk

morse_to_text = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
    "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
    "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
    ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
    "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
    "----.": "9"
}

def morse_to_text_translator():
    morse_code = morse_entry.get()
    words = morse_code.split("  ")  # Separar palabras
    translated_text = ""
    for word in words:
        letters = word.split(" ")  # Separar letras
        for letter in letters:
            if letter in morse_to_text:
                translated_text += morse_to_text[letter]
            else:
                translated_text += "?"  # Caracter de reemplazo para caracteres desconocidos
        translated_text += " "  # Agregar un espacio entre palabras
    translated_text_label.config(text="Texto traducido: " + translated_text.strip())  # Actualizar la etiqueta con el resultado

def text_to_morse_translator():
    text = text_entry.get().lower()
    morse_code = ""
    for char in text:
        if char == " ":
            morse_code += " "
        elif char in morse_to_text.values():
            morse_code += [key for key, value in morse_to_text.items() if value == char][0] + " "
    morse_code_label.config(text="Código Morse traducido: " + morse_code.strip())  # Actualizar la etiqueta con el resultado

window = tk.Tk()
window.title("Aprendiz SENA")

title_label = tk.Label(window, text="Aprendiz Rubén  Dario Triviño  Diaz - Programa ADSO")
title_label.pack()

morse_label = tk.Label(window, text="Código Morse:")
morse_label.pack()

morse_entry = tk.Entry(window)
morse_entry.pack()

translate_morse_button = tk.Button(window, text="Traducir a Texto", command=morse_to_text_translator)
translate_morse_button.pack()

translated_text_label = tk.Label(window, text="")
translated_text_label.pack()

text_label = tk.Label(window, text="Texto:")
text_label.pack()

text_entry = tk.Entry(window)
text_entry.pack()

translate_text_button = tk.Button(window, text="Traducir a Código Morse", command=text_to_morse_translator)
translate_text_button.pack()

morse_code_label = tk.Label(window, text="")
morse_code_label.pack()

window.mainloop()
