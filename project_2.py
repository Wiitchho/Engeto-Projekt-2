import random

def nahodne_org_cisla():
    seznam = [1,2,3,4,5,6,7,8,9]
    cislo = str(random.sample(seznam, 4))
    #spojit seznam do jednoho stringu
    return cislo


#uvítání
def nahodne_gener_c():
    while True:
        nahodne_cislo = int(random.random() * 9999)

        if len(str(nahodne_cislo)) == 4:
            for cislo in nahodne_cislo:
                if cislo in nahodne_cislo
            break
    return nahodne_cislo



oddelovac = 20 * '-'
uvitani = len('Vítám tě u hry Bulls & Cows!') * '-'

print('Vítám tě u hry Bulls & Cows,',uvitani,
      'Program vytvoří 4 místný náhodný číselný kód',
      'Tvým cílem je uhadnout tyto čísla! ',
      uvitani, sep='\n')

#Náhodně generované číslo
sifra = nahodne_gener_c()
print(nahodne_org_cisla())

#3.Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
# pokud bude obsahovat duplicity,začínat nulou, příp. obsahovat nečíselné znaky
# Program vyhodnotí tip uživatele

while True:
    hadam = int(input('Hádej číslo:'))
    if len(str(hadam)) != 4:
        print('Neplatný pokus')
    else:
        if hadam == sifra:
            print('Uhodnuto')
            break
        else:
            print('Zkus to znovu!')





