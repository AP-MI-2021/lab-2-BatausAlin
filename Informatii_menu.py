import tkinter


def informatii_menu():
    info_menu = tkinter.Tk()
    info_menu.geometry('1100x200')
    info_menu.title('Informatii')
    info_menu.resizable(False, False)

    label_problema_1 = tkinter.Label(info_menu, text='1. Găsește ultimul număr prim mai mic decât un număr dat.\n\n').place(x=5, y=5)
    label_problema_2 = tkinter.Label(info_menu, text='2. Se dă data nașterii în formatul `DD/MM/YYYY`. Determinați vârsta persoanei în zile.\n\n').place(x=5, y=25)
    label_problema_3 = tkinter.Label(info_menu, text='3. Dându-se numărul natural `n`, determină numerele prime `p1` si `p2` astfel încât `n = p1 + p2` (verificarea conjecturii lui Goldbach), `p1` minim și `p2` maxim. Pentru ce fel de `n` există soluție?\n\n').place(x=5, y=45)
    # label_problema_4 = tkinter.Label(info_menu, text='4. Execută un număr dat de pași pentru a calcula radicalul unui număr dat folosind metoda lui Newton cu `x0=2` și afișează aproximarea obținută.\n\n').place(x=5, y=65)


    info_menu.mainloop()
