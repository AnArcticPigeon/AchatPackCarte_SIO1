

import random,math,time

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator




def deck(tcollection):
    collection = []

    for i in range(tcollection):
            collection.append(i+1)

    return collection



def carte_random(tcollection,doublons,carte_tire):
    carte = -1

    if(doublons == "oui"):
        carte = random.randrange(1,tcollection+1)

    else:
        while(carte in carte_tire or carte == -1):
            carte = random.randrange(1,tcollection+1)
            
            
    return carte



def test(tcollection,nbr_carte,nbr_test):
    start_time = time.time()
    l_tour = []
    l_doublons = []
    max_tour = 0
    min_tour = 1000000

    #Boucle:Nombre de tests effectuer
    for i in range(nbr_test):
        nbr_tour = 0
        nbr_doublons = 0
        collection = deck(tcollection)

        #Boucle:Tant Que la collection n'est pas complete
        while (len(collection) > 0):
            #print(collection)
            carte_tire = []
            

            #Boucle: Nombre de carte obtenue a chaque achat
            for x in range(nbr_carte):
                carte = carte_random(tcollection,doublons,carte_tire)
                carte_tire.append(carte)
                #print("La carte",x +1,"sur",nbr_carte,"est la carte:",carte)

                #Cherche si la carte obtenue dans la collection et la suprime si elle est presente
                for c in collection:
                    if(c == carte):
                        collection.remove(carte)
                        break

                nbr_doublons = nbr_doublons + 1
            #print("liste des carte contenue dans le pack",carte_tire)
                  
            nbr_tour += 1 
        l_doublons.append(nbr_doublons)        
        l_tour.append(nbr_tour)
        if(max_tour < nbr_tour):
            max_tour = nbr_tour
        if(min_tour > nbr_tour):
            min_tour = nbr_tour
        #print("tour:",nbr_tour)
        print("test:",i +1,"/",nbr_test)

    moy_tour = sum(l_tour) / len(l_tour)
    moy_doublons = sum(l_doublons) / len(l_doublons)
    l_tour.sort()
    return moy_tour,moy_doublons,min_tour,max_tour,start_time,l_tour



def pourcentage(l_tour):
    l_pourcentage = []
    l_occurence = []
    #print(l_tour)
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
    ax.bar(l_tour,l_occurence, linewidth=2.0)
    ax.set(xticks=np.arange(min_theorique,max_tour+1,5))
    ax.set(yticks=np.arange(0,max(l_occurence),5))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlabel("Nombres d'achats")
    ax.set_ylabel("Occurence")
    ax.set_title("Occurence du nombres d'Achats")
    plt.show()



def graph_pourcentage(l_tour,l_pourcentage,max_tour,min_theorique):
    l_tour = list(dict.fromkeys(l_tour))

    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(l_tour,l_pourcentage, linewidth=2.0)
    ax.set(xticks=np.arange(min_theorique,max_tour+1,5))
    ax.set(yticks=np.arange(0,100,5))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlabel("Nombres d'achats")
    ax.set_ylabel("Pourcentage")
    ax.set_title("Occurence du nombres d'Achats")
    plt.show()


def graph_pourcentage2(l_tour,l_pourcentage,max_tour,min_theorique):
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
    ax.set(yticks=np.arange(0,100,5))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_xlabel("Nombres d'achats")
    ax.set_ylabel("Pourcentage")
    ax.set_title("Chance d'avoire une collection complete")
    plt.show()




doublons = str(input("Voulez vous avoir des doublons dans chaque packs ?:oui/non:"))
nbr_test = int(input("Saisir le nombre de test a faire:"))
tcollection = int(input("Saisir le nombre de carte dans la collection:"))
nbr_carte = int(input("Saisir le nombre de carte obtenue a chaque achat:"))
moy_tour,moy_doublons,min_tour,max_tour,start_time,l_tour = test(tcollection,nbr_carte,nbr_test)
min_theorique = math.ceil(tcollection / nbr_carte)

print("Il faudra en moyenne",round(moy_tour),"(",moy_tour,")","achats pour avoir la collection complete")
print("Le nombre de tours maximum a etait de:",max_tour,"tours")
print("Le nombre de tours minimum a etait de:",min_tour,"tours")
print("Le nombre minimum théorique d'achats est:",min_theorique)
print("Le nombre moyen de doublons a eté de:",round(moy_doublons))
print("--- %s seconds ---" % (time.time() - start_time))

l_pourcentage,l_occurence = pourcentage(l_tour)
#print(l_pourcentage)
print("la somme est:",sum(l_pourcentage))

graph_occurence(l_tour,l_occurence,max_tour,min_theorique)
graph_pourcentage2(l_tour,l_pourcentage,max_tour,min_theorique)

