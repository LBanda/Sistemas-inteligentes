#diccionario de reglas

REGLAS = {
    'moneda': 'pedir-codigo',
    'a1': 'servir-bebida1',
    'a2': 'servir-bebida2',
    'a3': 'servir-bebida3'
}

class AgenteReflex:
    #Agente racional de tipo tabla

    def __init__(self, reglas):
        self.reglas = reglas

    def actuar(self, percepcion, accion_basica=''):
        #Actua segun la percepcion y devuelve una accion
        if not percepcion:
            return accion_basica
        
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]
        return accion_basica



print("-- Agente Reflex: Maquina Expendedora --")

expendedora = AgenteReflex(REGLAS)

percepcion = input("indicar Percepcion: ")

while percepcion:
    accion = expendedora.actuar(percepcion, 'reiniciar')
    print(accion)
    percepcion = input("indicar Percepcion: ")