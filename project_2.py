import random

#uvítání
def nahodne_gener_c():
    while True:
        nahodne_cislo = int(random.random() * 9999)

        if len(str(nahodne_cislo)) == 4:
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
print(sifra)

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





