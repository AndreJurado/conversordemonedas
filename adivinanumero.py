import random

def run():
  numero=random.randint(1,100)
  elegido=int(input('Elige un número del 1 al 100'))

  while numero != elegido:
    if elegido < numero:
      print("busca un número más grande")

    else:
      print("busca un número más pequeño") 
    elegido = int(input('elige otro número')) 

  print('Ganaste')


if __name__ == "__main__":
  run()