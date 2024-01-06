#diccionario de Acciones

ACCIONES = {
    'moneda': 'pedir-codigo',
    'moneda,a1': 'servir-bebida1',
    'moneda,a2': 'servir-bebida2',
    'moneda,a3': 'servir-bebida3',
    'moneda,a1,moneda': 'pedir-codigo',
    'moneda,a2,moneda': 'pedir-codigo',
    'moneda,a3,moneda': 'pedir-codigo',
    'moneda,a1,moneda,a1': 'servir-bebida1',
    'moneda,a1,moneda,a2': 'servir-bebida2',
    'moneda,a1,moneda,a3': 'servir-bebida3',
    'moneda,a2,moneda,a1': 'servir-bebida1',
    'moneda,a2,moneda,a2': 'servir-bebida2',
    'moneda,a2,moneda,a3': 'servir-bebida3',
    'moneda,a3,moneda,a1': 'servir-bebida1',
    'moneda,a3,moneda,a2': 'servir-bebida2',
    'moneda,a3,moneda,a3': 'servir-bebida3'
}

class AgenteTabla:
    #Agente racional de tipo tabla

    def __init__(self, acciones):
        self.acciones = acciones
        self.percepciones = ""

    def actuar(self, percepcion, accion_basica=''):
        #Actua segun la percepcion y devuelve una accion
        if not percepcion:
            return accion_basica
        if len(self.percepciones) != 0:
            self.percepciones += ','
        self.percepciones += percepcion
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones = ''
        return accion_basica



print("-- Agente Tabla: Maquina Expendedora --")

expendedora = AgenteTabla(ACCIONES)

percepcion = input("indicar Percepcion: ")

while percepcion:
    accion = expendedora.actuar(percepcion, 'reiniciar')
    print(accion)
    percepcion = input("indicar Percepcion: ")