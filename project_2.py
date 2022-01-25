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

def uhadnute_cislo(tip,org_cisla,vizual):
# dodelat premisteni '-', hlásí to chyba v indexu a blokuje chod kódu!
    bulls = 0
    cows = 0
    for i,cislo in enumerate(org_cisla):
        print(i,cislo)
        if cislo == vizual[i]:
            vizual[i] = cislo
            bulls += 1
            print(f'Bulls : {bulls}')
        elif org_cisla in vizual:
            cown += 1

def kontrola_hrace(tip):
    #FUNC HOTOVA!
    '''
    Func slouží k ověření vstupu (tip) od hráče, zda, splňuje podmínky.
    1.(tip) obsahuje jenom čísla a ne žádné jíné znaky.
    2.(tip) má délku 4.
    3.(tip) nezačíná 0.
    4.neopakují čísla v (tip).
    :param tip: Vstup od hráče který tipuje.
    :return: Vrací Boolen True, když je vše ok nebo False.
    '''
    tip1 = str(tip)
    kontrola_set = []
    spravnost = True
    while True:
        if not str(tip1).isnumeric():
            print('Kód obsahu<je nepovolené znaky')
            spravnost = False
            break
        if len(str(tip1)) != 4:
            print('Kód má obsahovat 4 číslice!')
            spravnost = False
            break
        elif int(tip1) == 0:
            print('Kód nesmí začínat 0')
            spravnost = False
            break
        elif spravnost:
            for cislo in str(tip1):
                if cislo not in kontrola_set:
                    kontrola_set.append(cislo)
                else:
                    print('V kódu se opakují čísla!')
                    spravnost = False
                    break
            break
    return spravnost



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













