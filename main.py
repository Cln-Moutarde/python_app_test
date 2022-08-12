from argparse import FileType
from ast import main
from ctypes import resize, sizeof
import tkinter
from tkinter import filedialog
from tkinter.messagebox import askquestion, showinfo
from turtle import fd
from typing_extensions import Self
from webbrowser import get
import qrcode
from pyzbar import *
from pyzbar.pyzbar import decode
import PIL.Image
from io import BytesIO
from tkinter import *
import re
import webbrowser

#configuration de webbrowser
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'



#creation de la fenetre
window = Tk()

#debut de la personnalisation de la fenetre
window.title("Ultimate QR Code RRRRReader")
window.geometry("480x320")
window.minsize(400, 300)
window.maxsize(600, 650)
window.iconbitmap("laptop.ico")
window.config(background='#ACC7CD')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


def show_frame(frame):
    frame.tkraise()

def valider():
    text = entry_text.get()
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=TRUE)
    img = qr.make_image()
    img.save("qrcode.png")
    showinfo("QR Code", "Le QR Code a ete cree dans le dossier racine")


def fichier():
    FileType = ('Image file', '*.png'), ('All files', '*.*')
    filename = filedialog.askopenfilename(title='Ouvrir un fichier',initialdir="/", filetypes=FileType)
    img1 = PIL.Image.open((filename))
    img2 = decode(img1)
    result = re.search("""data=b'(.+?)', type=""", str(img2)).group(1)
    MsgBox = askquestion("QR Code", ("voici le resultat:", result, "Voulez-vous copier le resultat dans le presse-papier?"))
    if MsgBox == "yes":
        window.clipboard_clear()
        window.clipboard_append(result)
        showinfo("QR Code", "Le resultat a ete copie dans le presse-papier")
    
    MsgBox2 = askquestion("QR Code", "Voulez-vous ouvrir le resultat dans un navigateur?")
    
    if MsgBox2 == "yes":
            webbrowser.get(chrome_path).open(result)
            showinfo("QR Code", "Le resultat a ete ouvert dans un navigateur")
    else: showinfo("QR Code", "A bientot")

    


#frame
frameMENU = Frame(window, bg='#ACC7CD')
frameMENU.grid_rowconfigure(0, weight=1)
frameMENU.grid_rowconfigure(1, weight=0)
frameMENU.grid_rowconfigure(2, weight=0)
frameMENU.grid_rowconfigure(3, weight=0)
frameMENU.grid_columnconfigure(0, weight=1, uniform="group1")  
frame2 = Frame(frameMENU, bg='#ACC7CD')
frame3 = Frame(frameMENU, bg='#ACC7CD')

frameCREER = Frame(window, bg='#ACC7CD')
frameCREER = Frame(window, bg='#ACC7CD')
frameCREER.grid_rowconfigure(0, weight=1)
frameCREER.grid_rowconfigure(1, weight=0)
frameCREER.grid_rowconfigure(2, weight=0)
frameCREER.grid_rowconfigure(3, weight=0)
frameCREER.grid_columnconfigure(0, weight=1, uniform="group1")
frame4 = Frame(frameCREER, bg='#ACC7CD')
frame5 = Frame(frameCREER, bg='#ACC7CD')

frameLIRE = Frame(window, bg='#ACC7CD')
frameLIRE.grid_rowconfigure(0, weight=1)
frameLIRE.grid_columnconfigure(0, weight=1)
frame6 = Frame(frameLIRE, bg='#ACC7CD')
frame7 = Frame(frameLIRE, bg='#ACC7CD')

for frame in (frameMENU, frameCREER, frameLIRE, frame2, frame3, frame4, frame5, frame6, frame7):
    frame.grid(row=0, column=0, sticky='news')

#===========================MENU===========================

#texte 1 (titre)
label_title = Label(frame2, text="Bienvenue sur Ultimate QR Code Reader", font=("Arial", 18), bg='#ACC7CD', fg='white')
label_title.grid(row=0, column=1, padx=5, pady=5)

#texte 2 (sous-titre)
label_subtitle = Label(frame2, text="Que voulez vous faire ?", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_subtitle.grid(row=1, column=1, padx=5, pady=5)


#bouton acueille creer qr code
dwnd1 = PhotoImage(file="creer qr.png")
button1 = Button(frame3, image=dwnd1, borderwidth=0, command=lambda:(show_frame(frameCREER), show_frame(frame4), show_frame(frame5)))
button1.grid(row=2, column=0, padx=10, pady=10)

#texte boutton creer qr code
label_titlebutton1 = Label(frame3, text="Creer un QR Code", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_titlebutton1.grid(row=3, column=0, pady=10)

#bouton lire qr code
dwnd2 = PhotoImage(file="lire qr.png")
button2 = Button(frame3, image=dwnd2, borderwidth=0, command=lambda:(show_frame(frameLIRE), show_frame(frame6), show_frame(frame7)))
button2.grid(row=2, column= 2, pady=10)

#texte boutton lire qr code
label_titlebutton2 = Label(frame3, text="Lire un QR Code", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_titlebutton2.grid(row=3, column=2, pady=10)




#===========================CREER===========================

#Titre 
label_titleCREER = Label(frame4, text="Creer un QR Code", font=("Arial", 18), bg='#ACC7CD', fg='white')
label_titleCREER.pack(pady=10)

#Sous titre
label_subtitleCREER = Label(frame4, text="Tapez le texte désiré puis validez", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_subtitleCREER.pack( padx=5, pady=5)

#Champ de saisie
entry_text = Entry(frame4, width=30, borderwidth=0, font=("Arial", 13))
entry_text.pack(padx=10, pady=30, side=BOTTOM)


#Bouton valider 
dwnd3 = Button(frame5, text="Valider", font=("Arial", 17), borderwidth=0, command= valider)
dwnd3.pack(padx=10, pady=10)


#bouton retour menu
button3 = Button(frame5, text="retour au menu", borderwidth=0, command=lambda:show_frame(frameMENU))
button3.pack(side=BOTTOM, padx=10, pady=10)





#===========================LIRE===========================

#Titre
label_titleLIRE = Label(frame6, text="Lire un QR Code", font=("Arial", 18), bg='#ACC7CD', fg='white')
label_titleLIRE.pack(pady=10)

#Sous titre
label_subtitleLIRE = Label(frame6, text="Selectionnez un fichier puis validez", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_subtitleLIRE.pack( padx=5, side=BOTTOM)


#Bouton choisir fichier
dwnd4 = Button(frame7, text="Choisir un fichier", font=("Arial", 17), borderwidth=0, command= fichier)
dwnd4.pack(padx=10, pady=70)

#bouton retour menu
button4 = Button(frame7, text="retour au menu", borderwidth=0, command=lambda:show_frame(frameMENU))
button4.pack(side=BOTTOM, padx=10, pady=10)








#afficher les frame
show_frame(frameMENU)
frame2.grid(row=0, column=0, sticky='news')
frame3.grid(row=1, column=0, sticky='news')
frame4.grid(row=0, column=0, sticky='news')
frame5.grid(row=1, column=0, sticky='news')
frame6.grid(row=0, column=0, sticky='news')
frame7.grid(row=1, column=0, sticky='news')


#afficher la fenetre 
window.mainloop()