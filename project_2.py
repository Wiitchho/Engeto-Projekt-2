import random

def nahodne_org_cisla():
    seznam = [1,2,3,4,5,6,7,8,9]
    cislo_seznam = random.sample(seznam, 4)
    s_t_r = ''
    for cislo in cislo_seznam:
        s_t_r += str(cislo)
    print(s_t_r) # vymazat print, je jenom pro kontrolu
    return s_t_r

def hra_start():
    True
    nahodne_org_cisla()

def kontrola_hrace():
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
uvitani = len('Vítám tě u hry Bulls & Cows!') * '-'

print('Vítám tě u hry Bulls & Cows,',uvitani,
      'Program vytvoří 4 místný náhodný číselný kód',
      'Tvým cílem je uhadnout tyto čísla! ',
      uvitani, sep='\n')

#3.Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
# pokud bude obsahovat duplicity,začínat nulou, příp. obsahovat nečíselné znaky
# Program vyhodnotí tip uživatele





hra_start()
while hra_start():
    zadavani = input('Zadej váš 4 místný kód')
    for i,cislo in enumerate(zadavani):
        if cislo in gener_num:
            print(cislo)
            print('správně')











