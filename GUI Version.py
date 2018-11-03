import Tkinter as tk
import tkMessageBox as tkm
import base64
import sys
import os
from string import maketrans

#This is a small python application made by Pareekshith US Katti, 5th Sem, MIT Mysore
#Here are some details about the imported packages :
#Tkinker is a GUI development framework for python
#tkMessageBox is part of TKinter framework used to create dailog Boxes
#base64 is an encoding library. It is used in the program to encode all types of files to text files
#sys and os are used to read custom file paths from the user
#maketrans is used to define the translation for the Encryption and Decryption algorithms

#----------------------------Code------------------------------
#Encryption Algorithm : ABCD...Z to QWERTY...M
encstr = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
   'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')

#Decryption Algorithm : QWERTY...M to ABCD...Z
decstr = maketrans('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm',
   'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

#Encryption Function
def encrypt(text):
   return text.translate(encstr)

#Decryption Function
def decrypt(text):
   return text.translate(decstr)

def fileencrypt () :
        # Encryption is done by converting file to Text
        user_input = v.get()
        #Any file to Text file
        with open(user_input, "rb") as inFile:
            st = base64.b64encode(inFile.read())

        #String st is Encrypted using the Algorithm
        st=encrypt(st)
        #Encrypted string st is converted back to original file format
        user_output = v1.get()
        fh = open(user_output, "wb")
        fh.write(st.decode('base64'))
        fh.close()
        #The showinfo method (function) shows dialog box (info box)
        inf=tkm.showinfo('Success', 'File Encrypted')

def filedecrypt () :
        #Encrypted File is converted back to text.
        user_input = v2.get()
        with open(user_input, "rb") as inFile:
            st = base64.b64encode(inFile.read())
        #String st has contents of converted encrypted File

        #st is decrypted using the algorithm
        st=decrypt(st)
        user_output = v3.get()
        #The decrypted text file is converted back to original file format to get the original file
        fh = open(user_output, "wb")
        fh.write(st.decode('base64'))
        fh.close()
        #The infobox below shows a dialog saying that the file has been decrypted
        inf=tkm.showinfo('Success', 'File Decrypted')

#GUI Code
#Creating an object Root to access Tkinter functions
root=tk.Tk()
#String variables are created to be associated with Text Boxes
v=tk.StringVar()
v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()

#Main Heading
l1=tk.Label(root,text="File Encryptor and Decryptor",font="Verdana 20 bold",bg="Ghostwhite",fg="navy").pack(fill="x",pady=5)

#Label to Indicate that an input path must be taken for Encrption
l1=tk.Label(root,text="Enter File path with extension for Encryption",font="Verdana 10 bold").pack(fill="x",pady=5)

#Entry box to enter input path
e1=tk.Entry(root,textvariable=v).pack(fill="x",pady=5)

#Label to indicate that an output path must be taken to store Encrypted file
l1=tk.Label(root,text="Enter File path to store output",font="Verdana 10 bold").pack(fill="x",pady=5)

#Entry box to enter output path
e1=tk.Entry(root,textvariable=v1).pack(fill="x",pady=5)

#Button which triggers the file encryption process
rad1=tk.Button(root,text="Encrypt",padx=20,command=fileencrypt,bg="AntiqueWhite3").pack(fill="x",pady=5)

#Label to indicate that an input path must be entered for decryption
l1=tk.Label(root,text="Enter File path with extension for Decryption",font="Verdana 10 bold").pack(fill="x",pady=5)

#Entry box to enter input path
e1=tk.Entry(root,textvariable=v2).pack(fill="x",pady=5)

#Label to indicate that an output path must be taken to store Decrypted file
l1=tk.Label(root,text="Enter File path to store output",font="Verdana 10 bold").pack(fill="x",pady=5)

#Entry box to enter output path
e1=tk.Entry(root,textvariable=v3).pack(fill="x",pady=5)

#Button which triggers the file decryption process
rad2=tk.Button(root,text="Decrypt",padx=20,command=filedecrypt,bg="AntiqueWhite3").pack(fill="x",pady=5)

#This function is required to start te gui and keep it in an infinite loop state until it is closed
root.mainloop()
