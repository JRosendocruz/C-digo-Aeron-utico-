# Definir un diccionario que mapee cada letra del código a su versión extendida
codigo_aeronautico = {'A': 'ALFA','B': 'BRAVO','C': 'CHARLIE','D': 'DELTA','E': 'ECHO','F': 'FOXTROT','G': 'GOLF','H': 'HOTEL',
    'I': 'INDIA',
    'J': 'JULIETT',
    'K': 'KILO',
    'L': 'LIMA',
    'M': 'MIKE',
    'N': 'NOVEMBER',
    'O': 'OSCAR',
    'P': 'PAPA',
    'Q': 'QUEBEC',
    'R': 'ROMEO',
    'S': 'SIERRA',
    'T': 'TANGO',
    'U': 'UNIFORM',
    'V': 'VICTOR',
    'W': 'WHISKEY',
    'X': 'XRAY',
    'Y': 'YANKEE',
    'Z': 'ZULU'
}
def convertir_codigo(codigo):
    version_extendida = []
    for letra in codigo:
        # Convertir la letra a mayúsculas para manejar entradas en minúsculas
        letra = letra.upper()        
        if letra in codigo_aeronautico:           
            version_extendida.append(codigo_aeronautico[letra])
        else:            
            version_extendida.append('DESCONOCIDO')   
    return ' '.join(version_extendida)
codigo_ingresado = input("Ingrese una palabra para convertir: ")
print("El código aeronáutico extendido es:", convertir_codigo(codigo_ingresado))
