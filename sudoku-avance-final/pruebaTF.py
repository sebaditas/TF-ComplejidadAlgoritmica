import tkinter as tk
from tkinter import ttk
from sudoku_solver import SudokuSolver
from sudoku_printer import SudokuPrinter
import time

class SudokuGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.sudoku_solver = SudokuSolver()
        self.sudoku_printer = SudokuPrinter()
        self.root.geometry("540x500+300+100")

        self.button_font = ('Arial', 14)
        self.title_font = ('Arial', 24, 'bold')
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='black')

        space_frame = tk.Frame(self.root, height=10, bg='black')
        space_frame.pack()

        self.style = ttk.Style()

        self.style.configure('TButton', background='white', foreground='black', font=('Arial', 14))

        self.sudoku_frame = tk.Frame(self.root, bg='black')
        self.sudoku_frame.pack()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.sudoku_frame, width=3, bg='white', fg='black', font=('Arial', 14), bd=2)
                entry.grid(row=i, column=j, ipadx=10, ipady=10)
        
        solve_button = tk.Button(self.root, text="Resolver Sudoku", command=self.solve_sudoku, bg='darkgreen', fg='white', font=self.button_font)
        solve_button.pack(side=tk.LEFT, padx=5, pady=10)

        clear_button = tk.Button(self.root, text="Limpiar Sudoku", command=self.clear_sudoku, bg='red', fg='white', font=self.button_font)
        clear_button.pack(side=tk.RIGHT, padx=5, pady=10)

    def get_sudoku_input(self):
        num_filas = []
        for i in range(9):
            row_values = []
            for j in range(9):
                entry = self.sudoku_frame.grid_slaves(row=i, column=j)[0]
                value = entry.get()
                if value.isdigit():
                    row_values.append(int(value))
                else:
                    row_values.append(0)
            num_filas.append(row_values)
        return num_filas

    def solve_sudoku(self):
        numero_filas = self.get_sudoku_input()
        self.sudoku_solver.NumFilas = numero_filas

        time.sleep(1)
        self.sudoku_solver.resultado()

    def clear_sudoku(self):
        for i in range(9):
            for j in range(9):
                entry = self.sudoku_frame.grid_slaves(row=i, column=j)[0]
                entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()