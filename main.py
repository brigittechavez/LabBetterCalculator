def addmultiplenumbers (numbers):

  total = 0
  for num in numbers:
    total += num

  return total
  
def multiplymultiplenumbers (numbers):

  if not numbers:
    return 0

  total = 1
  for num in numbers:
    total *= num

  return total
  
def isitaninteger(num):

  return isinstance(num, int) or (isinstance(num, float) and num == int(num))


def isiteven(num):

  if not isitaninteger(num):
    return False
  return num % 2 == 0



def mostrar_menu():
  print("\n===== CALCULADORA BÁSICA =====")
  print("1. Sumar múltiples números")
  print("2. Multiplicar múltiples números")
  print("3. Verificar si un número es par")
  print("4. Verificar si un número es entero")
  print("5. Salir")
  
  return input("Seleccione una opción (1-5): ")

def obtener_numeros():
  entrada = input("integre los números separador por espacios: ")
  numeros = []

  for num in entrada.split():
    numeros.append(float(num))

  return numeros

def main():
  print("Hello learners! Bienvenid@ a tu calculadora de confianza")

  while True:
    opcion = mostrar_menu()

    if opcion == "1":
      numeros = obtener_numeros()
      resultado = addmultiplenumbers(numeros)
      print(f"La suma de {numeros} es: {resultado}")

    elif opcion == "2":
      numeros = obtener_numeros()
      resultado = multiplymultiplenumbers(numeros)
      print(f"La multiplicación de {numeros} es: {resultado}")

    elif opcion == "3":
      num = float(input("Ingrese un número para verificar si es par: "))
      resultado = isiteven(num)
      if resultado:     
        print(f"{num} es par: {resultado}")

      else:
        print(f"El número {num} NO es par o entero.")

    elif opcion =="4":
      num = float(input("Ingrese un número: "))
      resultado = isitaninteger(num)
      if resultado:
        print(f"El número {num} ES un entero.")
      else:
          print(f"El número {num} NO es un entero.")
                
    elif opcion == "5":
      print("¡Gracias por usar la Calculadora Básica!")
            
            
    else:
      print("Opción inválida. Por favor seleccione una opción válida (1-5).")
    

      

if __name__=="__main__":
  main()