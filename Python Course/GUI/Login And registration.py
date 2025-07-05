import tkinter as tk
from tkinter import messagebox

def validate_input(username, password):
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return False
    return True

def save_to_html(username, password):
    with open("user_data.html", "a") as file:
        file.write(f"<p>Username: {username}, Password: {password}</p>\n")

def check_credentials(username, password):
    with open("user_data.html", "r") as file:
        for line in file:
            if f"Username: {username}" in line and f"Password: {password}" in line:
                return True
    return False

def login():
    username = entry_username.get()
    password = entry_password.get()

    if validate_input(username, password):
        if check_credentials(username, password):
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login", "Invalid username or password")

def register():
    username = entry_username.get()
    password = entry_password.get()

    if validate_input(username, password):
        save_to_html(username, password)
        messagebox.showinfo("Register", f"User {username} registered successfully!")

# Create the main window
root = tk.Tk()
root.title("Social Media Login and Registration")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 200

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place widgets with styling
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, anchor="center")

label_username = tk.Label(frame, text="Username:", font=("Helvetica", 12))
label_username.grid(row=0, column=0, pady=10, sticky=tk.E)

entry_username = tk.Entry(frame, font=("Helvetica", 10))
entry_username.grid(row=0, column=1, pady=10, padx=10)

label_password = tk.Label(frame, text="Password:", font=("Helvetica", 12))
label_password.grid(row=1, column=0, pady=10, sticky=tk.E)

entry_password = tk.Entry(frame, show="*", font=("Helvetica", 10))
entry_password.grid(row=1, column=1, pady=10, padx=10)

button_login = tk.Button(frame, text="Login", command=login, font=("Helvetica", 12), width=15)
button_login.grid(row=2, column=0, columnspan=2, pady=15)

button_register = tk.Button(frame, text="Register", command=register, font=("Helvetica", 12), width=15)
button_register.grid(row=3, column=0, columnspan=2, pady=15)

# Run the main loop
root.mainloop()
