import random

with open("noms.txt", "r") as file:
    noms = file.read().splitlines()

noms = [nom.strip() for nom in noms]

if len(noms) < 2:
    print("erreur")
else:
    random.shuffle(noms)
    
    with open("res.txt", "w") as result_file:
        for i in range(len(noms)):
            personne = noms[i]
            personne_attribuee = noms[(i + 1) % len(noms)]
            line = f"{personne} offre un cadeau à {personne_attribuee}\n"
            print(line)
            result_file.write(line)
