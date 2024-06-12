#ALGORITMO LAS VEGAS
"""import random
import math

def punto():
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt(x**2 + y**2) <= 1:
            return (x, y)

# Generar un punto que cumple con la condición
point = punto()
print("Punto generado:", point)"""



#ALGORITMO MONTE CARLO
import random
import math

def monte_carlo_pi(num_muestra):
    dentro_circulo = 0

    for _ in range(num_muestra):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            dentro_circulo += 1

    return (dentro_circulo / num_muestra) * 4

# Número de muestras
num_muestra = 100

# Aproximar el valor de pi
aprox_pi = monte_carlo_pi(num_muestra)
print("Aproximación de pi:", aprox_pi)
