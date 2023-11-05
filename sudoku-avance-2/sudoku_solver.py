import pyautogui as pg

class SudokuSolver:

    def __init__(self):
        self.NumFilas = []

    def verificacion(self, x, y, n):
        return (
            self.verificar_fila(x, y, n) and
            self.verificar_columna(x, y, n) and
            self.verificar_subcuadricula(x, y, n)
        )

    def verificar_fila(self, x, y, n):
        for i in range(16):
            if self.NumFilas[i][x] == n and i != y:
                return False
        return True

    def verificar_columna(self, x, y, n):
        for i in range(16):
            if self.NumFilas[y][i] == n and i != x:
                return False
        return True

    def verificar_subcuadricula(self, x, y, n):
        x0 = (x // 4) * 4
        y0 = (y // 4) * 4

        for i in range(y0, y0 + 4):
            for j in range(x0, x0 + 4):
                if self.NumFilas[i][j] == n:
                    return False
        return True

    def resultado(self):
        for y in range(16):
            for x in range(16):
                if self.NumFilas[y][x] == 0:
                    for n in range(1, 17):
                        if self.verificacion(x, y, n):
                            self.NumFilas[y][x] = n
                            self.resultado()
                            self.NumFilas[y][x] = 0
                    return
        self.imprimirNumFilas()
        input("Seguimos?")

    def imprimirNumFilas(self):
        final = []
        str_fin = []
        borde = []

        for i in range(16):
            final.append(self.NumFilas[i])

        for lista in final:
            for num in lista:
                str_num = str(num)
                if len(str_num) == 1:
                    str_num = ' ' + str_num  # Agregar un espacio en blanco para números de un dígito
                str_fin.append(str_num)

        for num in str_fin:
            pg.press(num)
            pg.hotkey('right')
            borde.append(num)

            longitud = len(borde)
            if longitud % 16 == 0:
                for i in range(16):
                    pg.hotkey('left')
                pg.hotkey('down')