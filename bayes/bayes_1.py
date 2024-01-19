# Ejemplo simple teorema de Bayes aplicado a estimación de un sólo parámetro.
a_priori = 0.003
likelihood = 0.99
evidencia = 0.01

a_posteriori = likelihood * a_priori / evidencia
print(a_posteriori)

