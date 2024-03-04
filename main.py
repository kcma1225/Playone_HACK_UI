# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


window = Tk()

window.geometry("700x450")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 450,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    500.0,
    16.0,
    642.0,
    56.0,
    fill="#E7E7E7",
    outline="")

canvas.create_text(
    550.0,
    24.0,
    anchor="nw",
    text="USER 1",
    fill="#000000",
    font=("Inter", 20 * -1)
)

image_image_1 = PhotoImage(
    file=r"assets/main/image_1.png")
image_1 = canvas.create_image(
    522.0,
    36.0,
    image=image_image_1
)

canvas.create_text(
    67.0,
    111.0,
    anchor="nw",
    text="直播刷禮物",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    268.0,
    111.0,
    anchor="nw",
    text="飆評紀錄",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    571.0,
    409.0,
    anchor="nw",
    text="歷史紀錄查看",
    fill="#000000",
    font=("Inter", 16 * -1)
)

button_image_1 = PhotoImage(
    file=r"assets/main/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=653.0,
    y=33.0,
    width=43.0,
    height=23.0
)

button_image_2 = PhotoImage(
    file=r"assets/main/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=566.0,
    y=348.0,
    width=110.0,
    height=54.0
)

button_image_3 = PhotoImage(
    file=r"assets/main/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=232.0,
    y=33.0,
    width=140.0,
    height=70.0
)

button_image_4 = PhotoImage(
    file=r"assets/main/button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=38.0,
    y=33.0,
    width=140.0,
    height=70.0
)
window.resizable(False, False)
window.mainloop()
