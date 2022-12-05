import random
# Définir la liste lst_cards contenant la liste des cartes d'un jeu de 54 cartes
# A l'aide de caractère ASCII (cf. table des caractères ASCII jointes), déclarez une liste "lst_colors" contenant les couleurs d'un jeu de cartes
# - Carreau / Coeur / Trèfle / Pique
lst_colors = [chr(3), chr(4), chr(5), chr(6)]
# Résultat attendu : ['\x03', '\x04', '\x05', '\x06']
# Déclarez une liste "lst_signs" contenant la liste des types de cartes que peut contenir un jeu de cartes: 
lst_signs = ["As", "Roi", "Dame", "Valet"] + list(range(2,11))
lst_cards = []
for color in lst_colors:
    for sign in lst_signs:
        lst_cards.append(str(sign)+color)
random.shuffle(lst_cards)

lst_cards_player = lst_cards[:26]
lst_cards_computer = lst_cards[26:53]

# Affichage de la main de départ du joueur et de l'ordinateur
# print("Cartes joueur:", end=",")
# for card in lst_cards_player:
#     print(card, end=" ")
# print("\nCartes ordinateur:", end=",")
# for card in lst_cards_computer:
#     print(card, end=" ")

i = 0
input_abandon = "n"
# La partie continue tant que le joueur n'a pas décidé d'abandonner ou tant que l'ordinateur ou le joueur ne possède plus de carte
while input_abandon == "n" and len(lst_cards_player) != 0 and  len(lst_cards_computer) != 0:
    # Afficher la carte piochée par le joueur (nombre de cartes qu'il possède') /  la carte piochée par l'ordinateur (nombre de cartes qu'il possède')
    print("\nJoueur :", lst_cards_player[i] + " (" + str(len(lst_cards_player)) + ")", end=" / ")
    print("Ordinateur :", lst_cards_computer[i] + " (" + str(len(lst_cards_computer)) + ")")
    
    card_player = lst_cards_player[i][:-1]
    card_computer = lst_cards_computer[i][:-1]

    if card_player == card_computer:
        print("Egalité")
        lst_cards_computer.append(lst_cards_computer[i])
        lst_cards_player.append(lst_cards_player[i])
    elif card_player == "As" or card_player == "Roi" or card_player == "Dame" or card_player == "Valet" :
        if card_player == "As":
            print("Gagné !")
            lst_cards_player.append(lst_cards_computer[i])
            lst_cards_player.append(lst_cards_player[i])
        elif card_player == "Roi" and card_computer == "As" :
            print("Perdu :(")
            lst_cards_computer.append(lst_cards_computer[i])
            lst_cards_computer.append(lst_cards_player[i])
        elif card_player == "Dame" and (card_computer == "As" or card_computer == "Roi"):
            print("Perdu :(")
            lst_cards_computer.append(lst_cards_computer[i])
            lst_cards_computer.append(lst_cards_player[i])
        else:
            print("Gagné !")
            lst_cards_player.append(lst_cards_player[i])
            lst_cards_player.append(lst_cards_computer[i])
    else:
        if card_player > card_computer:
            print("Gagné !")
            lst_cards_player.append(lst_cards_player[i])
            lst_cards_player.append(lst_cards_computer[i])
        else:
            print("Perdu :(")
            lst_cards_computer.append(lst_cards_computer[i])
            lst_cards_computer.append(lst_cards_player[i])

    lst_cards_player.pop(i)
    lst_cards_computer.pop(i)

    # Affichage de la main du joueur et de l'ordinateur
    print("Cartes joueur:", end=",")
    for card in lst_cards_player:
        print(card, end=" ")
    print("\nCartes ordinateur:", end=",")
    for card in lst_cards_computer:
        print(card, end=" ")
    print("\n")

    input_abandon = input("Souhaitez-vous abandonner la partie (y:yes/n:no) ?")

if len(lst_cards_player) == 0 or input_abandon == "y":
    print("Vous avez perdu la partie")
else:
    print("Vous avez gagné la partie")