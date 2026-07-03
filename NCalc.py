import tkinter as tk
import math
import re

root = tk.Tk()
root.title("Advanced Expression Calculator")
root.geometry("950x250")
root.configure(bg="#2f3542")

header = tk.Label(
    root,
    text="Enter your expression:",
    font=("Arial", 14, "bold"),
    bg="#2f3542",
    fg="#f1f2f6"
)
header.pack(pady=15)

entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=70,
    bd=3,
    relief="flat",
    justify="center"
)
entry.pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#2f3542"
)
result_label.pack(pady=10)


def calculate():
    expression = entry.get()

    if not expression.strip():
        result_label.config(text="Please enter an expression", fg="#ffa500")
        return


    expression = re.sub(r'(\d)(?=\()', r'\1*', expression)
    expression = re.sub(r'(\d)(?=[A-Za-z])', r'\1*', expression)
    expression = re.sub(r'(\))(?=\()', r'\1*', expression)
    expression = re.sub(r'(\))(?=[A-Za-z])', r'\1*', expression)
    expression = re.sub(r'(pi|e)(?=\()', r'\1*', expression)


    expression = re.sub(
        r'\batan\((.*?)\)',
        r'math.degrees(math.atan(\1))',
        expression
    )

    expression = re.sub(
        r'\bsin\((.*?)\)',
        r'math.sin(math.radians(\1))',
        expression
    )

    expression = re.sub(
        r'\bcos\((.*?)\)',
        r'math.cos(math.radians(\1))',
        expression
    )

    expression = re.sub(
        r'\btan\((.*?)\)',
        r'math.tan(math.radians(\1))',
        expression
    )

    expression = re.sub(
        r'\bcosec\((.*?)\)',
        r'(1/math.sin(math.radians(\1)))',
        expression
    )

    expression = re.sub(
        r'\bsec\((.*?)\)',
        r'(1/math.cos(math.radians(\1)))',
        expression
    )

    expression = re.sub(
        r'\bcot\((.*?)\)',
        r'(1/math.tan(math.radians(\1)))',
        expression
    )

    expression = re.sub(r'\bpi\b', 'math.pi', expression)
    expression = re.sub(r'\be\b', 'math.e', expression)

    print("Evaluating:", expression)

    try:
        result = eval(expression, {"math": math})
        result_label.config(
            text=f"Result: {round(result, 4)}",
            fg="#2ed573"
        )

    except Exception as e:
        print(e)
        result_label.config(
            text="Error: Invalid Expression",
            fg="#ff4757"
        )


calc_button = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="#1e90ff",
    fg="white",
    activebackground="#70a1ff",
    activeforeground="white",
    relief="flat",
    width=12,
    command=calculate
)
calc_button.pack(pady=15)

root.bind("<Return>", lambda event: calculate())

root.mainloop()