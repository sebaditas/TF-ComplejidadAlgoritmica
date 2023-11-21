import tkinter as tk
from tkinter import ttk
from sudoku_solver import SudokuSolver
from sudoku_printer import SudokuPrinter
import time
from ttkthemes import ThemedStyle

class SudokuGameGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Vamos a resolver!!")
        self.root.geometry("700x470+200+50")

        style = ThemedStyle(self.root)
        style.set_theme("clam")

        self.style = ttk.Style()
        self.style.configure('TButton', background='white', foreground='black', font=('Arial', 14))

        self.background_label = tk.Label(root, bg='black')
        self.background_label.place(relwidth=1, relheight=1)

        frame = tk.Frame(root, bg='black', bd=5)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        title_label = tk.Label(frame, text="Sudoku Bot", font=('Arial', 24, 'bold'), bg='black', fg='white')
        title_label.grid(row=1, column=1, pady=(0, 80), padx=(20, 0))

        self.image_label = tk.Label(frame, bg='white')
        self.image_label.grid(row=1, column=0, pady=(20, 0), sticky='w')

        play_button = tk.Button(frame, text="Play Sudoku", command=self.open_sudoku_board, bg='darkmagenta', fg='white', font=('Arial', 14, 'bold'),
                                bd=3)
        play_button.grid(row=1, column=1, pady=(20, 0), padx=(20, 0))

        exit_button = tk.Button(frame, text="Exit Sudoku", command=self.root.destroy, bg='darkred', fg='white', font=('Arial', 14, 'bold'),
                                bd=3)
        exit_button.grid(row=1, column=1, pady=(140, 0), padx=(20, 0))

        self.image_path = "image.png"
        self.load_image()

    def load_image(self):
        try:
            img = tk.PhotoImage(file=self.image_path).subsample(2)
            self.image_label.config(image=img)
            self.image_label.image = img
        except tk.TclError:
            print(f"No se pudo cargar la imagen en {self.image_path}")

    def open_sudoku_board(self):
        sudoku_board_window = tk.Toplevel(self.root)
        sudoku_board_gui = SudokuGUI(sudoku_board_window)

class SudokuGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Bot")
        self.sudoku_solver = SudokuSolver()
        self.sudoku_printer = SudokuPrinter()
        self.root.geometry("550x520+300+100")

        self.button_font = ('Arial', 14)
        self.title_font = ('Arial', 24, 'bold')
        # self.entry_font = ('Arial', 14)

        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='black')

        space_frame = tk.Frame(self.root, height=10, bg='black')
        space_frame.pack()

        self.style = ttk.Style()

        self.style.configure('TButton', background='white', foreground='black', font=('Arial', 14))
        # self.style.configure('TEntry', background='white', foreground='black', font=self.entry_font, bd=2)

        self.sudoku_frame = tk.Frame(self.root, bg='black')
        self.sudoku_frame.pack()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.sudoku_frame, width=3, bg='white', fg='black', font=('Arial', 14, 'bold'), bd=2, relief=tk.RIDGE, justify=tk.CENTER,
                                highlightbackground='black')
                entry.grid(row=i, column=j, ipadx=10, ipady=10, padx=1, pady=1)

        solve_button = tk.Button(self.root, text="Resolver Sudoku", command=self.solve_sudoku, bg='darkgreen', fg='white', font=('Arial', 14, 'bold'))
        solve_button.pack(side=tk.LEFT, padx=5, pady=10)

        clear_button = tk.Button(self.root, text="Limpiar Sudoku", command=self.clear_sudoku, bg='red', fg='white', font=('Arial', 14, 'bold'))
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
    app = SudokuGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
