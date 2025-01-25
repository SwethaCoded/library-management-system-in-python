import tkinter as tk
class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        self.borrow_label = tk.Label(master, text="Borrow a book:")
        self.borrow_label.grid(row=0, column=0, padx=10, pady=10)
        self.borrow_listbox = tk.Listbox(master, height=5)
        self.borrow_listbox.grid(row=0, column=1, padx=10, pady=10)
        self.books = {"Harry Potter and the Philosopher's Stone-bk1", "The Lord of the Rings-bk2", "Fearless Governance-bk3", "India’s Women Unsung Heroes-bk4","The Bench-bk5","It’s a Wonderful Life-bk6","Let us Dream-bk7", "Will-bk8","The India Story-bk9","400 Days-bk10","How to Prevent the Next Pandemic-bk11","Unfilled Barrels India’s oil story-bk12","India, That is Bharat: Coloniality, Civilisation, Constitution-bk13","The Magic Tree-bk14","Wizards of Ice-bk15","Tower To The Stars-bk16","The Enchanted Ones-bk17","The Blood Dragon-bk18","Nothing In This World-bk18","Dead Man’s WIsh-bk19","The Happy Alien-bk20"} # Available books
        for book in self.books:
            self.borrow_listbox.insert(tk.END, book)
        self.name_label = tk.Label(master, text="Enter your name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.phone_label = tk.Label(master, text="Enter your phone number:")
        self.phone_label.grid(row=2, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)
        self.borrow_button = tk.Button(master, text="Borrow Now", command=self.borrow_book)
        self.borrow_button.grid(row=3, column=1, padx=10, pady=10)
        self.return_label = tk.Label(master, text="Return a book(enter book id):")
        self.return_label.grid(row=4, column=0, padx=10, pady=10)
        self.return_entry = tk.Entry(master)
        self.return_entry.grid(row=4, column=1, padx=10, pady=10)
        self.return_button = tk.Button(master, text="Return Now", command=self.return_book)
        self.return_button.grid(row=5, column=1, padx=10, pady=10)
        self.clear_button = tk.Button(master, text="Clear Fields", command=self.clear_fields)
        self.clear_button.grid(row=6, column=1, padx=10, pady=10)
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    def borrow_book(self):
        book = self.borrow_listbox.get(tk.ACTIVE)
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        result_text = f"Borrowed {book} by {name} ({phone})"
        self.result_label.config(text=result_text)
    def return_book(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        book = self.return_entry.get()
        if name and phone:
            result_text = f"Returned {book} by {name} ({phone})"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Please enter your name and phone number before returning a book.")
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.return_entry.delete(0, tk.END)
root = tk.Tk()
app = LibraryManagementSystem(root)
root.mainloop()