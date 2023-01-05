
import random,math,time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator


"""
Programe simulant le nombre d'achats moyen nécessaire pour completée une collection de n elements

#IMPORTANT: Par defaut VSCode ne vient pas avec les bibliotheques necesaire pour les graphs, le plus ismple est d'utiliser l'editeur "Spyder" qui a les bibliotheques requise de prés installer
"""


#fonction creant une liste contenant de 1 au nombre totale de carte dans la colection
def deck(tcollection):
    collection = []
    for i in range(tcollection):
            collection.append(i+1)
    return collection


#fonction tirant un nombre aléatoire("une carte") de 1 au nombre totale de carte dans la collection
def carte_random(tcollection,doublons,carte_tire):
    carte = -1
    #si on peut avoir des doublons dans chaque achat alor on tire un nombre aléatoire
    if(doublons == "oui"):
        carte = random.randrange(1,tcollection+1)

    #sinon on tire un nombre("une carte") qui n'est pas deja presente dans la liste carte_tire
    else:
        #tire une nouvelle carte si la carte tiré a deja etait tiré 
        while(carte in carte_tire or carte == -1):
            carte = random.randrange(1,tcollection+1)
    return carte


#fonction principale
def test(tcollection,nbr_carte,nbr_test):
    start_time = time.time()
    l_tour = [] #liste contenant tout les nombres d'achats nessesaire pour avoire la collection complete lors de tout les tests
    l_doublons = [] #liste contenant tout les doublons tirée
    max_tour = 0
    min_tour = 1000000

    #Boucle:Nombre de tests effectuer
    for i in range(nbr_test):
        nbr_tour = 0
        nbr_doublons = 0
        #creer une liste de 1 au nombre totale decarte dnas la collection
        collection = deck(tcollection)

        #Boucle:Tant Que la collection n'est pas complete
        while (len(collection) > 0):
            carte_tire = [] #liste contenant les cartes deja tirée lors de l'achat
            
            #tire les cartes obtenue a chaque achat
            for x in range(nbr_carte):
                carte = carte_random(tcollection,doublons,carte_tire)
                carte_tire.append(carte)

                #Boucle: Cherche si la carte obtenue est dans la liste collection et la suprime si elle est presente
                if(carte in collection):
                    collection.remove(carte)
                    
                else:
                    nbr_doublons = nbr_doublons + 1
                  
            nbr_tour += 1 
        l_doublons.append(nbr_doublons)        
        l_tour.append(nbr_tour)
        if(max_tour < nbr_tour):
            max_tour = nbr_tour
        if(min_tour > nbr_tour):
            min_tour = nbr_tour
        print("Test:",i +1,"/",nbr_test)

    moy_tour = sum(l_tour) / len(l_tour)
    moy_doublons = sum(l_doublons) / len(l_doublons)
    l_tour.sort()
    return moy_tour,moy_doublons,min_tour,max_tour,start_time,l_tour


#fonction utilisé pour les graphes, renvoie une liste contenant l'occurence du nombre de chaque tour ainsi qu une liste contenant le pourcentage de chaque occurence de nombre de tours
def pourcentage(l_tour):
    l_pourcentage = []
    l_occurence = []
    x = 1
    for i in range(len(l_tour)):
        if(i == len(l_tour)-1):
            l_pourcentage.append((x / len(l_tour))*100)
            l_occurence.append(x)
            x = 1
        else:
            if(l_tour[i] == l_tour[i+1]):
                x = x +1
            else:
                l_pourcentage.append((x / len(l_tour))*100)
                l_occurence.append(x)
                x = 1
    return l_pourcentage,l_occurence



def graph_occurence(l_tour,l_occurence,max_tour,min_theorique):
    l_tour = list(dict.fromkeys(l_tour))

    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.bar(l_tour,l_occurence, linewidth=1.5)
    ax.set(xticks=np.arange(min_theorique,max_tour+1,5))
    ax.set(yticks=np.arange(0,max(l_occurence),5))
    ax.locator_params(axis='x', nbins=20)
    ax.locator_params(axis='y', nbins=25)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.grid(True)
    ax.set_xlabel("Nombres d'achats")
    ax.set_ylabel("Occurence")
    ax.set_title("Occurence du nombres d'Achats")
    plt.show()



def graph_pourcentage(l_tour,l_pourcentage,max_tour,min_theorique):
    l_tour = list(dict.fromkeys(l_tour))
    l_pourcentage2 = []
    x = 0
    for i in range(len(l_pourcentage)):
        l_pourcentage2.append(l_pourcentage[i] + x)
        x = x + l_pourcentage[i]

    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(l_tour,l_pourcentage2, linewidth=2.0)
    ax.set(xticks=np.arange(min_theorique,max_tour+1,5))
    ax.set(yticks=([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.locator_params(axis='x', nbins=20)
    ax.grid(True)
    ax.set_xlabel("Nombres d'achats")
    ax.set_ylabel("Pourcentage")
    ax.set_title("Pourcentage de chance d'avoir toute la collection apres x achats")
    plt.show()



tcollection = int(input("Saisir le nombre totale de cartes dans la collection: "))
nbr_carte = int(input("Saisir le nombre de cartes obtenue a chaque achat: "))
doublons = str(input("Voulez vous avoir des doublons dans chaqu'un de ces achats ?:oui/non: "))
nbr_test = int(input("Saisir le nombre de tests a faire: "))
moy_tour,moy_doublons,min_tour,max_tour,start_time,l_tour = test(tcollection,nbr_carte,nbr_test)
min_theorique = math.ceil(tcollection / nbr_carte)

print("Il faudra en moyenne",math.ceil(moy_tour),"(",moy_tour,")","achats pour avoir la collection complete")
print("Le nombre de tours minimum a etait de:",min_tour,"tours")
print("Le nombre de tours maximum a etait de:",max_tour,"tours")
print("Le nombre minimum théorique d'achats est:",min_theorique)
print("Le nombre moyen de doublons a été de:",round(moy_doublons))
print("         Temp d'execution")
print("--- %s seconds ---" % (time.time() - start_time))

l_pourcentage,l_occurence = pourcentage(l_tour)
graph_occurence(l_tour,l_occurence,max_tour,min_theorique)
graph_pourcentage(l_tour,l_pourcentage,max_tour,min_theorique)

