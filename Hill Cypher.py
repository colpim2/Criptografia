# Hill Cypher
# C = (Text * Key) mod 26
# D = (Text * Key) inv mod 26 
# @author: Castillo Montes Pamela
# @date: 27.02.2024

import fileinput
import numpy as np

def datos_archivo():
  for line in fileinput.input():
    modo = line().strip().upper()
    texto = line().strip().upper()
    key = line().strip().upper()

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
    text += 'X'
  return texto

def texto_a_matriz(texto,textoMatriz):
  aux1 = 0
  aux2 = 0
  for i in range(len(texto)):
    if i % 2 == 0:
      #Se resta 65 para convertir de Ascii a rango 0-26
      textoMatriz[0][aux1] = int(ord(texto[i]) - 65)
      itr1 += 1
    else:
      textoMatriz[1][aux2] = int(ord(texto[i]) - 65)
      itr2 += 1
  return textoMatriz

def key_a_matriz(key,keyMatriz):
  aux3 = 0
  for i in range(2):
    for j in range(2):
      keyMatriz[i][j] = ord (key[aux3]) -65
  return keyMatriz

def validar_obtener_inv(keyMatriz):
  #Calcular el determinante
  determ = keyMatriz[0][0] * keyMatriz[1][1] - keyMatriz[0][1] * keyMatriz[1][0]
  determ = determ % 26    #Se aplica mod 26

  #¿Tiene inverso?
  mul_inv = -1
  for i in range(26):
    temp_inv = determ * i
    if temp_inv % 26 == 1:
      mul_inv = i
      break
    else:
      continue
  if mul_inv == -1:
    raise ValueError("No existe inverso")


def encrypt(texto,key):
  #Calcular tamaño de matrices para el texto
  row = 2
  col = int(len(texto) / 2) 

  #Matrices en 0
  textoMatriz = np.zeros((row, col), dtype=int)
  keyMatriz = np.zeros((2,2) ,dtype=int)


  texto = formato_texto(texto)
  textoMatriz = texto_a_matriz(texto,textoMatriz)
  keyMatriz = key_a_matriz(key,keyMatriz)

  pass

def decrypt(text,key):
  pass

def main():
  resultado = datos_archivo()
  print(resultado)