import numpy as np

class SudokuPrinter:

    def __init__(self):
        self.numFilas = list()

    def ingreso(self):

        condicion = not False

        while condicion:
            filas = input('Fila: ')
            enteros = list()

            for n in filas:
                enteros.append(int(n))
            self.numFilas.append(enteros)
        
            longitud = len(self.numFilas)

            if longitud == 9: break
            print('Fila ', str(longitud), ' Completado')

        return self.numFilas
