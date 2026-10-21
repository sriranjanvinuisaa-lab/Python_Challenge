#####################  MODULE -- Partie 1 ######################  

########## Variables

PI = 3.14159
E = 2.718281828459045

########## Fonction

def carre(x):
    return x ** 2

def cube(x):
    return x ** 3

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)

def valeur_absolue(x):
    return abs(x)

def maximum(liste):
    return max(liste)
    
def minimum(liste):
    return min(liste)

def moyenne(liste):
    return sum(liste) / len(liste)      # len() : combien de valeurs / éléments il y a dans la liste

def mediane(liste):
    liste_triee = sorted(liste)         # sorted() : trie les éléments par ordre croissant ou alphabétique
    n = len(liste_triee)
    med = n // 2

    if n % 2 == 1:
        return liste_triee[med]
    else:
        return (liste_triee[med - 1] + liste_triee[med]) / 2

def ecart_type(liste):
    moy = moyenne(liste)
    variance = sum((x - moy) ** 2 for x in liste) / len(liste)
    return variance ** 0.5



#####################  MODULE -- Partie 2 ######################  

# Fonction "somme_cumulee" qui contient un paramètre "liste".
def somme_cumulee(liste):
    """
    Paramètre : (liste) une liste de nombres.
    Calcul de la somme cumulée des éléments d'une liste (Boucle for)
    Retour : Liste contenant les sommes cumulées successives : resultat
    """
    resultat = []           # initialisatin d'une liste vide "resultat"
    somme = 0               # Initailisation de la somme à 0

    for x in liste:                  # Pour x dans la liste de la fonction "somme_cumulee"
        somme += x                   # Somme de x 
        resultat.append(somme)       # Ajout de la somme à la fin de la liste "résultat"

    return resultat 



# Fonction "compter_occurrences" qui contient un paramètre "liste".
def compter_occurrences(liste):
    """
    Paramètre : liste : une liste d'éléments à compter.
    Compte le nombre d'occurrences de chaque élément d'une liste (Boucle for avec la méthode set())
    Retour : Un dictionnaire associant chaque élément à son nombre d'occurrences.
    """
    return {x: liste.count(x) for x in set(liste)}      # Retourne : Valeur x et son nombre d'occurence.
                                                        # set() permet d'avoir des éléments sans doublons



# Fonction "inverser_dict" qui contient un paramètre "dictionnaire".
def inverser_dict(dictionnaire):
    """
    Paramètre : dictionnaire : le dictionnaire à inverser.
    Inverse les clés et les valeurs d'un dictionnaire.
    Retour : Un nouveau dictionnaire avec les clés et les valeurs inversées.
    """
    return {valeur: cle for cle, valeur in dictionnaire.items()}           # retourne l'inverse de clé et valeur donc valeur et clé.
                                                                           # items() permet de parcourir les paires clé-valeur 



# Fonction "filtrer_pairs" qui contient un paramètre "liste".
def filtrer_pairs(liste):
    """
    Paramètre : liste : liste à flitrer.
    Nouvelle liste contenant uniquemment les nombres pairs. 
    Retour : Liste contenant uniquemment les nombres pairs.
    """
    resultat_pairs = []                  # Initialisation d'une liste vide "resultat_pairs" (nouvelle liste)
    
    for x in liste:                       # Pour valeur x de la liste 
        if x % 2 == 0:                     # Vérifie si x est pair 
            resultat_pairs.append(x)        # Ajout de la valeur x pair dans la nouvelle liste 

    return resultat_pairs                     # Reourne la nouvelle liste




# Fonction "celsius_to_fahrenheit" qui contient un paramètre "celsius".
def celsius_to_fahrenheit(celsius):
    """
    Paramètre : celsius, la tmpérature en degré Celsius.
    Calcul pour convertir une température en degrés Celsius en Fahrenheit.
    """
    f = (celsius * 9/5) + 32        # Calcul de Fahrenheit

    return f                        # Retourne F (Fahrenheit)




# Fonction "trouver_doublons" qui contient un paramètre "liste".
def trouver_doublons(liste):
    """
    Parametre : liste, à examiner.
    Obj : Retourner les éléments qui apparaissent plusieurs fois dans la liste.
    Retour : Une liste contenant les éléments en double.
    """
    doublons = []               # Initialisation d'une liste vide "doublons" 

    for x in set(liste):             # Pour x, valeur unique de la liste "liste"
        if liste.count(x) > 1:       # Si le nombre de x apparait plusieurs fois dans la liste "liste" 
            doublons.append(x)       # Ajout de la valeur x dans la nouvelle liste "doublons"
            
    return doublons                   # Retourne la nouvelle liste



# calculer_moyenne_ponderee(valeurs, poids)
def calculer_moyenne_ponderee(valeurs, poids):
    """
    Calcule la moyenne pondérée d'une liste de valeurs.
    Paramètre 1 : valeurs, une liste de nombres.
    Paramètre 2 : poids, une liste de poids correspondants.
    Retour : Un nombre représentant la moyenne pondérée.
    """

    total = 0               # initialisation : somme des valeurs multipliées par leur poids
    total_poids = 0         # initialisation : somme des poids 

    for i in range(len(valeurs)):           # i parcours les indices (index) de la liste "valeurs"
        total += valeurs[i] * poids[i]      # multiplie chaque valeur par le poids situé au même index
        total_poids += poids[i]             

    return total / total_poids              # moyenne pondérée


# calculer_moyenne_ponderee(valeurs, poids) : version plus simple
def calculer_moyenne_ponderee_2(valeurs, poids):
    return sum(v * p for v, p in zip(valeurs, poids)) / sum(poids)



################## Partie Bonus ##########################

def analyser_texte(texte):
    mots = texte.split()                             # sépare la phrase en mots

    nb_total_mots = len(mots)                        # compte le nombre total de mots

    nb_caract = len(texte)                           # compte le nombre total de caractères dans la texte

    nb_caract_sans_sp = len(texte) - texte.count(" ")   # compte le nombre total de caractères sans espace dans le texte

    mots_long =  max(mots, key=len)                  # cherche le mot qui a le plus de caractères


    total = 0
    for mot in mots:                                 
        total += len(mot)
    if nb_total_mots > 0:
        moyenne = total / nb_total_mots
    else:
        moyenne = 0


    # dictionnaire des résultats
    resultat = {
        "nombre total de mots": nb_total_mots,
        "nombre de caractères (espaces inclus)": nb_caract,
        "nombre de caractères (espaces exclus)": nb_caract_sans_sp,
        "Mot le plus long": mots_long,
        "Longueur moyenne des mots": moyenne
        }

    return resultat
    
