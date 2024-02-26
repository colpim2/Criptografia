# Hill Cypher
# C = (Text * Key) mod 26
# D = (Text * Key) inv mod 26 
# @author: Castillo Montes Pamela
# @date: 27.02.2024

import fileinput

def matriz_ceros(row, col):
    matriz = []
    for i in range(row):
        fila = []
        for j in range(col):
            fila.append(0)
        matriz.append(fila)
    return matriz

def datos_archivo():
  modo = []
  texto = []
  key = []

  for lineNum, line in enumerate(fileinput.input()):
    if lineNum == 0:
      modo = line.strip().upper()
    elif lineNum == 1:
      texto = line.strip().upper()
    elif lineNum == 2:
      key = line.strip().upper()

  print(modo,texto,key)
  if len(key) != 4:
    return "La longitud de la clave debe ser 4."

  if modo == 'C':
    encrypted_text = encrypt(texto, key)
    return encrypted_text

  elif modo == 'D':
    decrypted_text = decrypt(texto, key)
    return decrypted_text

  else:
    return "Modo no reconocido."

def formato_texto(texto):
  #Si el tamaño del mensaje es inpar agrega un X al final
  if len(texto) % 2 != 0:
    texto += 'X'
  return texto

def texto_a_matriz(texto,textoMatriz):
  aux1 = 0
  aux2 = 0
  for i in range(len(texto)):
    if i % 2 == 0:
      #Se resta 65 para convertir de Ascii a rango 0-26
      textoMatriz[0][aux1] = int(ord(texto[i]) - 65)
      aux1 += 1
    else:
      textoMatriz[1][aux2] = int(ord(texto[i]) - 65)
      aux2 += 1
  return textoMatriz

def validar_obtener_inv(keyMatriz):
  #Calcular el determinante
  determ = keyMatriz[0][0] * keyMatriz[1][1] - keyMatriz[0][1] * keyMatriz[1][0]
  determ = determ % 26    #Se aplica mod 26

  #¿Tiene inverso?
  Inv = -1
  for i in range(26):
    tempInv = determ * i
    if tempInv % 26 == 1:
      Inv = i
      break
    else:
      continue

  if Inv == -1:
    raise ValueError("No existe inverso")

  return Inv

def encrypt(texto,key):
  texto = formato_texto(texto)

  #Calcular tamaño de matrices para el texto
  row = 2
  col = int(len(texto) / 2) 

  #Matrices en 0
  textoMatriz = matriz_ceros(row,col)
  keyMatriz = matriz_ceros(2,2)

  #Transformar en matrices
  textoMatriz = texto_a_matriz(texto,textoMatriz)
  keyMatriz = texto_a_matriz(key,keyMatriz)
  Inv = validar_obtener_inv(keyMatriz)

  encrypMsg = ""
  auxCount = int(len(texto)/2)

  for i in range(auxCount):
    temp1 = ( textoMatriz[0][i] * keyMatriz[0][0] ) + ( textoMatriz[1][i] * keyMatriz[0][1] )
    encrypMsg += chr((temp1 % 26) + 65)
    temp2 = ( textoMatriz[0][i] * keyMatriz[1][0] ) + ( textoMatriz[1][i] * keyMatriz[1][1] )
    encrypMsg += chr((temp2 % 26) + 65)

  return encrypMsg

def decrypt(texto,key):
  texto = formato_texto(texto)

  #Calcular tamaño de matrices para el texto
  row = 2
  col = int(len(texto) / 2) 

  #Matrices en 0
  textoMatriz = matriz_ceros(row,col)
  keyMatriz = matriz_ceros(2,2)

  #Transformar en matrices
  textoMatriz = texto_a_matriz(texto,textoMatriz)
  keyMatriz = texto_a_matriz(key,keyMatriz)
  Inv = validar_obtener_inv(keyMatriz)
  
  #Conjunta Transpuesta?
  keyMatriz[0][0], keyMatriz[1][1] = keyMatriz[1][1], keyMatriz[0][0]

  #Cambiar signos
  keyMatriz[0][1] *= -1
  keyMatriz[1][0] *= -1

  #Modulo
  keyMatriz[0][1] = keyMatriz[0][1] % 26
  keyMatriz[1][0] = keyMatriz[1][0] % 26

  #Multiplicar inversa por conjugada transpuesta
  for i in range(2):
      for j in range(2):
          keyMatriz[i][j] *= Inv

  #Modulo
  for i in range(2):
      for j in range(2):
          keyMatriz[i][j] = keyMatriz[i][j] % 26

  #Desencriptar
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