import time
import threading
import pyautogui
import tkinter as tk
from tkinter import messagebox
import keyboard

class Clicker:
    def __init__(self, root):
        self.root = root
        self.root.title("连点器")
        self.click_count = tk.IntVar()
        self.click_count.set(100)
        self.click_interval = tk.DoubleVar()
        self.click_interval.set(0.1)
        self.is_clicking = False
        self.click_thread = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="点击次数:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.click_count).grid(row=0, column=1)

        tk.Label(self.root, text="点击间隔(秒):").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.click_interval).grid(row=1, column=1)

        start_button = tk.Button(self.root, text="开始连点", command=self.start_clicking)
        start_button.grid(row=2, column=0, columnspan=2, pady=20)

        stop_button = tk.Button(self.root, text="停止连点", command=self.stop_clicking)
        stop_button.grid(row=3, column=0, columnspan=2, pady=20)

    def start_clicking(self):
        if not self.is_clicking:
            self.is_clicking = True
            self.click_thread = threading.Thread(target=self.click)
            self.click_thread.start()

    def stop_clicking(self):
        self.is_clicking = False

    def click(self):
        count = self.click_count.get()
        interval = self.click_interval.get()
        for _ in range(count):
            if not self.is_clicking:
                break
            pyautogui.click()
            time.sleep(interval)
            if keyboard.is_pressed('shift'):
                self.stop_clicking()
                messagebox.showinfo("提示", "检测到Shift键按下，停止连点。")
                break

if __name__ == "__main__":
    root = tk.Tk()
    clicker = Clicker(root)
    root.mainloop()
