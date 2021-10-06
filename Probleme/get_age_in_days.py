import tkinter
import datetime

# 2.Se dă data nașterii în formatul DD/MM/YYYY. Determinați vârsta persoanei în zile.

def get_age_in_days(DD, MM, YYYY):
    timpul_acum = datetime.datetime.now()

    data_introdusa = datetime.date(YYYY, MM, DD)
    data_de_azi = datetime.date(timpul_acum.year, timpul_acum.month, timpul_acum.day)
    data_finala = data_de_azi - data_introdusa
    return data_finala.days
    pass

def Problema_2():
    def test_get_age_in_days():
        # Am calculat de aici: https://www.topster.ro/calendar/tagerechner.php
        assert get_age_in_days(17, 5, 2002) == 7082
        assert  get_age_in_days(16, 6, 2002) == 7052
        assert  get_age_in_days(8, 12, 1990) == 11260

    test_get_age_in_days()

    def Obtine_rezultatul():
        afisare_rezultat.delete(0, 'end')
        DD = int(entry_DD.get())
        MM = int(entry_MM.get())
        YYYY = int(entry_YYYY.get())

        afisare_rezultat.insert(0, f'Număr total zile: {get_age_in_days(DD,MM,YYYY)}')
        pass



    Problema2 = tkinter.Tk()
    Problema2.title("Problema 2")
    Problema2.geometry('400x200')
    Problema2.resizable(False, False)

    label_info_problema = tkinter.Label(Problema2, text='Se dă data nașterii în formatul `DD/MM/YYYY`. Determinați vârsta \npersoanei în zile.').place(x=5, y=5)

    #Label
    label_DD = tkinter.Label(Problema2, text='Introduceți ziua nașterii:')
    label_DD.place(x=5, y=65)
    label_MM = tkinter.Label(Problema2, text='Introduceți luna nașterii:')
    label_MM.place(x=5, y=85)
    label_YYYY = tkinter.Label(Problema2, text='Introduceți anul nașterii:')
    label_YYYY.place(x=5, y=105)


    # Entry
    entry_DD = tkinter.Entry(Problema2)
    entry_DD.place(x=140, y=65)
    entry_MM = tkinter.Entry(Problema2)
    entry_MM.place(x=140, y=85)
    entry_YYYY = tkinter.Entry(Problema2)
    entry_YYYY.place(x=140, y=105)

    #Locul unde se afișează rezultatul
    afisare_rezultat = tkinter.Entry(Problema2)
    afisare_rezultat.place(x=5, y=170)

    button_subbmit = tkinter.Button(Problema2, text= 'Calculează', command= Obtine_rezultatul).place(x=330, y=170)
    Problema2.mainloop()



