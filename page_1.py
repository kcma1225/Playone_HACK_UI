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
    file=r"assets/page_1/button_1.png")
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
    file=r"assets/page_1/entry_1.png")
entry_bg_1 = canvas.create_image(
    153.0,
    310.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=21.0,
    y=292.0,
    width=264.0,
    height=34.0
)

canvas.create_text(
    21.0,
    262.0,
    anchor="nw",
    text="送禮次數",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=r"assets/page_1/entry_2.png")
entry_bg_2 = canvas.create_image(
    153.0,
    216.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=21.0,
    y=198.0,
    width=264.0,
    height=34.0
)

canvas.create_text(
    21.0,
    168.0,
    anchor="nw",
    text="禮物ＩＤ (點選)",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=r"assets/page_1/entry_3.png")
entry_bg_3 = canvas.create_image(
    153.0,
    122.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=21.0,
    y=104.0,
    width=264.0,
    height=34.0
)

canvas.create_text(
    21.0,
    74.0,
    anchor="nw",
    text="直播網址",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=r"assets/page_1/entry_4.png")
entry_bg_4 = canvas.create_image(
    592.0,
    249.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=499.0,
    y=62.0,
    width=186.0,
    height=373.0
)

canvas.create_text(
    549.0,
    29.0,
    anchor="nw",
    text="禮物列表",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=r"assets/page_1/entry_5.png")
entry_bg_5 = canvas.create_image(
    392.0,
    249.5,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=299.0,
    y=62.0,
    width=186.0,
    height=373.0
)

canvas.create_text(
    336.0,
    29.0,
    anchor="nw",
    text="使用者列表",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_2 = PhotoImage(
    file=r"assets/page_1/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=60.0,
    y=385.0,
    width=142.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
