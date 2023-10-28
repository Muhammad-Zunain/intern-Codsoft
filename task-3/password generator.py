
# ----------------------------------------------------- Import -------------------------------------------------------------- #

import random
from customtkinter import *
from CTkMessagebox import CTkMessagebox
import tkinter
from PIL import Image,ImageTk

root = CTk()
set_appearance_mode("dark")
set_default_color_theme("blue")

w = 650
h = 700

root.geometry(f"{w}x{h}")
root.title("Password Generator")
root.resizable("false","false")
img = CTkImage(Image.open("Password Generator.jpg"),size=(650,210))

# ----------------------------------------------------- GUI -------------------------------------------------------------- #

def Mainmenu():

    radio = StringVar(value="other")


    label = CTkLabel(root, text="",image=(img)) # --------Top Label------
    label.pack()

    label_name = CTkLabel(root, text="Enter Name :", font=CTkFont(family="arial", size=15, weight="bold"),  # ------Name Label-------
                          text_color="#8a8a8a")
    label_name.place(relx=0.1, rely=0.36, anchor=tkinter.NW)

    entry_name = CTkEntry(root, height=40, placeholder_text="Name", width=400, border_width=2, border_color="#3d66d9")
    entry_name.place(relx=0.19, rely=0.43)

    label_len = CTkLabel(root, text="Enter length of password :", font=CTkFont(family="arial", size=15, weight="bold"), # --------Password Label-------
                         text_color="#8a8a8a")
    label_len.place(relx=0.1, rely=0.53, anchor=tkinter.NW)

    entry_len = CTkEntry(root, height=40, placeholder_text="Lenght in number", width=400, border_width=2,
                         border_color="#3d66d9")
    entry_len.place(relx=0.19, rely=0.6)

    label_comp = CTkLabel(root, text="Select Complexity :", font=CTkFont(family="arial", size=15, weight="bold"),
                          text_color="#8a8a8a")
    label_comp.place(relx=0.1, rely=0.69, anchor=tkinter.NW)

    easy_radio = CTkRadioButton(root, text="Easy", border_width_checked=5, text_color="#8a8a8a",
                                border_color="#3d66d9", variable=radio, value="Easy")
    easy_radio.place(relx=0.17, rely=0.75)

    strong_radio = CTkRadioButton(root, text="Strong", border_width_checked=5, text_color="#8a8a8a",
                                  border_color="#3d66d9", variable=radio, value="Strong")
    strong_radio.place(relx=0.42, rely=0.75)

    very_strong_radio = CTkRadioButton(root, text="Very Strong", border_width_checked=5, text_color="#8a8a8a",
                                       border_color="#3d66d9", variable=radio, value="Very Strong")
    very_strong_radio.place(relx=0.62, rely=0.75)

    button = CTkButton(root, text="Generate", width=400, height=50,font=CTkFont(family="arial", weight="bold", size=20)  # -------Button-------
                       , border_color="white", border_width=2,corner_radius=10, command=lambda: generate(entry_len, radio,entry_name))
    button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


    # ----------------------------------------------------- Python Code -------------------------------------------------------------- #

def generate(num, complexity, name):
            value = num.get()
            item = complexity.get()
            if value != "" and item != "":
                dict = {"alphabets": "abcdefghijklmnopqrstyvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "special_chars": "~%\!@#-$&*_?"
                    , "number": "0123456789"}
                pswd = ""
                if value.isdigit():
                    if item != "other":
                        if item == "Easy":
                            for i in range(int(value)):
                                pswd = pswd + random.choice(dict["alphabets"] + dict["number"])

                        elif item == "Strong":
                            for i in range(int(value)):
                                str = dict["alphabets"]
                                str = str[20:46]
                                pswd = pswd + random.choice(dict["number"] + str)

                        elif item == "Very Strong":
                            for i in range(int(value)):
                                str = dict["alphabets"]
                                str = str[36:]
                                pswd = pswd + random.choice(dict["special_chars"] + dict["number"] + str)
                        CTkMessagebox(message=f'Password :  {pswd}',title="Password",icon="check",font=CTkFont(size=15))
                        num.delete(0, END)
                        complexity.set("other")
                        name.delete(0,END)
                    else:
                        CTkMessagebox(message="Select Complexity", title="Error", icon="warning")
                else:
                    CTkMessagebox(message="Invalid Password Lenght", title="Error", icon="warning")
                    num.delete(0, END)
            else:
                num.delete(0, END)
                complexity.set("other")
                name.delete(0, END)
                CTkMessagebox(message="Empty Input", title="Error", icon="cancel")

Mainmenu()
root.mainloop()