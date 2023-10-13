import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image

if __name__ == "__main__":
    print(">> welcome to Counter app v1.0, developed by: Artin (Ketchup d) <<")


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


def minusfunc(a=1):
    global count
    try:
        num = count.cget(key="text")
    except Exception as ea:
        print(ea)
    else:
        if num <= 0:
            pass
        else:
            try:
                num -= 1
            except Exception as ea:
                print(ea)
            else:
                count.config(text=num)


def resetfunc(a=1):
    global count
    count.config(text=0)


def themechanger():
    global dark, light, theme, reset, add, labelcopyright, count, frame_theme, frame_buttons, frame_count

    if theme.cget(key="image") == "pyimage2":
        window.config(bg="#1A1A1A")
        frame_buttons.config(bg="#1A1A1A")
        frame_theme.config(bg="#1A1A1A")
        frame_count.config(bg="#1A1A1A")
        count.config(fg="white", bg="#1A1A1A")
        reset.config(bg="#1A1A1A", image=reset_dark)
        add.config(bg="#1A1A1A", image=add_dark)
        minus.config(bg="#1A1A1A", image=minus_dark)
        labelcopyright.config(bg="#1A1A1A")
        theme.config(image=light, bg="#1A1A1A")

    elif theme.cget(key="image") == "pyimage3":
        window.config(bg="#f0f0f0")
        frame_buttons.config(bg="#f0f0f0")
        frame_theme.config(bg="#f0f0f0")
        frame_count.config(bg="#f0f0f0")
        count.config(fg="black", bg="#f0f0f0")
        reset.config(bg="#f0f0f0", image=reset_light)
        add.config(bg="#f0f0f0", image=add_light)
        minus.config(bg="#f0f0f0", image=minus_light)
        labelcopyright.config(bg="#f0f0f0")
        theme.config(image=dark, bg="#f0f0f0")


window = tk.Tk()

window.title("Counter")

icon = tk.PhotoImage(file="models//title_icon.png")
window.iconphoto(False, icon)

menu_bar = tk.Menu(window)
menu1 = tk.Menu(menu_bar, tearoff=False)

menu1.add_command(label="Add", command=addfunc, accelerator="Space, Enter")
menu1.add_command(label="Minus", command=minusfunc, accelerator="BackSpace")
menu1.add_command(label="Reset", command=resetfunc, accelerator="Ctrl+R")
menu1.add_command(label="Close", command=window.quit, accelerator="Alt+F4")

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

font_text = font.Font(size=18)
fontbuttons = font.Font(size=14)

frame_buttons = tk.Frame(window)
frame_buttons.pack(side="bottom")

count = tk.Label(frame_count, text=0, font=font_text)
count.pack(pady=15)

reset_light = ImageTk.PhotoImage(Image.open("models//reset_light.png"))
reset_dark = ImageTk.PhotoImage(Image.open("models//reset_dark.png"))
reset = tk.Button(frame_buttons, image=reset_light, borderwidth=0,
                  command=resetfunc)
reset.pack(side="bottom", pady=22)

add_light = ImageTk.PhotoImage(Image.open("models//add_light.png"))
add_dark = ImageTk.PhotoImage(Image.open("models//add_dark.png"))
add = tk.Button(frame_buttons,
                image=add_light, borderwidth=0, command=addfunc)
add.pack(side="right", pady=12)

minus_light = ImageTk.PhotoImage(Image.open("models//minus_light.png"))
minus_dark = ImageTk.PhotoImage(Image.open("models//minus_dark.png"))
minus = tk.Button(frame_buttons,
                  image=minus_light, borderwidth=0, command=minusfunc)
minus.pack(side="left", pady=12)

window.bind_all("<Return>", addfunc)
window.bind_all("<space>", addfunc)
window.bind_all("<BackSpace>", minusfunc)
window.bind_all("<Control-r>", resetfunc)

window.mainloop()
