def loadBuffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof") 
    return buffer

def buffet(entrada, tamano_buffer):
    inicio = 0
    avance = 0
    buffer = loadBuffer(entrada, inicio, tamano_buffer)
    lexema = ""

    while True:
        while avance < len(buffer):
            char = buffer[avance]
            avance += 1

            if char.isspace() or char == "eof":
                if lexema:
                    print(f"Lexema procesado: {lexema}")
                    lexema = ""
                if char == "eof":
                    return 
            else:
                lexema += char

        inicio += tamano_buffer
        buffer = loadBuffer(entrada, inicio, tamano_buffer)
        avance = 0

def main():
    entrada = list("Esto es un ejemplo de entrada con eof")
    tamano_buffer = 10

    buffet(entrada, tamano_buffer)

if __name__ == "__main__":
    main()
