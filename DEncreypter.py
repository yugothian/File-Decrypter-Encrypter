from tkinter import Tk
from cryptography.fernet import Fernet
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Choose Process')


def encryption():
    global key
    key = Fernet.generate_key()

    with open('key.key', 'wb') as filekey:
        filekey.write(key)

    with open('key.key', 'rb') as filekey:
        key = filekey.read()


    Tk().withdraw()
    filename = askopenfilename()

    with open(filename, "rb") as thefile:
        contents = thefile.read()

    contents_encrypted = Fernet(key).encrypt(contents)

    with open(filename, "wb") as thefile:
        thefile.write(contents_encrypted)





def decryption():
    Tk().withdraw()
    filename = askopenfilename()

    global key
    with open('key.key', 'rb') as filekey:
        key = filekey.read()
        
    with open(filename, "rb") as thefile:
        contents = thefile.read()

    contents_decrypted = Fernet(key).decrypt(contents)
        
    with open(filename, "wb") as thefile:
        thefile.write(contents_decrypted)


enc_button = ttk.Button(
    root,
    text='Encryption',
    command=encryption
)

enc_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


dec_button = ttk.Button(
    root,
    text='Decryption',
    command=decryption
)

dec_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()