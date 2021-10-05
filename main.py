from Informatii_menu import informatii_menu
from probleme_menu import probleme_calculator

import tkinter

fereastra_principala = tkinter.Tk()
fereastra_principala.geometry('500x100')
fereastra_principala.title('Bățăuș Alin-Alexandru')
fereastra_principala.resizable(False, False)

# Icon
fereastra_principala.iconphoto(False, tkinter.PhotoImage(file='icon/console_48px.png'))

Universitate = tkinter.Label(fereastra_principala, text='Universitatea Babes-Bolyai').place(x=5, y=5)
Facultate = tkinter.Label(fereastra_principala, text='Facultatea de Matematică și Informatică').place(x=5, y=25)
# Autor = tkinter.Label(fereastra_principala, text='Bățăuș Alin-Alexandru').place(x=5, y=45)

informatii_button = tkinter.Button(fereastra_principala, text='Informații probleme', command=informatii_menu).place(x=378, y=70)
probleme_button = tkinter.Button(fereastra_principala, text='Problemele', command=probleme_calculator).place(x=5, y=70)

fereastra_principala.mainloop()
