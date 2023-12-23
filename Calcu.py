import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error, try again.")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calcupy")

# Entry widget to display the input and result
entry = tk.Entry(root, width=20, font=("Helvetica", 16), bd=10, insertwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define the button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0),
]

# Create and place buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 16),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col)

# Run the Tkinter main loop
root.mainloop()

