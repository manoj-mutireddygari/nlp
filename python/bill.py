import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Item prices
prices = {
    "Dosa": 30,
    "Cookies": 15,
    "Tea": 10,
    "Coffee": 20,
    "Juice": 40,
    "Pancakes": 15,
    "Eggs": 7
}

# Create main window
root = tk.Tk()
root.title("Bill Management")
root.geometry("700x500")
root.configure(bg="white")

# Title label with a futuristic style
title_label = tk.Label(
    root, text="BILL MANAGEMENT", font=("Arial", 20, "bold"), bg="white", fg="#FF6600"
)
title_label.pack(pady=20)

# Frame for menu and quantity input
frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

# Menu frame with a futuristic style
menu_frame = tk.Frame(frame, bg="#f2f2f2", bd=2, relief="ridge")
menu_frame.grid(row=0, column=0, padx=10, sticky="n")
menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#FF6600")
menu_label.pack(pady=5)
for item, price in prices.items():
    item_label = tk.Label(menu_frame, text=f"{item} - Rs.{price}/unit", font=("Arial", 10), bg="#f2f2f2", fg="black")
    item_label.pack(anchor="w")

# Input frame for quantities with a futuristic style
quantity_frame = tk.Frame(frame, bg="white")
quantity_frame.grid(row=0, column=1, padx=10)
quantity_entries = {}
for i, item in enumerate(prices.keys()):
    item_label = tk.Label(quantity_frame, text=item, font=("Arial", 12, "bold"), fg="black", bg="white")
    item_label.grid(row=i, column=0, padx=5, pady=2, sticky="w")
    quantity_entries[item] = tk.Entry(quantity_frame, width=5, font=("Arial", 12), bg="#FFDDC1", fg="black", bd=0)
    quantity_entries[item].grid(row=i, column=1, padx=5, pady=2)

# Result frame for displaying bill total with a futuristic style
result_frame = tk.Frame(frame, bg="#f2f2f2", bd=2, relief="ridge")
result_frame.grid(row=0, column=2, padx=10)
bill_label = tk.Label(result_frame, text="Bill", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#FF6600")
bill_label.pack(pady=5)
total_var = tk.StringVar(value="Rs. 0.00")
total_display = tk.Label(result_frame, textvariable=total_var, font=("Arial", 16), fg="#FF6600", bg="#f2f2f2")
total_display.pack(pady=5)

# Calculate total function
def calculate_total():
    total = 0
    for item, entry in quantity_entries.items():
        quantity = entry.get()
        if quantity == "":
            quantity = 0
        try:
            quantity = int(quantity)
            total += quantity * prices[item]
        except ValueError:
            messagebox.showerror("Input Error", f"Please enter a valid quantity for {item}.")
            return
    total_var.set(f"Rs. {total:.2f}")

# Reset quantities function
def reset():
    for entry in quantity_entries.values():
        entry.delete(0, tk.END)
    total_var.set("Rs. 0.00")

# Print bill function
def print_bill():
    bill_text = "Bill Summary\n"
    bill_text += f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    total = 0
    for item, entry in quantity_entries.items():
        quantity = entry.get()
        if quantity == "":
            quantity = 0
        try:
            quantity = int(quantity)
            if quantity > 0:
                cost = quantity * prices[item]
                bill_text += f"{item}: {quantity} x Rs.{prices[item]} = Rs.{cost}\n"
                total += cost
        except ValueError:
            pass
    bill_text += f"\nTotal: Rs. {total:.2f}"
    messagebox.showinfo("Bill", bill_text)

# Buttons for actions with futuristic style
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)

button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#FF6600",
    "fg": "white",
    "activebackground": "#FF4500",
    "activeforeground": "black",
    "bd": 0,
    "relief": "flat",
    "width": 10,
}

reset_button = tk.Button(button_frame, text="Reset", command=reset, **button_style)
reset_button.grid(row=0, column=0, padx=10)
total_button = tk.Button(button_frame, text="Total", command=calculate_total, **button_style)
total_button.grid(row=0, column=1, padx=10)
print_button = tk.Button(button_frame, text="Print Bill", command=print_bill, **button_style)
print_button.grid(row=0, column=2, padx=10)

# Add shadows to make the UI pop
for widget in [title_label, menu_label, bill_label, total_display, reset_button, total_button, print_button]:
    widget.configure(relief="flat")

root.mainloop()
