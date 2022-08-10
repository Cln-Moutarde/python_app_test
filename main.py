from ctypes import resize, sizeof
from webbrowser import get
import qrcode
import pyzbar
from tkinter import *

#creation de la fenetre
window = Tk()

#debut de la personnalisation de la fenetre
window.title("Ultimate QR Code RRRRReader")
window.geometry("500x500")
window.minsize(400, 360)
window.maxsize(600, 600)
window.iconbitmap("laptop.ico")
window.config(background='#ACC7CD')

#frame
frame1 = Frame(window, bg='#ACC7CD')
frame2 = Frame(window, bg='#ACC7CD')

#texte 1 (titre)
label_title = Label(frame1, text="Bienvenue sur Ultimate QR Code Reader", font=("Arial", 18), bg='#ACC7CD', fg='white')
label_title.pack()

#texte 2 (sous-titre)
label_subtitle = Label(frame1, text="Que voulez vous faire ?", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_subtitle.pack()


#bouton1
dwnd1 = PhotoImage(file="creer qr.png")
button1 = Button(frame2, image=dwnd1, borderwidth=0)
button1.grid(row=2, column=1, padx=5, pady=10)

#texte boutton 1
label_titlebutton1 = Label(frame2, text="Creer un QR Code", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_titlebutton1.grid(row=3, column=1, padx=5, pady=10)

#bouton2
dwnd2 = PhotoImage(file="lire qr.png")
button2 = Button(frame2, image=dwnd2, borderwidth=0)
button2.grid(row=2, column= 5, padx=5, pady=10)

#etxte boutton 2
label_titlebutton2 = Label(frame2, text="Lire un QR Code", font=("Arial", 13), bg='#ACC7CD', fg='white')
label_titlebutton2.grid(row=3, column=5, padx=5, pady=10)


#afficher les frame
frame1.pack(expand=YES)
frame2.pack(expand=YES)

#afficher la fenetre 
window.mainloop()