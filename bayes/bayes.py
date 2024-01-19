# importando modulos necesarios
import pymc3 as pm


# El problema de la moneda
# de 100 lanzamientos 80 caras
n = 100
caras = 80


# Creación del modelo
niter = 2000
with pm.Model() as modelo_moneda:
    # a priori
    p = pm.Beta('p', alpha=2, beta=2)
    # likelihood
    y = pm.Binomial('y', n=n, p=p, observed=caras)


# Realizando el muestreo para la inferencia
with modelo_moneda:
    trace = pm.sample(niter, njobs=4)


# Analizando los resultados
pm.traceplot(trace, varnames=['p'], lines={'p':.8})
pass

# Información resumen. 
#Vemos que hay un 95% de probabilidades de que el valor de sesgo este entre
# .706 y .864
pm.summary(trace)