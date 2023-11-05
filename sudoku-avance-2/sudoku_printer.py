import numpy as np

class SudokuPrinter:

    def __init__(self):
        self.numFilas = []

    def ingreso(self):

        condicion = True

        while condicion:
            fila = input('Fila: ')
            enteros = []

            for n in fila.split():
                enteros.append(int(n))
            self.numFilas.append(enteros)

            longitud = len(self.numFilas)

            if longitud == 16:
                break
            print('Fila ', str(longitud), ' Completado')

        return self.numFilas
