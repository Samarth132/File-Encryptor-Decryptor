import base64
import sys
import os
from string import maketrans

#This is a small python application made by Pareekshith US Katti, 5th Sem, MIT Mysore
#Here are some details about the imported packages :
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
        user_input = raw_input("Enter the file to be Encrypted with extension : ")
        #Any file to Text file
        with open(user_input, "rb") as inFile:
            st = base64.b64encode(inFile.read())

        #String st is Encrypted using the Algorithm
        st=encrypt(st)
        #Encrypted string st is converted back to original file format
        user_output = raw_input("Enter the filename with extension to store the output : ")
        fh = open(user_output, "wb")
        fh.write(st.decode('base64'))
        fh.close()
        print "File Encrypted! \n"

def filedecrypt () :
        #Encrypted File is converted back to text.
        user_input = raw_input("Enter the file to be Decrypted with extension : ")
        with open(user_input, "rb") as inFile:
            st = base64.b64encode(inFile.read())
        #String st has contents of converted encrypted File

        #st is decrypted using the algorithm
        st=decrypt(st)
        user_output = user_output = raw_input("Enter the filename with extension to store the output : ")
        #The decrypted text file is converted back to original file format to get the original file
        fh = open(user_output, "wb")
        fh.write(st.decode('base64'))
        fh.close()
        print "File Decrypted! \n"

print "File Encryptor Decryptor"
print "By Pareekshith US Katti, 5th Sem, MIT Mysore"
flag=0
while (flag==0):
    op=input("Enter \n 1.Encrypt \n 2.Decrypt \n 3.Quit \n")
    if (op==1):
        fileencrypt()
    if (op==2):
        filedecrypt()
    if (op==3):
        flag=1
    else :
        print ""
