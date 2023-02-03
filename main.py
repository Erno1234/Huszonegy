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

def jatekosNagyobb_H_egy_Teszt():
    jatekosLista = [6, 5, 7, 8]
    gepLista = [6, 5, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: Pont nagyobb mint 21)")
    else:
        print("A teszt megbukott. (Játekos teszt: Pont nagyobb mint 21)")

def jatekosKevesebbP_Teszt():
    jatekosKev = [4, 5, 6, 3]
    gepKev = [5, 5, 5, 5]
    kapottEredmeny = eredmeny(jatekosKev, gepKev)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játékos teszt: Kevesebb pont)")
    else:
        print("A teszt megbukott. (Játékos teszt: Kevesebb pont)")
def jatekosEgyenloP_TobbL_Teszt():
    jatekosKev = [4, 5, 6, 3, 2]
    gepKev = [5, 5, 5, 5]
    kapottEredmeny = eredmeny(jatekosKev, gepKev)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játékos teszt: Egyenlő pontok több lap)")
    else:
        print("A teszt megbukott. (Játékos teszt: Egyenlő pontok több lap)")
def gepNagyobb_H_egy_Teszt():
    jatekosKev = [4, 5, 6, 8]
    gepKev = [5, 5, 5, 3]
    kapottEredmeny = eredmeny(jatekosKev, gepKev)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Gép teszt: Pont nagyobb mint 21)")
    else:
        print("A teszt megbukott. (Gép teszt: Pont kevesebb mint 21)")
def gepKevesebbP_Teszt():
    jatekosKev = [4, 5, 6, 3]
    gepKev = [5, 5, 5]
    kapottEredmeny = eredmeny(jatekosKev, gepKev)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Gép teszt: Kevesebb pont)")
    else:
        print("A teszt megbukott. (Gép teszt: Kevesebb pont)")
def gepEgyenloP_TobbL_Teszt():
    jatekosKev = [4, 5, 6, 3]
    gepKev = [5, 5, 8]
    kapottEredmeny = eredmeny(jatekosKev, gepKev)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Gép teszt: Egyenlő pontok több lap)")
    else:
        print("A teszt megbukott. (Gép teszt: Egyenlő pontok több lap)")
def dontetlen_Teszt():
    jatekosLista = [4, 5, 6, 3]
    gepLista = [5, 5, 5, 3]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Döntetlen"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Döntetlen teszt)")
    else:
        print("A teszt megbukott. (Döntetlen teszt)")
def tesztek():
    jatekosNagyobb_H_egy_Teszt()
    jatekosKevesebbP_Teszt()
    jatekosEgyenloP_TobbL_Teszt()
    gepNagyobb_H_egy_Teszt()
    gepKevesebbP_Teszt()
    gepEgyenloP_TobbL_Teszt()
    dontetlen_Teszt()


tesztek()