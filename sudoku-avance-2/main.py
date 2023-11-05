from sudoku_printer import SudokuPrinter
from sudoku_solver import SudokuSolver
import time

def main():
    sudoku_solver = SudokuSolver()
    sudoku_printer = SudokuPrinter()

    numeroFilas = sudoku_printer.ingreso()
    sudoku_solver.NumFilas = numeroFilas

    time.sleep(1)
    sudoku_solver.resultado()


if __name__ == "__main__":
    main()
