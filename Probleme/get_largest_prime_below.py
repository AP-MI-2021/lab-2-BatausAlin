import tkinter


def prim(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for _ in range(3, n // 2, 2):
        if n % _ == 0:
            return False

    return True


def get_largest_prime_below(n):
    if n < 2:
        return 0
    while n > 1:
        if not prim(n):
            n -= 1
        else:
            return n
    pass

def test_get_largest_prime_below():
    #Functie de test cand incepem problema1 o sa vedem daca este bine sau nu
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(25) == 23
    assert get_largest_prime_below(100) == 97


def Problema_1():
    def obtine_rezultatul():
        afisare_rezultat.delete(0, 'end')
        rezultat = get_largest_prime_below(int(entry_n.get()))
        afisare_rezultat.insert(0, f'Numar prim mai mic sau egal: {rezultat}')

    problema_1 = tkinter.Tk()
    problema_1.geometry('430x200')
    problema_1.resizable(False, False)
    problema_1.title('Problema 1')
    test_get_largest_prime_below()

    label_info_problema = tkinter.Label(problema_1, text='1. Găsește ultimul număr prim mai mic decât un număr dat.').place(x=2, y=5)

    label = tkinter.Label(problema_1, text='Introduceti valoare lui n:').place(x=2, y=25)

    entry_n = tkinter.Entry(problema_1)
    entry_n.place(x=5, y=45)

    button1 = tkinter.Button(problema_1, text='Rezolva', command=obtine_rezultatul).place(x=5, y=75)

    afisare_rezultat = tkinter.Entry(problema_1, width=38, font=('Arial', 14))
    afisare_rezultat.place(x=5, y=175)


    problema_1.mainloop()

