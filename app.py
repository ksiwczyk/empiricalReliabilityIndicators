#CONST
AUTOR = 'Konrad Siwczyk'
PRZEDMIOT = 'Podstawy niezawodności'
PROWADZACY_PRZEDMIOT = 'mgr inz. A.Pawlak'
TEMAT_ZADANIA = 'Wyznaczenie empirycznych wskaźników niezawodności: F(t), R(t), f(t), λ(t), ET na podstawie próby losowej.'
KOMUNIKAT_BŁEDU = 'Coś poszło nie tak, sprawdz ponownie.'
CZAS_OCZEKIWANIA = 2

#MODUŁY
import time
import matplotlib.pyplot as plt
#+-+-+-+-+-+-+-+-+-APP+-+-+-+-+-+-+-+-+-#

#INFORMACJE POWITALNE
print("AUTOR: \n{}".format(AUTOR))
print("{},{}".format(PRZEDMIOT, PROWADZACY_PRZEDMIOT))
print("Temat wykonywanego zadania: {}".format(TEMAT_ZADANIA))

#DEKLARACJA ILOŚCI DANYCH ORAZ SUMY DANYCH
print("Podaj liczbę danych do zadeklarowania:")
liczbaDanych = int(input())
#jesli beda jakies dane wystepowac to:
if liczbaDanych > 0:
    #podaj sumę liczb
    print("Podaj sumę liczb danych:")
    #wprowadz sumę liczb, *suma liczb danych musi byc calkowita*
    sumaLiczbDanych = int(input())
    print("Liczba danych oraz suma liczb danych zostały zadeklarowane!\n")
    print("Wprowadzone dane prezentują się następująco:\nLiczba danych do zadreklarowania: {}.\nSuma zadreklarowanych liczb: {}.".format(liczbaDanych, sumaLiczbDanych))
    #Ustalenie pierwszej wprowadzanej liczby przez użytkownika, język Python domyślnie dla pierwszej wartości przypisuje 0.
    #Dla poprawności wyświetlania wartości zostanie przez nas zadeklarowana wartość 1.
    startowaWartoscWprowadzanychDanych = 1
    #Deklaracja listy do przechowywania wartości wprowadzanych przez użytkownika oraz deklaracja jej długości
    wprowadzoneDane = []
    #Do funkcji len została dodana zmienna 'startowaWartoscWprowadzanychDanych' o wartości 1, gdyż domyślna pozycja startowa przesuneła się o 1 do przodu.
    dlugoscListyWprowadzoneDane = liczbaDanych + startowaWartoscWprowadzanychDanych
    #Użycie pętli for w celu wprowadzenia danych przez użytkownika.
    tempSumNumbers = 0
    pozostałoElementowDoWpisania = 0
    pozostałaSumaElementowDoWpisania = 0
    for liczbaIteracji in range(startowaWartoscWprowadzanychDanych, dlugoscListyWprowadzoneDane):
        print("Wprowadz {} liczbę: ".format(liczbaIteracji))
        #Podanie wartosci przez użytkownika, wymuszenie na użytkowniku podanie liczby o typie integer - czyli całkowitej
        #Przypisanie podanej wartości do zmiennej 'liczba'
        liczba = int(input())
        if liczba >= 0:
            if liczbaIteracji < dlugoscListyWprowadzoneDane:
                        #Dodanie wartości zmiennej 'liczba' do wcześniej utworzonej listy 'wprowadzoneDane'
                        wprowadzoneDane.append(liczba)
                        #Aktualnie wprowadzone dane do tablicy 'wprowadzoneDane'
                        print("Aktualnie wprowadzone dane: {}".format(wprowadzoneDane))
                        #Deklaracja 'zmiennej pomocniczej' o nazwie 'tempSumNumbers' -> Zmienna ma za zadanie zliczać obecną sumę wpisanych elementów do tablicy 
                        tempSumNumbers = tempSumNumbers + liczba
                        #Informacja o ilości pozostałych elementów do zadeklarowania
                        pozostałoElementowDoWpisania = liczbaDanych - liczbaIteracji
                        print("Do wypełnienia wszystkich zadeklarowanych liczb pozostało Ci {} liczb.".format(pozostałoElementowDoWpisania))
                        #Informacja o sumie elementów jaka pozostała do zadreklarowania
                        pozostałaSumaElementowDoWpisania = sumaLiczbDanych - tempSumNumbers
                        print("Musisz jeszcze zadeklarować elementy o łącznej sumie: {}.".format(pozostałaSumaElementowDoWpisania))
            elif liczbaIteracji == liczbaDanych and liczbaDanych == dlugoscListyWprowadzoneDane:    
                if sumaLiczbDanych == tempSumNumbers:
                    print("Aktualne dane: ", wprowadzoneDane)
                    print("Wartości zostały wprowadzone poprawnie i przeszły kontrole zgodności.")
            else:
                print(KOMUNIKAT_BŁEDU)
        else:
            print(KOMUNIKAT_BŁEDU)
print("Trwa ładowanie danych ...")
time.sleep(CZAS_OCZEKIWANIA)
print("############################################################")
menuString = 'MENU'.center(10)
print("{}".format(menuString))
print("############################################################")
print("1. Obliczanie dystrybuanty F*(t)")
print("2. Obliczanie funkcji niezawodności R*(t)")
print("3. Obliczanie funkcji gęstości prawdopodobieństwa f*(t)")
print("4. Obliczanie funkcji intensywności uszkodzeń lambda*(t)")
print("5. Obliczanie ET")
print("6. Koniec programu")
print("############################################################")
wybierzOpcje = input('Klinij liczbę od 1 do 6, aby wybrać daną opcje\n')
time.sleep(CZAS_OCZEKIWANIA)                

def sumowanieWartosci(liczbaIteracji, wprowadzoneDane):
    suma = 0
    for liczbaIteracjiSumowanieWartosci in range(liczbaIteracji):
        suma = suma + wprowadzoneDane[liczbaIteracjiSumowanieWartosci]
    return suma
if wybierzOpcje == '1':
    print("Wybrano: Obliczanie dystrybuanty F*(t)")
    time.sleep(CZAS_OCZEKIWANIA)
    wynikiDystrybuanta = []
    pomSumaElementow = 0
    pierwszaWartoscEmpirycznaDystrybuanty = 0
    wynikiDystrybuanta.append(pierwszaWartoscEmpirycznaDystrybuanty)
    for liczbaIteracji in range(1, len(wprowadzoneDane)):
        pomSumaElementow = pomSumaElementow + wprowadzoneDane[liczbaIteracji]
        wynikDystrybuanta = pomSumaElementow / sumaLiczbDanych
        wynikiDystrybuanta.append(round(wynikDystrybuanta, 3))
        print("Empiryczna wartosc dystrybuanty dla wartości {} to: {}".format(liczbaIteracji, wynikiDystrybuanta[liczbaIteracji]))
    plt.grid(True)
    plt.plot(wynikiDystrybuanta)
elif wybierzOpcje == '2':
    print("Wybrano: Obliczanie funkcji niezawodności R*(t)")
    time.sleep(CZAS_OCZEKIWANIA)
    wynikiNiezawodnosc = []
    pierwszaWartoscEmpirycznaNiezawodnosci = 1
    wynikiNiezawodnosc.append(pierwszaWartoscEmpirycznaNiezawodnosci) 
    for liczbaIteracji in range(1, len(wprowadzoneDane)+1):
        wynikNiezawodnosc = (sumaLiczbDanych - sumowanieWartosci(liczbaIteracji, wprowadzoneDane)) / sumaLiczbDanych
        wynikiNiezawodnosc.append(round(wynikNiezawodnosc, 3))
        print("Empiryczna wartosc niezawodnosci dla wartości {} to: {}".format(liczbaIteracji, wynikiNiezawodnosc[liczbaIteracji]))   
    plt.grid(True)
    plt.plot(wynikiNiezawodnosc)
elif wybierzOpcje == '3':
    if liczbaDanych < 10:
        print("Wybrano: Obliczanie funkcji gęstości prawdopodobieństwa f*(t)")
        time.sleep(CZAS_OCZEKIWANIA)
        wynikiGestosc = []
        pierwszaWartoscEmpirycznaGestosci = 0
        wynikiGestosc.append(pierwszaWartoscEmpirycznaGestosci)
        print("Empiryczna wartość gęstości dla wartości 1 to: 0")
        for liczbaIteracji in range(1, 9):
            wynikGestosc = wprowadzoneDane[liczbaIteracji] / (sumaLiczbDanych * (liczbaIteracji - (liczbaIteracji-1)))
            wynikiGestosc.append(round(wynikGestosc, 3))
            print("Empiryczna wartość gęstości dla wartości {} to: {}".format(liczbaIteracji+1, wynikiGestosc[liczbaIteracji]))
        plt.grid(True)
        plt.plot(wynikiGestosc)
    else:
        print("Przy obliczaniu gęstości musi być maksymalnie 9 liczb! Wpisz wartości ponownie!")

elif wybierzOpcje == '4':   
    if liczbaDanych < 10:
        print("Wybrano: Obliczanie funkcji intensywności uszkodzeń lambda*(t)")
        time.sleep(CZAS_OCZEKIWANIA)
        wynikiUszkodzen = []
        pierwszaWartoscEmpirycznaUszkodzen = 0
        wynikiUszkodzen.append(pierwszaWartoscEmpirycznaUszkodzen)
        print("Empiryczna wartość uszkodzeń dla wartości 1 to: 0")
        pomSumaElementow = 0
        for liczbaIteracji in range(1,9):
            pomSumaElementow = pomSumaElementow + wprowadzoneDane[liczbaIteracji]
            pomSumaElementow2 = pomSumaElementow - wprowadzoneDane[liczbaIteracji]
            licznik = wprowadzoneDane[liczbaIteracji]
            mianownik = ((sumaLiczbDanych - pomSumaElementow2) * (liczbaIteracji - (liczbaIteracji - 1)))
            wynikUszkodzen = licznik / mianownik
            wynikiUszkodzen.append(round(wynikUszkodzen, 3))
            print("Empiryczna wartość uszkodzeń dla wartości {} to: {}".format(liczbaIteracji+1, wynikiUszkodzen[liczbaIteracji]))    
        plt.grid(True)
        plt.plot(wynikiUszkodzen)
    else:
        print("Przy obliczaniu gęstości musi być maksymalnie 9 liczb! Wpisz wartości ponownie!")
elif wybierzOpcje == '5':
    if liczbaDanych == 10:
        print("Wybrano: Obliczanie wskaznika ET z dystrybuanty F*(t)")
        time.sleep(CZAS_OCZEKIWANIA)
        wynikiDystrybuanta = []
        wynikiSredniaTrwalosc = []
        pomSumaElementow = 0
        pierwszaWartoscEmpirycznaDystrybuanty = 0
        wynikiDystrybuanta.append(pierwszaWartoscEmpirycznaDystrybuanty)
        listaLiczbIteracji = []
        for liczbaIteracji in range(1, len(wprowadzoneDane)):
            listaLiczbIteracji.append(liczbaIteracji)
            pomSumaElementow = pomSumaElementow + wprowadzoneDane[liczbaIteracji]
            wynikDystrybuanta = pomSumaElementow / sumaLiczbDanych
            wynikiDystrybuanta.append(round(wynikDystrybuanta, 3))
            print("Empiryczna wartosc dystrybuanty dla wartości {} to: {}".format(liczbaIteracji, wynikiDystrybuanta[liczbaIteracji]))
        for liczbaIteracji in range(1, 9):
            wynikSredniaTrwalosc = (wynikiDystrybuanta[liczbaIteracji + 1] - wynikiDystrybuanta[liczbaIteracji]) * (liczbaIteracji+1)
            wynikiSredniaTrwalosc.append(round(wynikSredniaTrwalosc, 3))    
        ET = sum(wynikiSredniaTrwalosc) + wynikiDystrybuanta[1]
        print(wynikiSredniaTrwalosc)
        print("Średnia trwałość wynosi: {}".format(round(ET, 1)))
        #plt.plot(listaLiczbIteracji, marker='x')
        listaET = []
        listaET.append(round(ET, 3))
        plt.plot(listaET, marker='x')
        plt.grid(True)
        plt.show()
elif wybierzOpcje == '6':
    print("Wybrano: Koniec programu")
    time.sleep(CZAS_OCZEKIWANIA) 
    exit()      