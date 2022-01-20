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
print(nahodne_gener_c())
