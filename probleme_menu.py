import tkinter
from Probleme.get_largest_prime_below import Problema_1
from Probleme.get_age_in_days import Problema_2
from Probleme.get_goldbach import Problema_3


def probleme_calculator():
    probleme_rezolvare = tkinter.Tk()
    probleme_rezolvare.title('Problemele')
    probleme_rezolvare.resizable(False, False)
    probleme_rezolvare.geometry('400x200')

    problema_1 = tkinter.Button(probleme_rezolvare, text='Problema 1', command=Problema_1).place(x=5, y=5)
    problema_2 = tkinter.Button(probleme_rezolvare, text='Problema 2', command=Problema_2).place(x=79, y=5)
    problema_3 = tkinter.Button(probleme_rezolvare, text='Problema 3', command=Problema_3).place(x=153, y=5)
    probleme_rezolvare.mainloop()
