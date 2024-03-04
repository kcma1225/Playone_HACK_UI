from tkinter import *
from src.comp.placeholder import EntryWithPlaceholder as ph

window = Tk()
window.geometry("700x450")
window.configure(bg = "#FFFFFF")

#----------------------logo-------------------
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
logo_image_source = PhotoImage(
    file=r"assets/login/logo.png")
logo = canvas.create_image(
    638.0,
    80.0,
    image=logo_image_source
)
#------------------------------------------------------

#-------------------AC--------------------
canvas.create_text(
    41.0,
    63.0,
    anchor="nw",
    text="帳號(account):",
    fill="#000000",
    font=("微軟正黑體", 14 * -1)
)

ac_image_source = PhotoImage(file=r"assets/login/ac.png")

ac_image = canvas.create_image(
    205.5,
    111.0,
    image = ac_image_source
)
ac = ph(window,"請輸入帳號")

ac.place(
    x=45.0,
    y=91.0,
    width=324.0,
    height=40.0
)

#------------------------------------------

#-----------------------PW-----------------
canvas.create_text(
    42.0,
    148.0,
    anchor="nw",
    text="密碼(password):",
    fill="#000000",
    font=("微軟正黑體", 14 * -1)
)

pw_image_source = PhotoImage(file=r"assets/login/pw.png")

pw_image = canvas.create_image(
    205.5,
    196.0,
    image=pw_image_source
)
pw = ph(window, "請輸入密碼")

pw.place(
    x=45.0,
    y=176.0,
    width=324.0,
    height=40.0
)
#--------------------------------------------------

#----------------verify code-----------------------
canvas.create_text(
    234.0,
    276.0,
    anchor="nw",
    text="驗證碼(verification code)",
    fill="#000000",
    font=("微軟正黑體", 13 * -1)
)

verify_image_source = PhotoImage(file=r"assets/login/verify.png")

verify_image = canvas.create_image(
    350.5,
    316.5,
    image=verify_image_source
)
verify = ph(window, "請輸入驗證碼")

verify.place(
    x=238.0,
    y=303.5,
    width=227,
    height=27.5
)
#--------------------------------------------------

#--------------------login button-------------------
login_btn_source = PhotoImage(
    file=r"assets/login/login.png")
login_btn = Button(
    image=login_btn_source,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
login_btn.place(
    x=273.0,
    y=395.0,
    width=142.0,
    height=41.0
)
#------------------------------------------------------

#-----------------------remember ac-------------------
canvas.create_text(
    319.0,
    357.0,
    anchor="nw",
    text="記住此帳密",
    fill="#000000",
    font=("微軟正黑體", 14 * -1)
)

remember_btn_source = PhotoImage(
    file=r"assets/login/remember.png")
remember_btn = Button(
    image=remember_btn_source,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
remember_btn.place(
    x=292.0,
    y=354.0,
    width=20.0,
    height=20.0
)
#------------------------------------------------------


#------------------version------------------------
canvas.create_text(
    639.0,
    427.0,
    anchor="nw",
    text="ver 1.0",
    fill="#000000",
    font=("arial", 15 * -1)
)
#------------------------------------------------



window.resizable(False, False)
window.mainloop()
