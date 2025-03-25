import tkinter as tk
from tkinter import ttk, messagebox
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")
        master.resizable(False, False)

        self.expression = "" 
        self.result_label = tk.Label(
            master, text="0", font=("Arial", 20), anchor="e", padx=10
        ) 
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=10)
        button_layout = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            ("=", 4, 1),  
            (".", 4, 2),
            ("+", 4, 3),
        ]
        for btn_text, row, col in button_layout:
            button = tk.Button(
                master,
                text=btn_text,
                font=("Arial", 16),
                padx=20,
                pady=15,
                command=lambda text=btn_text: self.button_click(text),
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        clear_button = tk.Button(
            master,
            text="C",
            font=("Arial", 16),
            padx=20,
            pady=15,
            bg="red",
            fg="white",
            command=self.clear,
        )
        clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        for col in range(4):
            master.columnconfigure(col, weight=1)
        for row in range(6):
            master.rowconfigure(row, weight=1)
    def button_click(self, text):
        if text == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result) 
                self.result_label.config(text=result) 
            except Exception:
               messagebox.showerror("Ошибка", "Неверное выражение") 
               self.expression = ""
               self.result_label.config(text="0") 
        else:
          self.expression += text
          self.result_label.config(text=self.expression)
    def clear(self):
        self.expression = ""
        self.result_label.config(text="0")
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()