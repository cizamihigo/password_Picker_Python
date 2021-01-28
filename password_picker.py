import random
import string

print("This Is Password Picker")

Nouns = ['Student','Christian','Rodrigue',
'congo', 'prosper','gloire', 'Expert','Kigali',
'Gisozi','Nyamirambo','Nyarutarama','Nyarugenge',
'musicien','chanteur','danseur','droomeur',
'Enseignant','AskGoogle','Aksanti','Amina']
number = random.randrange(0,3000)
spec_char = random.choice(string.punctuation)
adjectives = ['Loyal','special','secure','happy','Jovial','Peaceful',
'dark','suny','cold','wet','Orange','Fat','Flat', 'sleepy', 'fast', 'slow', 'white', 'blue'
,'yellow','greeen','brave','proud','...','groove','grind','grinning']

while True:

    Up = random.choice(Nouns).upper()
    Low = random.choice(Nouns).lower()
    uplow = [Up, Low]
    nounchoice = random.choice(uplow)

    Upa = random.choice(adjectives).upper()
    Lowa = random.choice(adjectives).lower()
    uplowa = [Upa, Lowa]
    adjectivechoice = random.choice(uplowa)

    password = '~' + adjectivechoice + nounchoice + str(number) + spec_char
    print("New password is : %s " %password)

    useranswer = input("Do you need another password \ty or \tn \t:")
    response = useranswer.upper()
    if response == 'N' :
        break


