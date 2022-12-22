# EXERCICE 1 : 1. A l’aide de la table des caractères ASCII fournie en annexe, déclarer une liste « lst_colors »
# et stockez les 4 couleurs (carreau, cœur, trèfle, pique) d’un jeu de cartes sous la forme d’un caractère
lst_colors = [chr(3), chr(4), chr(5), chr(6)]
# print("lst_colors : ", lst_colors)

# EXERCICE 1 : 2. Déclarez une liste « lst_values » et stockez dans celle-ci la liste des valeurs d’un jeu de cartes.
# Pour générer les valeurs allant de 2 à 10 vous utiliserez les méthodes list() et range().
lst_values = ["As", "Roi", "Dame", "Valet"] + list(range(2,11))
# print("lst_values : ", lst_values)

# EXERCICE 1 : 3. Déclarez une liste « lst_cards » et, à l’aide de 2 boucles,
# remplissez cette liste avec les 52 cartes qui constituent un jeu de cartes
# en utilisant les 2 listes déclarées ci-dessus (« lst_colors » et « lst_values »)
lst_cards = []
for color in lst_colors:
    for sign in lst_values:
        lst_cards.append(str(sign)+color)
# print("lst_cards : ", lst_cards)


# EXERCICE 1 : 4. A l’aide de la bibliothèque random, mélangez la liste « lst_cards »
# en copiant/collantle code ci-dessous :
import random
random.shuffle(lst_cards)
# print("lst_cards : ", lst_cards)

# EXERCICE 1 : 5. Affectez les 52 cartes en part égale dans les 2 listes respectives suivantes :
# « lst_player_cards » et « lst_computer_cards »
lst_player_cards = lst_cards[:26]
# print(lst_player_cards)
lst_computer_cards = lst_cards[26:53]
# print("lst_computer_cards : ", lst_computer_cards)

# EXERCICE 2 : 1. A l’aide d’une boucle judicieusement choisie, demandez au joueur s’il souhaite abandonner ou non,
# il devra saisir 0 pour « Non » et 1 pour « Oui ».En cas d’abandon quittez la boucle.
input_abandon = 0
# EXERCICE 2 : 5. Gardez en stock la carte piochée par le joueur ainsi que celle piochée par l’ordinateur. Pour ce faire,
# déclarez 2 listes : « lst_player_cards_playing » et « lst_computeur_cards_playing ». 
lst_player_cards_playing = []
lst_computer_cards_playing = []
while input_abandon == 0 and len(lst_player_cards) != 0 and len(lst_computer_cards) != 0:
    # EXERCICE 2 : 3. A l’intérieur de cette boucle et avant de posez la question au joueur s’il souhaite abandonner,
    # affichez la carte piochée par le joueur ainsi que par l’ordinateur.
    # Cette action revient à afficher la première valeur des listes respectives « lst_player_cards » et « lst_computer_cards »
    # EXERCICE 2 : 4. Reprenez l’affichage de la question 3. et concaténez avec le nombre de cartes que possède le joueur et le nombre de cartes que possède l’ordinateur
    print("\nJoueur :", lst_player_cards[0] + " (" + str(len(lst_player_cards)) + " cartes)", end=" / ")
    print("Ordinateur :", lst_computer_cards[0] + " (" + str(len(lst_computer_cards)) + " cartes)")
    
    # EXERCICE 2 : 5. Ajoutez la carte piochée par le joueur à la liste « lst_player_cards_playing »
    # et la carte piochée par l’ordinateur à la liste  « lst_computer_cards_playing ».
    lst_player_cards_playing.append(lst_player_cards[0])
    # print("lst_player_cards_playing : ", lst_player_cards_playing)
    lst_computer_cards_playing.append(lst_computer_cards[0])
    # print("lst_computer_cards_playing : ", lst_computer_cards_playing)

    # EXERCICE 2 : 6. Retirer les cartes piochées des listes « lst_player_cards » et « lst_computer_cards »
    lst_player_cards.pop(0)
    # print("lst_player_cards : ", lst_player_cards)
    lst_computer_cards.pop(0)
    # print("lst_computer_cards : ", lst_computer_cards)

    # EXERCICE 3 : 1. Avant toute chose, pour contrôler quel est la vainqueur d’une manche
    # et afin que la comparaison soit plus simple vous allez devoir retirer le caractère ASCII
    # récupéré pour ne garder que la valeur de chacune des cartes piochées. Une fois le caractère retiré,
    # stockez les valeurs retraitées dans les variables temporaires
    # suivantes : « value_player_card » et « value_computer_card ».
    # Intégrez ce retraitement avant de demander au joueur s’il souhaite abandonner la partie.
    player_card = lst_player_cards_playing[-1]
    value_player_card = player_card[:-1]
    # print("value_player_card : ", value_player_card)
    computer_card = lst_computer_cards_playing[-1]
    value_computer_card = computer_card[:-1]
    # print("value_computer_card : ", value_computer_card)

    # EXERCICE 3 : 2. Afin de savoir qui remporte la manche, testez dans un premier temps à l’aide 
    # d’une condition, si le valeur de la carte piochée par le joueur est égale à la valeur piochée
    # par l’ordinateur et affichez « Bataille ! »
    if value_player_card == value_computer_card:
        print("Bataille !")
        # EXERCICE 3 : 6. Gérez la bataille : lors d’une bataille le joueur et l’ordinateur vont devoir piocher
        # une nouvelle carte sans la regarder et l’ajouter dans la liste des cartes en jeu.
        # Pour ce faire, prenez la première valeur des listes « lst_player_cards » et « lst_computer_cards »
        # pour les ajouter aux listes respectives « lst_player_cards_playing » et « lst_computer_cards_playing »
        # puis supprimez ces valeurs des listes « lst_player_cards » et « lst_computer_cards »
        lst_player_cards_playing.append(lst_player_cards[0])
        lst_computer_cards_playing.append(lst_computer_cards[0])
        lst_player_cards.pop(0)
        lst_computer_cards.pop(0)

    # EXERCICE 3 : 4. A l’aide du tableau de la question précédente,
    # écrivez la suite du test conditionnel de la question afin savoir si le joueur a gagné
    # et affichez « Manche remportée », dans le cas contraire affichez « Manche perdue ».
    # Pour répondre à cette question différentes syntaxes sont possibles.
    # CAS 1 : Le joueur a un AS
    # CAS 2 : Le joueur a un Roi et l'ordinateur n'a pas d'AS
    # CAS 3 : Le joueur a une Dame et l'ordinateur n'a pas d'As ni de Roi
    # CAS 4 : Le joueur a un Valet et l'ordinateur n'a pas d'As ni de Roi, ni de Dame
    # CAS 5 : La carte du joueur est plus forte que la carte de l'ordinateur
    # Syntaxe 1
    elif value_player_card == "As" or (value_player_card == "Roi" and value_computer_card != "As") or (value_player_card == "Dame" and value_computer_card != "As" and value_computer_card != "Roi") or (value_player_card == "Valet" and value_computer_card != "As" and value_computer_card != "Roi" and value_computer_card != "Dame") or value_player_card > value_computer_card:
        print("Manche remportée")
        # EXERCICE 3 : 5. Victoire du joueur : ajouter les valeurs des listes « lst_player_cards_playing » et « lst_computer_cards_playing »
        # à la liste « lst_player_cards » et videz les listes « lst_player_cards_playing » et « lst_computer_cards_playing »
        lst_player_cards = lst_player_cards + lst_player_cards_playing + lst_computer_cards_playing
        # print(lst_player_cards)
        lst_player_cards_playing = []
        lst_computer_cards_playing = []
    # Syntaxe 2
    # elif value_player_card == "As":
    #     print("Manche remportée")
    # elif value_player_card == "Roi" and value_computer_card != "As":
    #         print("Manche remportée")
    # elif value_player_card == "Dame" and value_computer_card != "As" and value_computer_card != "Roi":
    #     print("Manche remportée")
    # elif value_player_card == "Valet" and value_computer_card != "As" and value_computer_card != "Roi" and value_computer_card != "Dame":
    #     print("Manche remportée")
    # elif value_player_card > value_computer_card:
    #     print("Manche remportée")
    else:
        print("Manche perdue")
        # EXERCICE 3 : 5. Défaite du joueur : ajouter les valeurs des listes « lst_player_cards_playing » et « lst_computer_cards_playing » à la liste « lst_computer_cards »
        # et videz les listes « lst_player_cards_playing » et « lst_computer_cards_playing »
        lst_computer_cards = lst_computer_cards + lst_player_cards_playing + lst_computer_cards_playing
        # print("lst_computer_cards : ", lst_computer_cards)
        lst_player_cards_playing = []
        lst_computer_cards_playing = []

    input_abandon = int(input("Souhaitez-vous abandonner la partie (0:Non / 1:Oui) ? "))

# EXERCICE 4 : 1. Ecrivez un test qui affichera « Vous avez gagné la partie » ou « Vous avez perdu la partie » en fonction de conditions que vous aurez vous-même réfléchies.
if len(lst_player_cards) == 0 or input_abandon == 1:
    print("Vous avez perdu la partie")
else:
    print("Vous avez gagné la partie")