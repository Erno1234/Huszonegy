#Megoldás
def eredmeny(jatekosLapok: [int], gepLapok: [int]):
    szoveg = ""
    jatekosPont = pontszamitas(jatekosLapok)
    gepPont = pontszamitas(gepLapok)

    if jatekosPont > 21:
        szoveg = "Játékos vesztett"
    elif gepPont > 21:
        szoveg = "Gép vesztett"
    return szoveg
def pontszamitas(lapok: [int]):
    pontok = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok

#Tesztesetek

def jatekosVesztettTeszt():
    jatekosLista = [6, 5, 7, 8]
    gepLista = [6, 5, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.")
    else:
        print("A teszt megbukott.")
def tesztek():
    jatekosVesztettTeszt()


tesztek()