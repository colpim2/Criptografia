"""
RC4

Se implementa el algoritmo RC4 para la encriptación.

@author: Castillo Montes Pamela
@date: 14.03.2024
"""
# Importación Bibliotecas
import fileinput

# Lee la entrada desde un archivo y realiza encriptación.
def datos_archivo():
  key = ""
  plaintext = ""
  
  key = input().strip().encode()
  plaintext = input().strip().encode()
  encrypMsg = encrypt(key,plaintext)

  return encrypMsg

def rc4_init(key):
    global S, i, j
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + key[i % len(key)] + S[i]) % 256
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0

def rc4_output():
    global S, i, j
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    return S[(S[i] + S[j]) % 256]

def encrypt(key,plaintext):
    rc4_init(key)
    ciphertext = bytearray()
    for char in plaintext:
        ciphertext.append(char ^ rc4_output())
    return "".join("{:02X}".format(byte) for byte in ciphertext)

def main():
  resultado = datos_archivo()
  print(resultado)

if __name__ == "__main__":
    main()
