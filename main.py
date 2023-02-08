#Megoldás
def eredmeny(jatekosLapok: [int], gepLapok: [int], jatekosLapszamok: [int], gepLapszamok: [int]):
    szoveg = ""
    jatekosPont = pontszamitas(jatekosLapok)
    gepPont = pontszamitas(gepLapok)
    jLapszam = lapszamlalas(jatekosLapszamok)
    gepLapszam = lapszamlalas(gepLapszamok)
    if gepPont > 21 and jatekosPont > 21:
        szoveg = "Döntetlen, a ház nyert"
    elif jatekosPont > 21:
        szoveg = "Játékos vesztett"
    elif gepPont > 21:
        szoveg = "Gép vesztett"
    elif jatekosPont > gepPont:
        szoveg = "Gép vesztett"
    elif gepPont > jatekosPont:
        szoveg = "Játékos vesztett"
    elif gepLapszam > jLapszam:
        szoveg = "Gép vesztett"
    elif gepLapszam < jLapszam:
        szoveg = "Játékos vesztett"
    elif gepLapszam == jLapszam:
        szoveg = "Döntetlen, osztoztok a nyereségen"

    else:
        szoveg = "Döntetlen"
    return szoveg
def pontszamitas(lapok: [int]):
    pontok = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok

def lapszamlalas(lapoksz: [int]):
    lapsz = 0
    for i in range(len(lapoksz)):
        lapsz += 1
    return lapsz
#Tesztesetek

def jatekosNagyobb_H_egy_Teszt():
    jatekosLista = [6, 5, 7, 8]
    gepLista = [6, 5, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: Pont nagyobb mint 21)")
    else:
        print("A teszt megbukott. (Játekos teszt: Pont nagyobb mint 21)")

def jatekosKevesebbP_Teszt():
    jatekosLista = [4, 5, 6, 3]
    gepLista = [5, 5, 5, 5]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játékos teszt: Kevesebb pont)")
    else:
        print("A teszt megbukott. (Játékos teszt: Kevesebb pont)")
def jatekosEgyenloP_TobbL_Teszt():
    jatekosLista = [4, 5, 6, 3, 2]
    gepLista = [5, 5, 5, 5]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játékos teszt: Egyenlő pontok több lap)")
    else:
        print("A teszt megbukott. (Játékos teszt: Egyenlő pontok több lap)")
def gepNagyobb_H_egy_Teszt():
    jatekosLista = [4, 5, 6, 2]
    gepLista = [5, 5, 5, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Gép teszt: Pont nagyobb mint 21)")
    else:
        print("A teszt megbukott. (Gép teszt: Pont kevesebb mint 21)")
def gepKevesebbP_Teszt():
    jatekosLista = [4, 5, 6, 3]
    gepLista = [5, 5, 5]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Gép teszt: Kevesebb pont)")
    else:
        print("A teszt megbukott. (Gép teszt: Kevesebb pont)")
def gepEgyenloP_TobbL_Teszt():
    jatekosLista = [4, 5, 6,]
    gepLista = [5, 5, 3, 2]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Gép teszt: Egyenlő pontok több lap)")
    else:
        print("A teszt megbukott. (Gép teszt: Egyenlő pontok több lap)")
def jatekosNyert_Teszt():
    jatekosLista = [4, 5, 6, 5]
    gepLista = [5, 5, 5, 3]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Játékos teszt: Játékosnak több pontja van)")
    else:
        print("A teszt megbukott. (Játékos teszt: Játékosnak több pontja van)")
def gepNyert_Teszt():
    jatekosLista = [4, 5, 6, 2]
    gepLista = [5, 5, 5, 3]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Gép teszt: Gépnek több pontja van)")
    else:
        print("A teszt megbukott. (Gép teszt: Gépnek több pontja van)")
def dontetlen_Teszt():
    jatekosLista = [4, 5, 6, 3]
    gepLista = [5, 5, 5, 3]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Döntetlen, osztoztok a nyereségen"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres.(Döntetlen teszt)")
    else:
        print("A teszt megbukott. (Döntetlen teszt)")
# Házi
def jatekos_H_egy_Teszt():
    jatekosLista = [6, 5, 7, 3]
    gepLista = [6, 5, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: Pont egyenlő: 21)")
    else:
        print("A teszt megbukott. (Játekos teszt: Pont egyenlő: 21)")
def jatekosTobbL_T_K_Teszt():
    jatekosLista = [6, 5, 7, 1]
    gepLista = [6, 5, 4]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: 19 pont több lappal)")
    else:
        print("A teszt megbukott. (Játekos teszt: 19 pont több lappal)")
def jatekosKevesebbL_T_K_Teszt():
    jatekosLista = [6, 11, 2]
    gepLista = [6, 5, 4, 2]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: 19 pont kevesebb lappal)")
    else:
        print("A teszt megbukott. (Játekos teszt: 19 pont kevesebb lappal)")
def jatekos_H_egy_Veszt_Teszt():
    jatekosLista = [6, 5, 7, 3]
    gepLista = [6, 5, 10]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: Pont egyenlő: 21 vesztett teszt)")
    else:
        print("A teszt megbukott. (Játekos teszt: Pont egyenlő: 21 vesztett teszt)")

def jatekosTobbL_T_K_Veszt_Teszt():
    jatekosLista = [6, 5, 7, 1]
    gepLista = [6, 5, 9]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: 19 pont több lappal (Vesztett))")
    else:
        print("A teszt megbukott. (Játekos teszt: 19 pont több lappal (Vesztett))")
def jatekosKevesebbL_T_K_Veszt_Teszt():
    jatekosLista = [6, 11, 2]
    gepLista = [6, 5, 4, 5]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: 19 pont kevesebb lappal (Vesztett))")
    else:
        print("A teszt megbukott. (Játekos teszt: 19 pont kevesebb lappal (Vesztett))")

def gep_H_egy_Teszt():
    jatekosLista = [6, 5, 8]
    gepLista = [6, 5, 7, 3]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: Pont egyenlő: 21)")
    else:
        print("A teszt megbukott. (Játekos teszt: Pont egyenlő: 21)")
def gepTobbL_T_K_Teszt():
    jatekosLista = [6, 5, 4]
    gepLista = [6, 5, 7, 1]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: 19 pont több lappal)")
    else:
        print("A teszt megbukott. (Játekos teszt: 19 pont több lappal)")
def gepKevesebbL_T_K_Teszt():
    jatekosLista = [6, 5, 4, 2]
    gepLista = [6, 11, 2]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: 19 pont kevesebb lappal)")
    else:
        print("A teszt megbukott. (Játekos teszt: 19 pont kevesebb lappal)")
def gep_H_egy_Veszt_Teszt():
    jatekosLista = [6, 5, 10]
    gepLista = [6, 5, 5, 5]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Játekos teszt: Pont egyenlő: 21 vesztett teszt (Vesztett))")
    else:
        print("A teszt megbukott. (Játekos teszt: Pont egyenlő: 21 vesztett teszt (Vesztett))")

def gepTobbL_T_K_Veszt_Teszt():
    jatekosLista = [6, 5, 9]
    gepLista = [6, 5, 4, 4]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Gép teszt: 19 pont több lappal (Vesztett))")
    else:
        print("A teszt megbukott. (Gép teszt: 19 pont több lappal (Vesztett))")
def gepKevesebbL_T_K_Veszt_Teszt():
    jatekosLista = [6, 5, 6, 3]
    gepLista = [6, 5, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Gép teszt: 19 pont kevesebb lappal (Vesztett))")
    else:
        print("A teszt megbukott. (Gép teszt: 19 pont kevesebb lappal (Vesztett))")
def mindK_H_egy_Dontetlen_Teszt():
    jatekosLista = [6, 5, 6, 4]
    gepLista = [6, 5, 8, 2]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Döntetlen, osztoztok a nyereségen"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Döntetlen teszt: Mind 2 fél 21 pont)")
    else:
        print("A teszt megbukott. (Döntetlen teszt: Mind 2 fél 21 pont)")
def kevesebb_H_egy_Dontetlen_Teszt():
    jatekosLista = [6, 5, 6]
    gepLista = [6, 3, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Döntetlen, osztoztok a nyereségen"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Döntetlen teszt: Mind 2 fél egyenlő pont és lapszám)")
    else:
        print("A teszt megbukott. (Döntetlen teszt: Mind 2 fél 21 pont és lapszám)")
def mindK_Nagyobb_H_egy_Dontetlen_Teszt():
    jatekosLista = [6, 5, 6, 6]
    gepLista = [6, 5, 8, 8]
    kapottEredmeny = eredmeny(jatekosLista, gepLista, jatekosLista, gepLista)
    vartEredmeny = "Döntetlen, a ház nyert"
    if kapottEredmeny == vartEredmeny:
        print("A teszt sikeres. (Döntetlen teszt: Mind 2 fél meghaladta 21 pontot)")
    else:
        print("A teszt megbukott. (Döntetlen teszt: Mind 2 fél meghaladta 21 pont)")
def tesztek():
    jatekosNagyobb_H_egy_Teszt()
    jatekosKevesebbP_Teszt()
    jatekosEgyenloP_TobbL_Teszt()

    gepNagyobb_H_egy_Teszt()
    gepKevesebbP_Teszt()
    gepEgyenloP_TobbL_Teszt()

    jatekosNyert_Teszt()
    gepNyert_Teszt()
    dontetlen_Teszt()
    #Házi
    jatekos_H_egy_Teszt()
    jatekosTobbL_T_K_Teszt()
    jatekosKevesebbL_T_K_Teszt()

    jatekos_H_egy_Veszt_Teszt()
    jatekosTobbL_T_K_Veszt_Teszt()
    jatekosKevesebbL_T_K_Veszt_Teszt()

    gep_H_egy_Teszt()
    gepTobbL_T_K_Teszt()
    gepKevesebbL_T_K_Teszt()

    gep_H_egy_Veszt_Teszt()
    gepTobbL_T_K_Veszt_Teszt()
    gepKevesebbL_T_K_Veszt_Teszt()

    mindK_H_egy_Dontetlen_Teszt()
    kevesebb_H_egy_Dontetlen_Teszt()
    mindK_Nagyobb_H_egy_Dontetlen_Teszt()
tesztek()