import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image


def addfunc(a=1):
    global count
    try:
        num = count.cget(key="text")
    except Exception as ea:
        print(ea)
    else:
        try:
            num += 1
        except Exception as ea:
            print(ea)
        else:
            count.config(text=num)


def resetfunc(a=1):
    global count
    count.config(text=0)


def themechanger():
    global dark, light, theme, reset, add, labelcopyright, count, frame_theme, frame_buttons, frame_count

    if theme.cget(key="image") == "pyimage1":
        window.config(bg="#1A1A1A")
        frame_buttons.config(bg="#1A1A1A")
        frame_theme.config(bg="#1A1A1A")
        frame_count.config(bg="#1A1A1A")
        count.config(fg="white", bg="#1A1A1A")
        reset.config(fg="white", bg="#1A1A1A")
        add.config(fg="white", bg="#1A1A1A")
        labelcopyright.config(bg="#1A1A1A")
        theme.config(image=light, bg="#1A1A1A")

    elif theme.cget(key="image") == "pyimage2":
        window.config(bg="#f0f0f0")
        frame_buttons.config(bg="#f0f0f0")
        frame_theme.config(bg="#f0f0f0")
        frame_count.config(bg="#f0f0f0")
        count.config(fg="black", bg="#f0f0f0")
        reset.config(fg="black", bg="#f0f0f0")
        add.config(fg="black", bg="#f0f0f0")
        labelcopyright.config(bg="#f0f0f0")
        theme.config(image=dark, bg="#f0f0f0")


window = tk.Tk()

window.title("Counter")

menu_bar = tk.Menu(window)
menu1 = tk.Menu(menu_bar, tearoff=False)

menu1.add_command(label="Close", command=window.quit, accelerator="Alt+F4")
menu1.add_command(label="Reset", command=resetfunc, accelerator="Ctrl+R")

menu_bar.add_cascade(label="menu", menu=menu1)

window.config(menu=menu_bar)

dark = ImageTk.PhotoImage(Image.open(
    "models\\dark.png"))
light = ImageTk.PhotoImage(Image.open(
    "models\\light.png"))

frame_theme = tk.Frame(window, width=30, height=30)
frame_theme.pack(side="top", fill="both", pady=5, padx=5)
theme = tk.Button(frame_theme, image=dark, command=themechanger, borderwidth=0)
theme.pack(side="left")

frame_count = tk.Frame(window)
frame_count.pack(side="top", fill="both")

labelcopyright = tk.Label(text="© 2023 - Counter app",
                          fg="#949494")
labelcopyright.pack(side="bottom")

window.geometry("300x300")

fonttext = font.Font(size=15)
fontbuttons = font.Font(size=14)

frame_buttons = tk.Frame(window)
frame_buttons.pack(side="bottom")

count = tk.Label(frame_count, text=0, font=fonttext)
count.pack(pady=15)

reset = tk.Button(frame_buttons, text="Reset", font=fontbuttons,
                  width=7, height=-1, command=resetfunc)
reset.pack(side="bottom", pady=30)

add = tk.Button(frame_buttons, text="Add",
                font=fontbuttons, width=7, command=addfunc)
add.pack(side="bottom", pady=10)

window.bind_all("<Return>", addfunc)
window.bind_all("<space>", addfunc)
window.bind_all("<Control-r>", resetfunc)

window.mainloop()
