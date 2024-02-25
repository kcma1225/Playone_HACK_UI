from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton
import sqlite3


window = Tk(className=" PLAY ONE Hacker")
window.geometry("700x450")
window.configure(bg = "#FFFFFF")

TABLE_NAME = "ac_table"
ID = "ID"
AC = "account"
PW = "password"

conn = sqlite3.connect(r'src/ac.db')
cursor = conn.cursor()
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({ID} INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {AC} TEXT, {PW} TEXT)")


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
image_image_1 = PhotoImage(
    file=r'assets/frame0/image_1.png')
image_1 = canvas.create_image(
    349.0,
    86.0,
    image=image_image_1
)

canvas.create_text(
    639.0,
    427.0,
    anchor="nw",
    text="ver 1.0",
    fill="#000000",
    font=("Inter SemiBold", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=r'assets/frame0/entry_1.png')
entry_bg_1 = canvas.create_image(
    350.5,
    213.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=193.0,
    y=190.0,
    width=320.0,
    height=45.0
)

entry_image_2 = PhotoImage(
    file=r'assets/frame0/entry_2.png')
entry_bg_2 = canvas.create_image(
    350.5,
    298.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=193.0,
    y=275.0,
    width=320.0,
    height=45.0
)

canvas.create_text(
    186.0,
    165.0,
    anchor="nw",
    text="帳號(account):",
    fill="#000000",
    font=("微軟正黑體", 14 * -1)
)

canvas.create_text(
    187.0,
    250.0,
    anchor="nw",
    text="密碼(password):",
    fill="#000000",
    font=("微軟正黑體", 14 * -1)
)

#---------------------button-------------------------
r_btn = 0

def remember_pw():
    global r_btn
    if r_btn == 0:
        print("以勾")
        r_btn = 1
        
    else:
        print("取消勾勾")
        r_btn = 0

button_image_1 = PhotoImage(
    file=r'assets/frame0/button_1.png')
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=273.0,
    y=395.0,
    width=142.0,
    height=41.0
)

#---------------------check button------------------------------

checkbutton_1 = Checkbutton(
    command=remember_pw,
    relief="flat"
)
checkbutton_1.place(
    x=223.0,
    y=346.0,
    width=20.0,
    height=20.0
)

#-----------------------------------------------

canvas.create_text(
    250.0,
    349.0,
    anchor="nw",
    text="記住此帳密",
    fill="#000000",
    font=("微軟正黑體", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
