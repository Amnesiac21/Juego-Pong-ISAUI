from pygame import mixer
from tkinter import *
from tkinter import messagebox
from subprocess import call

menu = Tk()
menu.geometry("800x600")
menu.title("Menu Pong")
menu.config(bg="black")
menu.resizable(0, 0)
img_titulo = PhotoImage(
    file=r'C:\Users\Business\Desktop\Python2022\Tkinter\PongEnTurtle\logo200.png')
img_stop = PhotoImage(
    file=r'C:\Users\Business\Desktop\Python2022\Tkinter\PongEnTurtle\pause.png')
img_continue = PhotoImage(
    file=r'C:\Users\Business\Desktop\Python2022\Tkinter\PongEnTurtle\continue.png')
music = r'C:\Users\Business\Desktop\Python2022\Tkinter\PongEnTurtle\MenuMusic.mp3'
exec = r'C:\Users\Business\Desktop\Python2022\Tkinter\PongEnTurtle\Pong.py'

mixer.init()
mixer.music.load(music)
mixer.music.play(-1)


def jugar():  # funcion para ejecutar el script "Pong.py"
    call(['python', exec])


def reanudar():
    mixer.music.unpause()


def pausar():
    mixer.music.pause()


def salir():
    resultado = messagebox.askquestion(
        "Salir", "¿Seguro que quieres salir?")
    if resultado != "no":
        messagebox.showinfo(
            message="¡Hasta luego, buena suerte!", title="Adios!")
        menu.destroy()


lbl_separador1 = Label(menu, text="soy un label separador",
                       bg="black", fg="black")
lbl_separador1.grid(row=0, column=0, ipadx=50, ipady=30)

titulo = Label(menu, image=img_titulo)
titulo.grid(row=0, column=1, sticky=W)

lbl_separador2 = Label(menu, text="soy un label separador",
                       bg="black", fg="black")
lbl_separador2.grid(row=1, column=0, ipadx=50, ipady=30)

btn_jugar = Button(menu, text="Jugar", font=(
    "Burko Bold", 16), bg="black", fg="white", relief=SUNKEN, command=jugar)  # command=jugar
btn_jugar.grid(row=2, column=1,
               padx=10, pady=10, ipadx=10, ipady=10)

lbl_separador3 = Label(menu, text="soy un label separador",
                       bg="black", fg="black")
lbl_separador3.grid(row=3, column=0, ipadx=50, ipady=30)

btn_salir = Button(menu, text="Salir", font=(
    "Burko Bold", 16), bg="black", fg="white", relief=SUNKEN, command=salir)
btn_salir.grid(row=3, column=1,
               padx=10, pady=10, ipadx=10, ipady=10)

btn_stopSound = Button(menu, image=img_stop, command=pausar)
btn_stopSound.grid(row=4, column=0, padx=2, pady=100,
                   ipadx=3, ipady=3, sticky="SW")

btn_continueSound = Button(menu, image=img_continue, command=reanudar)
btn_continueSound.grid(row=4, column=0, padx=2, pady=100,
                       ipadx=3, ipady=3, sticky="S")


menu.mainloop()
