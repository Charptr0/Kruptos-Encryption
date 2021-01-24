import tkinter as tk
from tkinter import Label, filedialog
from encryption import *
from constants import *

app = tk.Tk() #Start the app
app.title("Kruptos Encryption") #Title
app.config(bg= darkColor)
app.geometry("800x800") #Resolution
app.resizable(0,0) 

def openEncrypt(): #If the user clicked the "encrypted button"
    decryptButton.place_forget()
    creditsButton.place_forget()
    encryptButton.place_forget()
    
    chooseFileButton.place(relx=0.16, rely=0.3)
    chooseFileButton.config(text="Click here to choose a file to encrypt")

def askUserForFile():# this lets the user select a file and the user can chose a different file if needed. Also restricts filetypes to .txt and .json
    global fileName
    fileName = filedialog.askopenfilename(title="Select a file to encrypt", filetypes=((".txt files", "*.txt"), (".json files", "*.json")))
    if(fileName != ""):
        fileSelectedLabel.place(relx=0.27, rely=0.27)
        encryptConfirmationButton.place(relx=0.27, rely=0.5)
        chooseFileButton.config(text="Choose a different file")
        chooseFileButton.place(relx=0.27, rely=0.7)

def askUserForEncryptedtFile(): #User picks file to decrypt and the key. User can change the file if needed. File types are restricted to .txt and .json
    global encryptedFilePath
    encryptedFilePath = filedialog.askopenfilename(title="Select a file to decrypt", filetypes=((".txt files", "*.txt"), (".json files", "*.json")))
    if(encryptedFilePath != ""):
        fileSelectedLabel.place(relx=0.27, rely=0.2)
        chooseKeyButton.place(relx=0.25, rely=0.5)
        decryptChooseButton.config(text = "Select a new file", padx=112)
        decryptChooseButton.place(relx=0.25,rely=0.65)

def askUserForKey(): #this lets the user decrypt the selected file when you click the decryptButtonFinal
    global keyFilePath
    keyFilePath = filedialog.askopenfilename(title="Select the appropriate key", filetypes=((".key files", "*.key"), ("all files", "*")))
    if(keyFilePath != ""):
        keySelectedLabel.place(relx=0.3609, rely=0.36)
        decryptButtonFinal.place(relx=0.25, rely=0.8)


def actualDecrypting(): #this decrypts the file
    errMsg = decryptFile(encryptedFilePath, keyFilePath)
    if errMsg != "Error": #put the success label here
        keySelectedLabel.place_forget()
        fileSelectedLabel.place_forget()
        decryptButtonFinal.place_forget()
        unsuccessfullyDecryptedLabel.place_forget()
        successfullyDecryptedLabel.place(relx=0.1,rely=0.15)
        reEncryptButton.place(relx=0.25,rely=0.8)

        
    else: #put the unsuccess label here
        unsuccessfullyDecryptedLabel.place(relx=0.096,rely=0.1)
        keySelectedLabel.place_forget()
        fileSelectedLabel.place_forget()
        decryptButtonFinal.place_forget()

def reEncrypt():
    reEncryptTheFile()
    mainMenuButton.place(relx=0.38, rely=0.5)
    successfullyReEncryptLabel.place(relx=0.06,rely=0.17)
    successfullyDecryptedLabel.place_forget()
    chooseKeyButton.place_forget()
    decryptChooseButton.place_forget()
    reEncryptButton.place_forget()
    

def encryptFile(): #If the encrypt button has been pressed
    global fileName
    keyName = generateNewKey(fileName)
    keyLabel.config(text="Please do not delete your key!\nYour key is saved in " + keyName)
    keyLabel.place(relx=0.1, rely=0.8)
    chooseFileButton.place_forget()
    fileSelectedLabel.place_forget()
    encryptConfirmationButton.place_forget()
    fileEncryptMessage.place(relx=0.14, rely=0.27)
    mainMenuButton.place(relx=0.38, rely=0.5)
   
def decryptFileMenu():
    encryptButton.place_forget()
    creditsButton.place_forget()
    decryptButton.place_forget()
    decryptChooseButton.place(relx=0.25, rely=0.2)

 
def returnToMainMenu(): #Return back to menu
    names.place_forget()
    successfullyReEncryptLabel.place_forget()
    fileEncryptMessage.place_forget()
    mainMenuButton.place_forget()
    keyLabel.place_forget()
    encryptButton.place(relx=0.34, rely=0.3)
    decryptButton.place(relx=0.34, rely=0.5)
    creditsButton.place(relx = 0.4, rely=0.8)

def contributions():
    encryptButton.place_forget()
    decryptButton.place_forget()
    creditsButton.place_forget()
    names.place(relx=0.25, rely=0.3)
    mainMenuButton.place(relx=0.4, rely=0.8)

title = tk.Label(text="Kruptos Encryption", bg=darkColor, fg= whiteTextColor, font=(fontName, 20, "bold")) #Create the title
title.place(relx=0.337, rely=0)

encryptButton = tk.Button(text="Encrypt a file", padx=50, pady=10, font=(fontName, 20), bg = buttonsColor, fg = whiteTextColor, command=openEncrypt)
encryptButton.place(relx=0.34, rely=0.3)

decryptButton = tk.Button(text = "Decrypt a file", padx=50, pady=10, font =(fontName, 20), bg = buttonsColor, fg = whiteTextColor, command=decryptFileMenu)
decryptButton.place(relx=0.34, rely=0.5)

creditsButton = tk.Button(text = "Credits", padx=30, pady=10, font=(fontName, 20 ), bg = darkColor, fg = whiteTextColor, command=contributions)
creditsButton.place(relx = 0.4, rely=0.8)

chooseFileButton = tk.Button(text="Click here to choose a file to encrypt", padx=60, pady=10, font=(fontName, 20), command=askUserForFile)

encryptConfirmationButton = tk.Button(text="Encrypt the selected file", padx=50, pady=10, font=(fontName, 20), command=encryptFile)

mainMenuButton = tk.Button(text="Main Menu", padx=20, pady=10, font=(fontName, 20), command=returnToMainMenu)

fileEncryptMessage = tk.Label(text="File successfully encrypted", font=(fontName, 30), padx=80, pady=10, bg = darkColor, fg = fileSelectedColor)
fileSelectedLabel = tk.Label(text="File selected", font=(fontName, 30), padx=80, pady=10, bg = darkColor, fg = fileSelectedColor)

keyLabel = tk.Label(text="",font=(fontName, 20), padx=80, pady=10, bg = darkColor, fg = keyNameColor)

chooseKeyButton = tk.Button(text="Choose a appropriate key",padx=60, pady=10, font=(fontName, 20), command=askUserForKey)

decryptChooseButton = tk.Button(text="Choose a file to decrypt", padx=58, pady=10, font=(fontName, 20), command=askUserForEncryptedtFile)

decryptButtonFinal = tk.Button(text="Decrypt", padx=160, pady=10, font=(fontName, 20), bg="green", command=actualDecrypting)

keySelectedLabel = tk.Label(text="Key selected",font=(fontName, 30), bg = darkColor, fg = fileSelectedColor)

successfullyDecryptedLabel = tk.Label(text="The file has been successfully decrypted", font=(fontName, 30), bg=darkColor, fg="green")
unsuccessfullyDecryptedLabel = tk.Label(text="Something went wrong, wrong key or file", font=(fontName, 30), bg=darkColor, fg="red")

reEncryptButton = tk.Button(text="Re-encrypt", font=(fontName, 30), bg="green", command=reEncrypt, padx=113)

successfullyReEncryptLabel = tk.Label(text="The file has been successfully re-encrypted", font=(fontName, 30), bg=darkColor, fg="green")

names = tk.Label(text="Made by\nChenhao Li\nRiaz Ahmed\nYeiry Chaverra\nRamon Camilo\n\nCUNY Hackathon 2021 ", font=(fontName, 30), bg=darkColor, fg=whiteTextColor)

app.mainloop() #Start the app





