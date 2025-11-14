import tkinter as tk

def show_info():
    info_label.config(text=f"Name: Faith Bonuke\nAddress: 3397 Maureen LN, Stillwater, Minnesota")

def main():
    root = tk.Tk()
    root.title("Personal Info")

    show_button = tk.Button(root, text="Show Info", command=show_info)
    show_button.pack(pady=10)
    
    global info_label
    info_label = tk.Label(root, text="", font=("Arial", 12))
    info_label.pack(pady=10)
    
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=10)
    
    # Start the GUI loop
    root.mainloop()

main()
