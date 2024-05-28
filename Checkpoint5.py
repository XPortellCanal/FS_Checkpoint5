#cree un bucle For de Python.
for num in range(1,11):
  print(num)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(num1, num2, num3):
  return(num1 + num2 + num3)

suma(2,11,25)  
  
#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
lambda_suma = lambda num1, num2, num3: num1 + num2 + num3

lambda_suma(2,11,25)

# Utilizando la siguiente lista y variable, determine
# si el valor de la variable coincide o no con un valor de la lista.
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

string_included = nombre in lista_nombre

if string_included:
  print(f"{nombre} esta incluido en la lista")
else:
  print(f"{nombre} NO esta incluido en la lista")

