"""
Hill Cypher

Se implementa el algoritmo Hill para la encriptación y desencriptación.
Encrypt: C = (Text * Key) mod 26
Decrypt: D = (Text * inv(Key)) mod 26

@author: Castillo Montes Pamela
@date: 27.02.2024
"""
# Importación Bibliotecas
import fileinput

# Llena una matriz de 0s
def matriz_ceros(row, col):
    matriz = []
    for i in range(row):
        fila = []
        for j in range(col):
            fila.append(0)
        matriz.append(fila)
    return matriz

# Lee la entrada desde un archivo y realiza encriptación o desencriptación según el modo
def datos_archivo():
  modo = ""
  texto = ""
  key = ""

  modo = input().strip()
  texto = input().strip()
  key = input().strip()
  """
  for lineNum, line in enumerate(fileinput.input()):
    if lineNum == 0:
      modo = line.strip().upper()
    elif lineNum == 1:
      texto = line.strip().upper()
    elif lineNum == 2:
      key = line.strip().upper()
  """
  # Excepción tamaño key
  #if len(key) != 4:
  #  raise ValueError("La longitud de la clave debe ser 4.")

  # Modo encriptar
  if modo == 'C':
    encrypted_text = encrypt(texto, key)
    return encrypted_text

  # Modo desencriptar
  #elif modo == 'D':
  else:
    decrypted_text = decrypt(texto, key)
    return decrypted_text

  # Excepción modo 
  #else:
  #  raise ValueError("Modo no reconocido.")

# Si el tamaño del mensaje es impar agrega un X al final
def formato_texto(texto):
  if len(texto) % 2 != 0:
    texto += 'X'
  return texto

# Convierte el texto en una matriz
def texto_a_matriz(texto,textoMatriz):
  aux1 = 0
  aux2 = 0
  for i in range(len(texto)):
    if i % 2 == 0:    # El caracter siguiente lo agrega a la primera fila
      textoMatriz[0][aux1] = int(ord(texto[i]) - 65)   #Se resta 65 para convertir de Ascii a rango 0-26
      aux1 += 1
    else:             # El caracter siguiente lo agrega a la segunda fila
      textoMatriz[1][aux2] = int(ord(texto[i]) - 65)   #Se resta 65 para convertir de Ascii a rango 0-26
      aux2 += 1
  return textoMatriz

def llave_a_matriz(key,keyMatriz):
  keyMatriz[0][0] = ord(key[0]) - 65
  keyMatriz[1][0] = ord(key[1]) - 65
  keyMatriz[0][1] = ord(key[2]) - 65
  keyMatriz[1][1] = ord(key[3]) - 65
  return keyMatriz

# Valida y obtiene la inversa de la key
def validar_obtener_inv(keyMatriz):
  #Calcular el determinante
  determ = (keyMatriz[0][0] * keyMatriz[1][1]) - (keyMatriz[0][1] * keyMatriz[1][0])
  #determ = determ % 26    

  #¿Tiene inverso?
  Inv = -1
  for i in range(26):
    tempInv = determ * i
    if tempInv % 26 == 1:
      Inv = i
      break
  
  #if Inv == -1:
  #  raise ValueError("No existe inverso")

  return Inv

#  Encripta el texto
def encrypt(texto,key):
  texto = formato_texto(texto)

  # Calcula el tamaño de las matrices para el texto
  row = 2
  col = int(len(texto) / 2) 

  # Inicizaliza las matrices en 0
  textoMatriz = matriz_ceros(row,col)
  keyMatriz = [[0, 0], [0, 0]]

  # Transforma el texto en matrices
  textoMatriz = texto_a_matriz(texto,textoMatriz)
  keyMatriz = llave_a_matriz(key,keyMatriz)
  Inv = validar_obtener_inv(keyMatriz)

  # Realiza la encriptación
  encrypMsg = ""
  auxCount = int(len(texto)/2)

  for i in range(auxCount):
    temp1 = ( textoMatriz[0][i] * keyMatriz[0][0] ) + ( textoMatriz[1][i] * keyMatriz[0][1] )
    encrypMsg += chr((temp1 % 26) + 65)
    temp2 = ( textoMatriz[0][i] * keyMatriz[1][0] ) + ( textoMatriz[1][i] * keyMatriz[1][1] )
    encrypMsg += chr((temp2 % 26) + 65)

  return encrypMsg

#  Desencripta el texto
def decrypt(texto,key):
  texto = formato_texto(texto)

  # Calcula el tamaño de las matrices para el texto
  row = 2
  col = int(len(texto) / 2) 

  # Inicizaliza las matrices en 0
  textoMatriz = matriz_ceros(row,col)
  keyMatriz = [[0, 0], [0, 0]]

  # Transforma el texto en matrices
  textoMatriz = texto_a_matriz(texto,textoMatriz)
  keyMatriz = llave_a_matriz(key,keyMatriz)
  Inv = validar_obtener_inv(keyMatriz)
  
  # Calculo de matriz adjunta
  keyMatriz[0][0], keyMatriz[1][1] = keyMatriz[1][1], keyMatriz[0][0]

  # Cambiar signos
  keyMatriz[0][1] *= -1
  keyMatriz[1][0] *= -1

  # Modulo
  keyMatriz[0][1] = keyMatriz[0][1] % 26
  keyMatriz[1][0] = keyMatriz[1][0] % 26

  # Multiplicar inversa por adjunta
  for i in range(2):
      for j in range(2):
          keyMatriz[i][j] *= Inv

  # Modulo
  for i in range(2):
      for j in range(2):
          keyMatriz[i][j] = keyMatriz[i][j] % 26

  # Realiza la desencriptación
  decryptMsg = ""
  auxCount = int(len(texto)/2)

  for i in range(auxCount):
    temp1 = ( textoMatriz[0][i] * keyMatriz[0][0] ) + ( textoMatriz[1][i] * keyMatriz[0][1] )
    decryptMsg += chr((temp1 % 26) + 65)
    temp2 = ( textoMatriz[0][i] * keyMatriz[1][0] ) + ( textoMatriz[1][i] * keyMatriz[1][1] )
    decryptMsg += chr((temp2 % 26) + 65)

  return decryptMsg

def main():
  resultado = datos_archivo()
  print(resultado)

if __name__=="__main__":
  main()