
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


