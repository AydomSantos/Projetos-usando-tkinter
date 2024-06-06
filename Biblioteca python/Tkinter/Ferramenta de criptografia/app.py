from tkinter import *
from tkinter import messagebox
import base64


def encrypt():
    password = code.get()
    if password == "1234":
        screen_dois = Toplevel(screen)
        screen_dois.geometry("400x200")
        screen_dois.config(bg="#ed3833")

        message = text_um.get(1.0, END)
        # Encode message as bytes using UTF-8 for wider character support
        encoded_message = message.encode("utf-8")
        # Base64 encode the encoded bytes
        base64_bytes = base64.b64encode(encoded_message)
        # Decode the encoded bytes to a string (encrypted message)
        encrypted_message = base64_bytes.decode("utf-8")

        Label(screen_dois, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)

        text_dois = Text(screen_dois, font="Abpote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_dois.place(x=10, y=40, width=380, height=150)

        text_dois.insert(END, encrypted_message)
    elif password == "":
        messagebox.showerror("encryption", "input Password")
    elif password != "1234":
        messagebox.showerror("encryption","input Password")

def decrypt():
    password = code.get()
    if password == "1234":
        screen_dois = Toplevel(screen)
        screen_dois.geometry("400x200")
        screen_dois.config(bg="#ed3833")

        message = text_um.get(1.0, END)
        # Encode message as bytes using UTF-8 for wider character support
        base64_bytes = message.encode("utf-8")
        # Base64 decode the encoded bytes
        decoded_bytes = base64.b64decode(base64_bytes)
        # Decode the encoded bytes to a string (decrypted message)
        decrypted_message = decoded_bytes.decode("utf-8")

        Label(screen_dois, text="DECRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)

        text_dois = Text(screen_dois, font="Abpote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_dois.place(x=10, y=40, width=380, height=150)

        text_dois.insert(END, decrypted_message)
    elif password == "":
        messagebox.showerror("decryption", "input Password")
    elif password != "1234":
        messagebox.showerror("decryption","input Password")   


def main_screen():
    global screen, code, text_um

    screen = Tk()
    screen.geometry("375x398")
    screen.title("PcApp")

    def reset():
        code.set("")
        text_um.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)

    text_um = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text_um.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()
