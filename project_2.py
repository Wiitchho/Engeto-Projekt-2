import random

def nahodne_org_cisla():
    #FUNKCE HOTOVÁ!
    '''
    funkce ke generování náhodného 4-místného unikátního čísla
    Ze seznamu vždy vezme jeden parametr a připojí ho do proměnné s_t_r

    :return: 4 místný uníkátní kód uložený ve strignu
    '''
    seznam = [1,2,3,4,5,6,7,8,9]
    cislo_seznam = random.sample(seznam, 4)
    s_t_r = ''
    for cislo in cislo_seznam:
        s_t_r += str(cislo)
    print(s_t_r) # vymazat print, je jenom pro kontrolu
    return s_t_r

def hra_start():
    vizual = ['____']
    cisla = nahodne_org_cisla()

    while True:
        tip = hrac_hada(vizual)
        uhadnute_cislo(tip,cisla,vizual)



def hrac_hada(vizual):
    #Funkce HOTOVA!
    '''
    funkce na hádání číslice
    :param vizual:  '_ _ _ _'
    :return: zadaná číslice v proměnné tip
    '''
    print(' '.join(vizual))
    tip = str(input('Zadej císlici:'))
    return tip

def uhadnute_cislo(tip,cisla,vizual):
# dodelat premisteni '-', hlásí to chyba v indexu a blokuje chod kódu!
    bulls = 0
    cows = 0
    for i,cislo in enumerate(cisla):
        print(i,cislo)
        if cisla == vizual[i]:
            vizual[i] = tip
            bulls += 1
            print(f'Bulls : {bulls}')
        elif cisla in vizual:
            cown += 1



def kontrola_hrace():
#Dodělat kontrolu hráče, není zapojena do programu!
    seznam_cisel = []
    while True:
        zadavani = input('Zadej váš 4 místný kód')
        if len(str(zadavani)) != 4:
            print('Kód má obsahovat pouze 4 číslice!')
        elif int(zadavani) == 0:
            print('Kód nesmí začínat 0')
        #elif not zadavani.isnumeric():
            #print('Kód obsahuje nepovolené znaky')
        for cisla in zadavani:
            if cisla in seznam_cisel:
                seznam_cisel.append(cisla)
                print('Číslo musí být originál')

    else:
        print('vše je OK')
        False



#uvítání
oddelovac = 20 * '-'
uvitani = len('Vítám tě u hry Bulls & Cows!') * '--'

print('Vítám tě u hry Bulls & Cows,',uvitani,
      'Program vytvoří 4 místný náhodný číselný kód',
      'Tvým cílem je uhadnout tyto čísla! ',
      uvitani,
      'Každé číslo je unikátní a proto se neopakuje',
      uvitani, sep='\n')

#3.Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
# pokud bude obsahovat duplicity,začínat nulou, příp. obsahovat nečíselné znaky
# Program vyhodnotí tip uživatele

hra_start()













