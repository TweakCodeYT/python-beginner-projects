import tkinter as tk

#GUI setup
root = tk.Tk()
root.title ("Even or odd Checker")
root.geometry ("300x200")

# Input label and entry field
tk.Label(root, text="Enter a number:") .pack(pady=5)
entry = tk.Entry(root, justify="center")
entry.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font = ("Helvetica", 12))
result_label.pack(pady=10)

# Check if number is even or odd
def check_even_odd():
    try:
        number = int(entry.get())
        if number % 2 == 0 :
            result_label.config(text=f"{number} is EVEN ✅", fg="green")
        else:
            result_label.config(text=f"{number} is ODD ❌", fg="blue")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")

# Check button
check_button = tk.Button(root, text="Check", command=check_even_odd)
check_button.pack(pady=10)

# Run the app
root.mainloop()