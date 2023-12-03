import tkinter as tk
import sys
import os
import pyperclip

user_input = input("Input Your Url : \n")
root = tk.Tk()


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


os.system("@echo off")

print("=========================")
print("==~Input Url In Alt Text~==")
print("=========================\n")

output = f"![Alt text]({user_input})"

print(output)

root.title("~Alt Text Copy~")
root.iconbitmap(resource_path("./resources/images/icon/app.ico"))
root.geometry("300x300")
root.resizable(False, False)
root.attributes("-topmost", True)
root.configure(bg="black")


def copy():
    pyperclip.copy(output)


os.system("@echo on")

buttom_copy = tk.Button(
    root,
    text="~~~~~~~~~~Copy Url~~~~~~~~~~",
    font=("Arial", 16),
    command=copy,
    width=28,
)
buttom_copy.pack()
buttom_copy.config(fg="red", bg="black")


root.mainloop()
