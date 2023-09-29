
const morseToText = () => {
    const morseInput = document.getElementById("morseInput").value;
    const words = morseInput.split("  ");
    let translatedText = "";

    for (const word of words) {
        const letters = word.split(" ");
        for (const letter of letters) {
            if (letter in morseToTextDict) {
                translatedText += morseToTextDict[letter];
            } else {
                translatedText += "?"; // Caracter de reemplazo para caracteres desconocidos
            }
        }
        translatedText += " "; // Agregar un espacio entre palabras
    }

    document.getElementById("translatedText").textContent = "Texto traducido: " + translatedText.trim();
};

const textToMorse = () => {
    const textInput = document.getElementById("textInput").value.toLowerCase();
    let morseCode = "";

    for (const char of textInput) {
        if (char === " ") {
            morseCode += " ";
        } else if (char in textToMorseDict) {
            morseCode += textToMorseDict[char] + " ";
        }
    }

    document.getElementById("morseCode").textContent = "Código Morse traducido: " + morseCode.trim();
};

const morseToTextDict = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
    "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
    "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
    ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
    "--..": "z", "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
    "----.": "9"
};

const textToMorseDict = {};
for (const morse in morseToTextDict) {
    textToMorseDict[morseToTextDict[morse]] = morse;
}