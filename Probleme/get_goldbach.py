from Probleme.get_largest_prime_below import prim
import tkinter


def Problema_3():
    Problema3 = tkinter.Tk()
    Problema3.title('Problema 3')
    Problema3.geometry('700x200')
    Problema3.resizable(False, False)

    def test_get_goldbach():
        '''
        Nu am putut face functia de test intrucat eu direct din functie fac afisarea si nu returnez cele 2 variabile, am o idee despre cum sa o fac
        dar am deja cele 2 problema aceasta este optionala
        :return:
        '''
        pass

    def get_goldbach(n):
        gasite = False
        primul_numar = 2
        al_doilea_numar = 0
        while not gasite and primul_numar <= n - primul_numar:
            if prim(primul_numar) and prim(n - primul_numar):
                al_doilea_numar = n - primul_numar
                gasite = True
            else:
                primul_numar += 1

        if primul_numar > al_doilea_numar:
            primul_numar, al_doilea_numar = al_doilea_numar, primul_numar

        if primul_numar + al_doilea_numar is not n:
            primul_numar_afisat.insert(0, f'Nu exista!')
            al_doilea_numar_afisat.insert(0, f'Nu exista!')
        else:
            primul_numar_afisat.insert(0, f'{primul_numar}')
            al_doilea_numar_afisat.insert(0, f'{al_doilea_numar}')



        pass

    def rezultat_calcul():
        primul_numar_afisat.delete(0, 'end')
        al_doilea_numar_afisat.delete(0, 'end')

        get_goldbach(int(numarul_natural_n.get()))

        test_get_goldbach()


    # Label
    info_problema = tkinter.Label(Problema3, text='Dându-se numărul natural `n`, determină numerele prime `p1` si `p2` astfel încât `n = p1 + p2` (verificarea conjecturii lui Goldbach) \n`p1` minim și `p2` maxim. Pentru ce fel de `n` există soluție?')
    info_problema.place(x=5, y=5)
    info_numarul_natural_n = tkinter.Label(Problema3, text='Introduceți valoarea lui n:').place(x=5, y=65)
    info_primul_numar = tkinter.Label(Problema3, text='Primul numar este: ').place(x=5, y=110)
    info_al_doilea_numar = tkinter.Label(Problema3, text='Al doilea numar este: ').place(x=5, y=130)
    # Entry
    numarul_natural_n = tkinter.Entry(Problema3)
    numarul_natural_n.place(x=150, y=65)

    # Afisare rezultat
    primul_numar_afisat = tkinter.Entry(Problema3)
    primul_numar_afisat.place(x=150, y=110)
    al_doilea_numar_afisat = tkinter.Entry(Problema3)
    al_doilea_numar_afisat.place(x=150, y=130)

    # Button
    button_subbmit = tkinter.Button(Problema3, text='Calculează', command=rezultat_calcul).place(x=5, y=170)

    Problema3.mainloop()
