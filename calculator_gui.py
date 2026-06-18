import tkinter as tk
from tkinter import ttk, messagebox
from subprocess import Popen, PIPE, STDOUT

history = []


def calculate():

    operation = operation_var.get()

    try:

        if operation == "sqrt":

            num1 = num1_entry.get()

            process = Popen(
                [
                    'java',
                    '-jar',
                    'JavaCalculator.jar',
                    'sqrt',
                    num1
                ],
                stdout=PIPE,
                stderr=STDOUT
            )

            result = process.stdout.read().decode().strip()

            history.append(
                f"√{num1} = {result}"
            )

        else:

            num1 = num1_entry.get()
            num2 = num2_entry.get()

            process = Popen(
                [
                    'java',
                    '-jar',
                    'JavaCalculator.jar',
                    operation,
                    num1,
                    num2
                ],
                stdout=PIPE,
                stderr=STDOUT
            )

            result = process.stdout.read().decode().strip()

            symbols = {
                "add": "+",
                "subtract": "-",
                "multiply": "*",
                "divide": "/",
                "power": "^"
            }

            history.append(
                f"{num1} {symbols.get(operation)} {num2} = {result}"
            )

        result_label.config(
            text=f"Result: {result}"
        )

        update_history()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


def update_history():

    history_box.delete(
        "1.0",
        tk.END
    )

    for item in history:

        history_box.insert(
            tk.END,
            item + "\n"
        )


def clear_all():

    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)

    result_label.config(
        text="Result:"
    )

    history.clear()

    history_box.delete(
        "1.0",
        tk.END
    )


def operation_changed(event):

    if operation_var.get() == "sqrt":
        num2_entry.delete(0, tk.END)
        num2_entry.config(state="disabled")
    else:
        num2_entry.config(state="normal")


root = tk.Tk()

root.title(
    "Cross-Language Calculator - Python & Java Integration"
)

root.geometry("750x650")

tk.Label(
    root,
    text="Python GUI integrated with Java Calculation Engine",
    font=("Arial", 10)
).pack(pady=5)

# Number 1

tk.Label(
    root,
    text="Number 1",
    font=("Arial", 12)
).pack()

num1_entry = tk.Entry(
    root,
    width=40
)

num1_entry.pack(pady=5)

# Operation

tk.Label(
    root,
    text="Operation",
    font=("Arial", 12)
).pack()

operation_var = tk.StringVar()

operation_combo = ttk.Combobox(
    root,
    textvariable=operation_var,
    values=[
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "sqrt"
    ],
    state="readonly"
)

operation_combo.pack(pady=5)

operation_combo.current(0)

operation_combo.bind(
    "<<ComboboxSelected>>",
    operation_changed
)

# Number 2

tk.Label(
    root,
    text="Number 2",
    font=("Arial", 12)
).pack()

num2_entry = tk.Entry(
    root,
    width=40
)

num2_entry.pack(pady=5)

# Buttons

tk.Button(
    root,
    text="Calculate",
    width=15,
    command=calculate
).pack(pady=10)

tk.Button(
    root,
    text="Clear",
    width=15,
    command=clear_all
).pack(pady=5)

# Result

result_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 14, "bold")
)

result_label.pack(pady=15)

# History

tk.Label(
    root,
    text="Calculation History",
    font=("Arial", 12, "bold")
).pack()

history_box = tk.Text(
    root,
    width=60,
    height=12
)

history_box.pack(pady=10)

root.mainloop()