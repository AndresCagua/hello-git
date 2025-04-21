def decipher(ciphertext, known_word):
    def shift_char(c, shift):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            return c  # Dejar signos de puntuación y espacios tal cual

    for shift in range(1, 26):  # Probar todos los desplazamientos posibles
        decrypted = ''.join(shift_char(c, shift) for c in ciphertext)
        if known_word in decrypted:
            return decrypted

    return "invalid"


texto_cifrado = "Eqfkpi vguvu ctg hwp cpf ejcnngpikpi"
palabra_conocida = "coding"

print(decipher(texto_cifrado, palabra_conocida))
