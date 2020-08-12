opcion = input("Conversor de moneda\nEscoja: \n1.Cambiar de pesos colombianos a dólares \n2.Pasar de dólares a pesos colombianos")

if opcion == '1':
  pesos = input("¿Cuantos pesos colombianos tienes?")
  pesos = float(pesos)
  valor_dolar = 3875
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $" + dolares + "dólares")
elif opcion == '2' :
  dolares = input("¿Cuantos dólares  tienes?")
  dolares = float(dolares)
  valor_pesos = 1/3875
  pesos = dolares / valor_pesos
  pesos = round(pesos, 2)
  pesos = str(pesos)
  print("Tienes $" + pesos + "pesos")
