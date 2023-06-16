import tkinter as tk

# create a new instance of Tkinter
window = tk.Tk()

# set the window title
window.title("Calculator")

# set the window size
window.geometry("300x200")

# create the input fields
label1 = tk.Label(window, text="Enter First Number :")
label1.grid(column=0, row=0)
input1 = tk.Entry(window)
input1.grid(column=1, row=0)

label2 = tk.Label(window, text="Enter Second Number :")
label2.grid(column=0, row=1)
input2 = tk.Entry(window)
input2.grid(column=1, row=1)

# create the operator dropdown
label3 = tk.Label(window, text="Select Operator :")
label3.grid(column=0, row=2)
operator = tk.StringVar(window)
operator.set("+")
operator_dropdown = tk.OptionMenu(window, operator, "+", "-", "*", "/")
operator_dropdown.grid(column=1, row=2)

# create the result label
result_label = tk.Label(window, text="")
result_label.grid(column=1, row=4)

# create the calculate button
def calculate():
    try:
        num1 = float(input1.get())
        num2 = float(input2.get())
        op = operator.get()
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)

# run the window
window.mainloop()
