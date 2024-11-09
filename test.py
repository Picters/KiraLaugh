import tkinter as tk
from tkinter import messagebox
import platform
import psutil
import socket
import time
import uuid

# Функции для получения информации
def get_system_info():
    info = [
        f"System: {platform.system()}",
        f"Node Name: {platform.node()}",
        f"Release: {platform.release()}",
        f"Version: {platform.version()}",
        f"Machine: {platform.machine()}",
        f"Processor: {platform.processor()}",
        f"Architecture: {platform.architecture()[0]}",
        f"UUID: {uuid.getnode()}",
        f"IP Address: {socket.gethostbyname(socket.gethostname())}",
        f"Uptime: {int(time.time() - psutil.boot_time()) // 3600} hours",
        f"Boot Time: {time.ctime(psutil.boot_time())}"
    ]
    return "\n".join(info)

def get_cpu_info():
    cpu_info = [
        f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz",
        f"CPU Usage: {psutil.cpu_percent(interval=1)}%",
        f"Logical Cores: {psutil.cpu_count(logical=True)}",
        f"Physical Cores: {psutil.cpu_count(logical=False)}",
        f"CPU Times: {psutil.cpu_times()}",
    ]
    # Добавляем данные о температуре, если поддерживается системой
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items():
                for entry in entries:
                    cpu_info.append(f"{name} Temperature: {entry.current}°C")
    return "\n".join(cpu_info)

def get_memory_info():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    memory_info = [
        f"Total Memory: {memory.total // (1024 ** 2)} MB",
        f"Available Memory: {memory.available // (1024 ** 2)} MB",
        f"Used Memory: {memory.used // (1024 ** 2)} MB",
        f"Memory Usage: {memory.percent}%",
        f"Swap Total: {swap.total // (1024 ** 2)} MB",
        f"Swap Used: {swap.used // (1024 ** 2)} MB",
        f"Swap Usage: {swap.percent}%"
    ]
    return "\n".join(memory_info)

def get_disk_info():
    disk_info = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.extend([
            f"Device: {partition.device}",
            f"Mountpoint: {partition.mountpoint}",
            f"File System Type: {partition.fstype}",
            f"Total Size: {usage.total // (1024 ** 3)} GB",
            f"Used: {usage.used // (1024 ** 3)} GB",
            f"Free: {usage.free // (1024 ** 3)} GB",
            f"Percentage: {usage.percent}%\n"
        ])
    return "\n".join(disk_info)

def get_network_info():
    net_io = psutil.net_io_counters()
    network_info = [
        f"Bytes Sent: {net_io.bytes_sent // (1024 ** 2)} MB",
        f"Bytes Received: {net_io.bytes_recv // (1024 ** 2)} MB",
        f"Packets Sent: {net_io.packets_sent}",
        f"Packets Received: {net_io.packets_recv}",
        f"Active Connections: {len(psutil.net_connections())}"
    ]
    # Добавляем информацию по каждому сетевому интерфейсу
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                network_info.append(f"{interface_name} IP Address: {address.address}")
                network_info.append(f"{interface_name} Netmask: {address.netmask}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                network_info.append(f"{interface_name} MAC Address: {address.address}")
    return "\n".join(network_info)

# Отображение информации
def show_system_info():
    messagebox.showinfo("System Information", get_system_info())

def show_cpu_info():
    messagebox.showinfo("CPU Information", get_cpu_info())

def show_memory_info():
    messagebox.showinfo("Memory Information", get_memory_info())

def show_disk_info():
    messagebox.showinfo("Disk Information", get_disk_info())

def show_network_info():
    messagebox.showinfo("Network Information", get_network_info())

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
