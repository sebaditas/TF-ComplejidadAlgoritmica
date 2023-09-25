import pyautogui as pg
import time
import string

class SudokuSolver:

    def __init__(self):
        self.NumFilas = list()
#desde aqui
    def verificacion(self, x, y, n):
        return (
            self.verificar_fila(x, y, n) and
            self.verificar_columna(x, y, n) and
            self.verificar_subcuadricula(x, y, n)
        )

    def verificar_fila(self, x, y, n):
        for i in range(9):
            if self.NumFilas[i][x] == n and i != y:
                return False
        return True

    def verificar_columna(self, x, y, n):
        for i in range(9):
            if self.NumFilas[y][i] == n and i != x:
                return False
        return True

    def verificar_subcuadricula(self, x, y, n):
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3

        for i in range(y0, y0 + 3):
            for j in range(x0, x0 + 3):
                if self.NumFilas[i][j] == n:
                    return False
        return True
#hasta aqui usamos divide y conquista para separar los problemas de verificacion en cuatro

    def resultado(self):
        for y in range(9):
            for x in range(9):
                if self.NumFilas[y][x] == 0:
                    for n in range(1, 10):
                        if self.verificacion(x, y, n):
                            self.NumFilas[y][x] = n
                            self.resultado()
                            self.NumFilas[y][x] = 0
                    return
        self.imprimirNumFilas()
        input("Seguimos?")

    def imprimirNumFilas(self):
        final = list()
        str_fin = list()
        borde = list()

        for i in range(9): final.append(self.NumFilas[i])

        for listas in final:
            for num in listas: str_fin.append(str(num))

        for num in str_fin:
            pg.press(num)
            pg.hotkey('right')
            borde.append(num)
            if len(borde) % 9 == 0:
                for i in range(9):
                    pg.hotkey('left')
                pg.hotkey('down')
