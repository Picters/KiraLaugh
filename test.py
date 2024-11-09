import tkinter as tk
from tkinter import messagebox
import platform
import psutil
import socket
import time

# Функции для получения информации
def get_system_info():
    info = [
        f"System: {platform.system()}",
        f"Release: {platform.release()}",
        f"Version: {platform.version()}",
        f"Machine: {platform.machine()}",
        f"Processor: {platform.processor()}",
        f"CPU Count: {psutil.cpu_count(logical=False)} (Physical), {psutil.cpu_count()} (Logical)",
        f"CPU Usage: {psutil.cpu_percent()}%",
        f"Memory: {psutil.virtual_memory().total // (1024 ** 2)} MB",
        f"Available Memory: {psutil.virtual_memory().available // (1024 ** 2)} MB",
        f"Used Memory: {psutil.virtual_memory().used // (1024 ** 2)} MB",
        f"Disk Usage (Root): {psutil.disk_usage('/').percent}%",
        f"Total Disk Space: {psutil.disk_usage('/').total // (1024 ** 3)} GB",
        f"Free Disk Space: {psutil.disk_usage('/').free // (1024 ** 3)} GB",
        f"Battery: {psutil.sensors_battery().percent}%" if psutil.sensors_battery() else "No battery detected",
        f"IP Address: {socket.gethostbyname(socket.gethostname())}",
        f"Uptime: {int(time.time() - psutil.boot_time()) // 3600} hours"
    ]
    return "\n".join(info)

def show_system_info():
    messagebox.showinfo("System Information", get_system_info())

def show_cpu_info():
    cpu_info = [
        f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz",
        f"CPU Usage: {psutil.cpu_percent(interval=1)}%",
        f"Logical Cores: {psutil.cpu_count(logical=True)}",
        f"Physical Cores: {psutil.cpu_count(logical=False)}"
    ]
    messagebox.showinfo("CPU Information", "\n".join(cpu_info))

def show_memory_info():
    memory = psutil.virtual_memory()
    memory_info = [
        f"Total Memory: {memory.total // (1024 ** 2)} MB",
        f"Available Memory: {memory.available // (1024 ** 2)} MB",
        f"Used Memory: {memory.used // (1024 ** 2)} MB",
        f"Memory Usage: {memory.percent}%"
    ]
    messagebox.showinfo("Memory Information", "\n".join(memory_info))

def show_disk_info():
    disk = psutil.disk_usage('/')
    disk_info = [
        f"Total Disk Space: {disk.total // (1024 ** 3)} GB",
        f"Used Disk Space: {disk.used // (1024 ** 3)} GB",
        f"Free Disk Space: {disk.free // (1024 ** 3)} GB",
        f"Disk Usage: {disk.percent}%"
    ]
    messagebox.showinfo("Disk Information", "\n".join(disk_info))

def show_network_info():
    network_info = [
        f"IP Address: {socket.gethostbyname(socket.gethostname())}",
        f"Bytes Sent: {psutil.net_io_counters().bytes_sent // (1024 ** 2)} MB",
        f"Bytes Received: {psutil.net_io_counters().bytes_recv // (1024 ** 2)} MB",
        f"Connections: {len(psutil.net_connections())} active"
    ]
    messagebox.showinfo("Network Information", "\n".join(network_info))

# Создание интерфейса
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg="black")

# Кнопки для отображения информации
buttons = [
    ("System", show_system_info),
    ("CPU", show_cpu_info),
    ("Memory", show_memory_info),
    ("Disk", show_disk_info),
    ("Network", show_network_info)
]

for text, command in buttons:
    btn = tk.Button(root, text=text, command=command, font=("Arial", 14), width=15, height=2, bg="gray", fg="white")
    btn.pack(pady=10)

# Закрытие по ESC
root.bind("<Escape>", lambda e: root.destroy())

# Запуск главного цикла
root.mainloop()
