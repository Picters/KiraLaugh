import tkinter as tk
from tkinter import messagebox
import time

# Настройки
PASSWORD = "1234"  # Установите ваш пароль

def check_password(event=None):
    entered_password = password_entry.get()
    if entered_password == PASSWORD:
        root.destroy()  # Закрыть окно блокировки
    else:
        messagebox.showerror("Ошибка", "Неверный пароль")
        password_entry.delete(0, tk.END)

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%d.%m.%Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)

# Создание главного окна
root = tk.Tk()
root.title("Заблокировано")
root.attributes('-fullscreen', True)
root.configure(bg='black')

# Блокировка возможности закрыть окно
root.bind("<Alt-F4>", lambda e: "break")
root.bind("<Escape>", lambda e: "break")

# Фон (можно добавить изображение)
background = tk.Label(root, bg='black')
background.place(relwidth=1, relheight=1)

# Отображение времени
time_label = tk.Label(root, font=('Helvetica', 48), fg='white', bg='black')
time_label.pack(pady=100)
date_label = tk.Label(root, font=('Helvetica', 24), fg='white', bg='black')
date_label.pack()

# Поле ввода пароля
password_frame = tk.Frame(root, bg='black')
password_frame.pack(pady=50)

password_label = tk.Label(password_frame, text="Пароль:", font=('Helvetica', 24), fg='white', bg='black')
password_label.pack(side=tk.LEFT, padx=10)

password_entry = tk.Entry(password_frame, show='*', font=('Helvetica', 24))
password_entry.pack(side=tk.LEFT)
password_entry.focus()

# Кнопка "Ввод"
submit_button = tk.Button(root, text="Войти", command=check_password, font=('Helvetica', 18))
submit_button.pack(pady=20)

# Привязка клавиши Enter к проверке пароля
root.bind('<Return>', check_password)

# Запуск обновления времени и даты
update_time()

# Запуск главного цикла
root.mainloop()
