import tkinter as tk

# Function to update the input field
def button_click(number):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + str(number))

# Function to clear the input field
def clear():
    input_field.delete(0, tk.END)

# Function to perform the calculation
def calculate():
    current = input_field.get()
    try:
        result = eval(current)
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except Exception:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the input field
input_field = tk.Entry(window, width=20, font=('Arial', 16))
input_field.grid(row=0, column=0, columnspan=4)

# Create the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, font=('Arial', 12),
              command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create the clear button
clear_button = tk.Button(window, text="C", width=5, height=2, font=('Arial', 12), command=clear)
clear_button.grid(row=row_val, column=col_val)

# Run the application
window.mainloop()
