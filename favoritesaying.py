import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Favorite Saying")

    saying = "Everyone wants a village but no one wants to be a villager"
    
    label = tk.Label(root, text=saying, wraplength=400, font=("Arial", 14))
    label.pack(padx=20, pady=20)

    root.mainloop()

main()
