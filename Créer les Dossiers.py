import random
import os
import numpy as np
os.chdir(r"C:\Users\maroc\Desktop\ECOLE\nsi-tp master\NSI-TP-master\Exercice Parcours en Largeur")
root = os.getcwd() #Naviguer avant de lancer le programme sinon ça va envahir votre dossier utilisateur

File = []
Compteur = 0
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Liste = []

def MkDos(p,v,path): #path chemin dossier, p proba de créer un dossier
    global File,Compteur,Liste
    os.chdir(path)
    u = random.random()
    v = random.random()
    while u<p:
        print("Création")
        os.mkdir(str(Compteur))
        os.chdir(str(Compteur))
        # Ajouter ouvrir document avec proba v et écrire Alphabet[compteur%26]
        if random.random()<p:
            with open("text.txt","w+") as file:
                file.write(Alphabet[Compteur%26])
                Liste.append(Alphabet[Compteur%26])
        temp_path = os.getcwd()
        File.append(temp_path)
        os.chdir("..")
        u = random.random()
        Compteur +=1
    os.chdir(root)


def Boucle(v,p,t): #p proba initiale, t taux de décroissance
    global File,Compteur,Liste
    MkDos(v,p,root)
    while len(File)>0:
        pathDos = File.pop(0)
        p = max(0, p*np.exp(-t*Compteur))
        print(len(File))
        MkDos(p,v,pathDos)


#Enlever le commentaire de la ligne suivante et lancer la Fonction Boucle.

#Boucle(0.5,0.9,0.000001)


