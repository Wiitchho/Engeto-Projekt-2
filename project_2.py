import datetime
import random

def nahodne_org_cisla():
    #HOTOVÁ FUNC!
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
    return s_t_r
def hrac_hada():
    #HOTOVA FUNC!
    '''
    funkce na hádání číslice
    :return: zadaná číslice v proměnné tip
    '''
    tip = str(input('Zadej císlici:'))
    return tip
def cow_kontrola(tip,cislo_org):
    # HOTOVÁ FUNC!
    '''
    :param tip: Tip hráče
    :param cislo_org: Unikátní kód, který se snaží uhodnout
    :return: Vrátí počet čísel, které uživatel zadal jako tip a jsou v kódu,
     ale ne na správném místě.
    '''
    cow = 0
    for cislo in tip:
        if cislo in cislo_org:
            cow += 1
    return cow
def bull_kontrola (tip,cislo_org):
    # HOTOVÁ FUNC!
    '''
    Func. která počítá bull. bull = tip hráče -> soprávné číslo na správném místě
    :param tip: Tip hráče
    :param cislo_org: Unikátní kód, který se snaží uhodnout
    :return: Vrátí počet čísel, které uživatel zadal jako tip a trefil i umístění.
    '''
    bull = 0
    for i, cislo_org in enumerate(cislo_org):
        if cislo_org in tip[i]:
            bull += 1

    return bull
def vypocet_cow(bull,cow):
    #FUNC HOTOVA!
    '''
    Počítá jaký je cow, když je min. 1 bull.
    :param bull:
    počet bull v tipu
    počet cow v tipu
    :return: vrací počet cow
    '''
    vysledek = cow - bull
    return vysledek
def kontrola_hrace(tip,org_cislo):
    #FUNC HOTOVA!
    '''
    Func slouží k ověření vstupu (tip) od hráče, zda, splňuje podmínky.
    Tlačítko pro možné rychlé ukončení(KO).
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
        if tip == 'KO':
            print(f'Prohrál jsi, cislo bylo: {org_cislo}')
            quit()

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
def mnoz_jedno(bull, cow):
    #FUNC HOTOVA!
    '''
    Kontrola pro jednotné a nebo množné číslo textu (Bull a Cow) vs (Bulls a Cows).
    :param bull:Když je bull větší jak 1 Tak je množné číslo Bulls
    :param cow: Když je cow větší jak 1 tak je množné číslo Cows
    :return: Vrátí tupl s upraveným textem podle jednotného nebo množného čísla.
    '''
    bull_text = ''
    cow_text = ''
    if bull > 1:
        bull_text = 'Bulls'
    elif bull <= 1:
        bull_text = 'Bull'
    if cow > 1:
        cow_text = 'Cows'
    elif cow <= 1:
        cow_text = 'Cow'
    return bull_text, cow_text
def hra_start():
    '''
    Func která spojuje ostatní funkce do jedné a díky tomu běží celá hra
    :return:
    '''
    cas_start = datetime.datetime.now()
    cas_start.strftime('%M:%S')
    hra_bezi = True
    sifra = nahodne_org_cisla()
    pocet_pokusu = 0
    while hra_bezi:
        tip_hrace = hrac_hada()
        kontrola = kontrola_hrace(tip_hrace,sifra)
        if kontrola == True:
            bull = bull_kontrola(tip_hrace,sifra)
            cow = cow_kontrola(tip_hrace,sifra)
            cow_vysledek = vypocet_cow(bull,cow)
            print(bull,mnoz_jedno(bull,cow_vysledek)[0],)
            print(cow_vysledek,mnoz_jedno(bull,cow_vysledek)[1])
            pocet_pokusu += 1
            if bull == 4:
                print(f'Gratuluji, vyhrál jsi!, Tvoje číslo bylo: {sifra}',
                      f'Potřeboval jsi k tomu : {pocet_pokusu} pokusů!',
                      sep='\n')

                hra_bezi = False

#Začátek programu________________
oddelovac = 20 * '-'
uvitani = len('Vítám tě u hry Bulls & Cows!') * '--'

print('Vítám tě u hry Bulls & Cows,',uvitani,
      'Program vytvoří 4 místný náhodný číselný kód',
      'Tvým cílem je uhadnout tyto čísla! ',
      uvitani,
      'Každé číslo je unikátní a proto se neopakuje',
      'Program bude ukazovat počet Bull/s a Cow/s',
      uvitani,
      'Bull znamená, že si trefil číslo i jeho umístění',
      'Cow znamená, že jsi uhádl číslici, ale ne umístění',
      uvitani,
      'Pravidla:',
      '1. Číslice musí být 4',
      '2. Číslice se nesmí opakovat',
      '3. Nejsou povoleny žádné jinačí znaky kromě číslic',
      uvitani,
      'Pokud se budeš chtít vzdát, napiš KO',
      uvitani,
      sep='\n')
cas_start = datetime.datetime.now()
cas_start.strftime('%M:%S')

hra_start()

#chces hrát znova nebo chces statistiky?
cas_konec = datetime.datetime.now()
cas_konec.strftime('%M:%S')
final_cas = cas_konec - cas_start
print(uvitani)
print(f'Trvalo ti to přesně : {final_cas}')
















