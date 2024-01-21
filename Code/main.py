import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import pyautogui as pg
import pygetwindow as gw
import schedule
import webbrowser


def is_telegram_open():
    telegram_windows = gw.getWindowsWithTitle("Telegram")
    if telegram_windows:
        return telegram_windows[0].isMinimized
    else:
        return False


def start_telegram_bots():
    try:
        if not is_telegram_open():
            # Open telegram | You should put the Telegram app on your app bar first
            pg.hotkey("winleft", "1")

        # It's not mandatory, you can just delete this piece of code.
        # But pin your bots TRX and BNB bots they should be first in the list

        # Click on the first bot in the pinned list
        pg.moveTo(262, 127)
        pg.click(262, 127)

        # Click on the input field
        pg.moveTo(983, 875, 0.1)
        pg.click(983, 875)

        # Write /start and press enter
        pg.typewrite("/start")
        pg.typewrite(["enter"])

        pg.moveTo(1287, 930, 0.5)
        pg.click(1287, 930)

        # Same for the second bot
        pg.moveTo(238, 213)
        pg.click(238, 213)

        pg.moveTo(983, 875, 0.1)
        pg.click(983, 875)

        pg.typewrite("/start")
        pg.typewrite(["enter"])

        pg.moveTo(1287, 930, 0.5)
        pg.click(1287, 930)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def start_telegram_bots_threaded():
    threading.Thread(target=start_telegram_bots).start()


def stop_telegram_bots():
    root.destroy()


def on_link_click():
    webbrowser.open("https://telegra.ph/KAK-POLZOVATSYA-FARM-BOTOM-01-18")


# Периодический запуск проверки, если Telegram открыт
schedule.every(10).seconds.do(start_telegram_bots_threaded)

# GUI setup
root = tk.Tk()
root.title("TRX-BNB TIME TO PICK UP COINS")
root.geometry("500x300+700+200")

icon_path = "C:/Code Projects/GUI/TRX-BNB-AUTO-GRABBER/Code/mainericon.ico"
root.iconbitmap(icon_path)

label = tk.Label(root, text="TRX-BNB СОБИРАТЕЛЬ МОНЕТ", font="Arial 15 bold")
label.pack(pady=30)

# Пути к изображениям
image_path1 = "C:/Code Projects/GUI/TRX-BNB-AUTO-GRABBER/Code/trx_img.png"
image_path2 = "C:/Code Projects/GUI/TRX-BNB-AUTO-GRABBER/Code/bnb_img.png"

# Загрузка изображений с помощью Pillow и изменение размера
image1 = Image.open(image_path1)
image1 = image1.resize((125, 100), resample=Image.LANCZOS)
img1 = ImageTk.PhotoImage(image1)

image2 = Image.open(image_path2)
image2 = image2.resize((80, 80), resample=Image.LANCZOS)
img2 = ImageTk.PhotoImage(image2)

# Создание виджетов Label с измененными изображениями
image_label1 = tk.Label(root, image=img1)
image_label1.place(x=10, y=150)  # Установка координат для первого изображения

image_label2 = tk.Label(root, image=img2)
image_label2.place(x=400, y=110)  # Установка координат для второго изображения

label2 = tk.Label(root, text="КАК ПОЛЬЗОВАТЬСЯ?", font="Arial 8 bold", fg="blue")
label2.pack(side="bottom", anchor="e")
label2.bind("<Button-1>", lambda event: on_link_click())

# Создание и размещение кнопки "Stop"
stop_button = tk.Button(root, text="Stop", width=10, height=1, bg="red", fg="white", command=stop_telegram_bots)
stop_button.pack(side="bottom")

# Создание и размещение кнопки "Start"
start_button = tk.Button(root, text="Start", width=10, height=1, bg="green", fg="white",
                         command=start_telegram_bots_threaded)

start_button.pack(side="bottom", pady=20)

root.mainloop()
