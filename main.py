from ast import main
from ctypes import resize, sizeof
from typing_extensions import Self
from webbrowser import get
import qrcode
import pyzbar
from tkinter import *

#creation de la fenetre
window = Tk()

#debut de la personnalisation de la fenetre
window.title("Ultimate QR Code RRRRReader")
window.geometry("500x500")
window.minsize(400, 400)
window.maxsize(1920, 1080)
window.iconbitmap("laptop.ico")
window.config(background='#ACC7CD')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


def show_frame(frame):
    frame.tkraise()


#frame
frameMENU = Frame(window, bg='#ACC7CD')
frameMENU.grid_rowconfigure(0, weight=1)
frameMENU.grid_columnconfigure(0, weight=1)
frame2 = Frame(frameMENU, bg='#ACC7CD')
frame3 = Frame(frameMENU, bg='#ACC7CD')

frameCREER = Frame(window, bg='#ACC7CD')
frameCREER.grid_rowconfigure(0, weight=1)
frameCREER.grid_columnconfigure(0, weight=1)
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
label_title.grid(row=0, column=1, padx=5,) 

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
label_titleCREER.grid(row=0, column=1, padx=5,)

#Sous titre
label_subtitleCREER = Label(frame4, text="Tapez le texte désiré puis validez", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_subtitleCREER.grid(row=1, column=1, padx=5, pady=5)






#bouton retour menu
button3 = Button(frame5, text="retour au menu", borderwidth=0, command=lambda:show_frame(frameMENU))
button3.grid(row=2, column= 2, pady=10)





#===========================LIRE===========================

#Titre
label_titleLIRE = Label(frame6, text="Lire un QR Code", font=("Arial", 18), bg='#ACC7CD', fg='white')
label_titleLIRE.grid(row=0, column=1, padx=5,)

#Sous titre
label_subtitleLIRE = Label(frame6, text="Selectionnez un fichier puis validez", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_subtitleLIRE.grid(row=1, column=1, padx=5, pady=5)


#bouton retour menu
button4 = Button(frame7, text="retour au menu", borderwidth=0, command=lambda:show_frame(frameMENU))
button4.grid(row=2, column= 2, pady=10)








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