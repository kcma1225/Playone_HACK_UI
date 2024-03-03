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
button_image_1 = PhotoImage(
    file=r"assets/page_2/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=10.0,
    y=10.0,
    width=30.0,
    height=30.0
)

entry_image_1 = PhotoImage(
    file=r"assets/page_2/entry_1.png")
entry_bg_1 = canvas.create_image(
    349.5,
    277.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=34.0,
    y=127.0,
    width=631.0,
    height=299.0
)

button_image_2 = PhotoImage(
    file=r"assets/page_2/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=232.0,
    y=86.0,
    width=47.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=r"assets/page_2/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=166.0,
    y=86.0,
    width=47.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=r"assets/page_2/button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=100.0,
    y=86.0,
    width=47.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=r"assets/page_2/button_5.png")
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=34.0,
    y=86.0,
    width=47.0,
    height=30.0
)

button_image_6 = PhotoImage(
    file=r"assets/page_2/button_6.png")
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=531.0,
    y=96.0,
    width=44.0,
    height=28.0
)

button_image_7 = PhotoImage(
    file=r"assets/page_2/button_7.png")
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=531.0,
    y=58.0,
    width=44.0,
    height=28.0
)

button_image_8 = PhotoImage(
    file=r"assets/page_2/button_8.png")
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=464.0,
    y=96.0,
    width=44.0,
    height=28.0
)

button_image_9 = PhotoImage(
    file=r"assets/page_2/button_9.png")
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=464.0,
    y=58.0,
    width=44.0,
    height=28.0
)

button_image_10 = PhotoImage(
    file=r"assets/page_2/button_10.png")
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=397.0,
    y=96.0,
    width=44.0,
    height=28.0
)

button_image_11 = PhotoImage(
    file=r"assets/page_2/button_11.png")
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=397.0,
    y=58.0,
    width=44.0,
    height=28.0
)

canvas.create_text(
    539.0,
    39.0,
    anchor="nw",
    text="199",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    475.0,
    38.0,
    anchor="nw",
    text="90",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    409.0,
    38.0,
    anchor="nw",
    text="30",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

button_image_12 = PhotoImage(
    file=r"assets/page_2/button_12.png")
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=562.0,
    y=10.0,
    width=50.608428955078125,
    height=23.103759765625
)

entry_image_2 = PhotoImage(
    file=r"assets/page_2/entry_2.png")
entry_bg_2 = canvas.create_image(
    345.0,
    20.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=153.0,
    y=8.0,
    width=384.0,
    height=23.0
)

canvas.create_text(
    82.0,
    12.0,
    anchor="nw",
    text="直播網址",
    fill="#000000",
    font=("Inter", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
