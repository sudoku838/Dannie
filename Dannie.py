import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END
import os

class AddressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Адресная книжка")
        self.root.geometry("400x400")  # Установка фиксированного размера окна
        # Создание фрейма для ввода данных
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        #Поля ввода
        self.name_label = tk.Label(self.frame, text="Имя:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.address_label = tk.Label(self.frame, text="Адрес:")
        self.address_label.grid(row=1, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.frame, width=30)
        self.address_entry.grid(row=1, column=1, padx=5, pady=5)
        self.city_label = tk.Label(self.frame, text="Город:")
        self.city_label.grid(row=2, column=0, padx=5, pady=5)
        self.city_entry = tk.Entry(self.frame, width=30)
        self.city_entry.grid(row=2, column=1, padx=5, pady=5)
        #поле для email
        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.grid(row=3, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.frame, width=30)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)
        #Кнопки
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)
        self.add_button = tk.Button(self.button_frame, text="Добавить", command=self.add_entry, width=10)
        self.add_button.grid(row=0, column=0, padx=5)
        self.delete_button = tk.Button(self.button_frame, text="Удалить", command=self.delete_entry, width=10)
        self.delete_button.grid(row=0, column=1, padx=5)
        self.save_button = tk.Button(self.button_frame, text="Сохранить", command=self.save_to_file, width=10)
        self.save_button.grid(row=0, column=2, padx=5)
        self.listbox = Listbox(self.root, width=50, height=10)
        self.listbox.pack(pady=10)
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.load_from_file()
    def add_entry(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        email = self.email_entry.get()
        if name and address and city and email:
            entry = f"{name}, {address}, {city}, {email}"
            self.listbox.insert(END, entry)
            self.clear_entries()
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля.")
    def delete_entry(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите запись для удаления.")
    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.email_entry.delete(0, END)
    def save_to_file(self):
        try:
            with open(os.path.join(self.data_folder, "address_book.txt"), "w", encoding="utf-8") as file:
                for i in range(self.listbox.size()):
                    file.write(self.listbox.get(i) + "\n")
            messagebox.showinfo("Успех", "Данные успешно сохранены!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {str(e)}")
    def load_from_file(self):
        try:
            file_path = os.path.join(self.data_folder, "address_book.txt")
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    for line in file:
                        self.listbox.insert(END, line.strip())
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {str(e)}")
if __name__ == "__main__":
    root = tk.Tk()
    app = AddressApp(root)
    root.mainloop()