import random as rr

import tkinter as bk
from tkinter import ttk
from ttkthemes import themed_tk as tk
import pyperclip
from tkinter import messagebox


root= tk.ThemedTk()
root.geometry("440x70")
root.resizable(height=False, width=False)
root.title("Password Generator")
root.iconbitmap(r'assets\Webalys-Kameleon.pics-Key.ico')


pass_word = bk.Label(root, text="Password")
pass_word.place(x=0, y=5)

im = bk.PhotoImage(file="assets\info.png")

def generate():
    Entry.delete(0, "end")
    length=var2.get()
    val1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    val2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val3 = "abcdefghijklmnopqrstuvwxyz"
    strength = var1.get()

    try:
     if strength==1:
       password = rr.sample(val3, length )
       final = "".join(password)
       Entry.insert(10, final)

     elif strength==2:
       password = rr.sample(val2, length)
       final = "".join(password)
       Entry.insert(10, final)

     elif strength==3:
      password = rr.sample(val1, length)
      final = "".join(password)
      Entry.insert(10, final)

     else:
      messagebox.showerror(title="Password Generator", message="Please select the strength of the password.")

    except:
     messagebox.showerror(title="Password Generator", message="Please try again with a smaller length.")

def copy():
 try:
  pass_w=Entry.get()
  pyperclip.copy(pass_w)
  messagebox.showinfo(title="Password Generator", message="The password is copied to the clipboard.")
 except:
  messagebox.showerror(title="Password Generator", message="Please try again.")


def inf():
    messagebox.showinfo(title="Password Generator", message="Password Generator is an application programmed with python to generate random passwords. Thanks to the developer - Pratham Khanduja.")
var1 = bk.IntVar()
var2 = bk.IntVar()


Entry = bk.Entry(root, width=25)
Entry.place(x=64,y=5)

length_label=bk.Label(root, text="Length")
length_label.place(x=5, y=40)


copy_but=ttk.Button(root, text="Copy", command=copy)
copy_but.place(x=224, y=5)

gen_but=ttk.Button(root, text="Generate", command=generate)
gen_but.place(x=314, y=5)

radio_low= ttk.Radiobutton(root, text="Low", variable=var1, value=1)
radio_low.place(x=218, y=40)

radio_medium= ttk.Radiobutton(root, text="Medium", variable=var1, value=2)
radio_medium.place(x=268, y=40)

radio_strong= ttk.Radiobutton(root, text="Strong", variable=var1, value=3)
radio_strong.place(x=338, y=40)

select_length=ttk.Combobox(root, textvariable=var2)
select_length['values']=(8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)
select_length.current(0)
select_length.bind('<<ComboboxSelected>>')
select_length.place(x=68, y=40)

info = ttk.Button(root, image=im, command=inf)
info.place(x=398,y=20)




root.mainloop()
