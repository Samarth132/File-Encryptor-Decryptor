import base64
import tkinter as tk
import sys
import os
import tkinter.messagebox as tkm
import json

en = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','MNBVCXZLKJHGFDSAPOIUYTREWQmnbvcxzlkjhgfdsapoiuytrewq')
dc = str.maketrans('MNBVCXZLKJHGFDSAPOIUYTREWQmnbvcxzlkjhgfdsapoiuytrewq','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

def encrypt(text):
    return text.decode().translate(en)

def decrypt(text):
    return text.decode().translate(dc)

def file_encryptor():
    u_in = sv1.get()
    with open(u_in,'rb') as fh_r:
        t_file = base64.b64encode(fh_r.read())
    t_file = encrypt(t_file).encode()
    u_out = sv2.get()
    fh_w = open(u_out,'wb')
    fh_w.write(base64.b64decode(t_file))
    fh_w.close()
    ds_msg = tkm.showinfo('File encrypted')

def file_decryptor():
    u_in = sv3.get()
    with open(u_in,'rb') as fh_r:
        t_file = base64.b64encode(fh_r.read())
    t_file = decrypt(t_file).encode()
    u_out = sv4.get()
    fh_w = open(u_out,'wb')
    fh_w.write(base64.b64decode(t_file))
    fh_w.close()
    ds_msg = tkm.showinfo('File decrypted')

# Gui
window = tk.Tk()

sv1 = tk.StringVar()
sv2 = tk.StringVar()
sv3 = tk.StringVar()
sv4 = tk.StringVar()

dt1 = tk.Label(window,text = 'Filecryptor',bg = 'black',fg = 'grey50',width = 10,height = 12,font = 'Helvetica 10 bold').pack(fill = 'x',pady = 5)

dt1 = tk.Label(window,text = 'Enter file path for encryption with extention',font = 'Helvetica 10').pack(fill = 'x',pady = 5)
ents = tk.Entry(window,textvariable = sv1,font = 'Helvetica 20').pack(fill="x",pady=5)

dt1 = tk.Label(window,text = 'Enter file path to store output',font = 'Helvetica 10').pack(fill = 'x',pady = 5)
ents = tk.Entry(window,textvariable = sv2,font = 'Helvetica 20').pack(fill="x",pady=5)

button_1 = tk.Button(window,text = 'encrypt',padx = 20,bg = 'grey50',fg = 'black',command = file_encryptor).pack(fill = 'x',pady = 5)

dt1 = tk.Label(window,text = 'Enter file path for decryption with extention',font = 'Helvetica 10').pack(fill = 'x',pady = 5)
ents = tk.Entry(window,textvariable = sv3,font = 'Helvetica 20').pack(fill="x",pady=5)

dt1 = tk.Label(window,text = 'Enter file path to store output',font = 'Helvetica 10').pack(fill = 'x',pady = 5)
ents = tk.Entry(window,textvariable = sv4,font = 'Helvetica 20').pack(fill="x",pady=5)

button_1 = tk.Button(window,text = 'decrypt',padx = 20,bg = 'grey50',fg = 'black',command = file_decryptor).pack(fill = 'x',pady = 5)

window.mainloop()
