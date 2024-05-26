# -*- coding: utf-8 -*-
"""
Projet Fin d'Année
Atig Tasnim
Ben Mansour Youssef
Bowé Romain
Pochic Arthur
"""
#####################################"Définitions###################################################

#Définitions des classes utiles pour notre solution en respectant le diagramme UML

from abc import ABC, abstractmethod
from enum import Enum

class Filiere(Enum):
    MI = "Math/Info"
    MF = "Math/Finance"
    GI = "Génie Informatique"

    def __str__(self):
        return self.value

class Personne(ABC):
    def __init__(self, nom, prénom):
        self.nom = nom
        self.prénom = prénom

class Admin(Personne):
    def __init__(self, nom, prénom, idAdmin, mdpAdmin):
        super().__init__(nom, prénom)
        self.idAdmin = idAdmin
        self.mdpAdmin = mdpAdmin
        self.remplissage_active = False

    def activerRemplissage(self):
        self.remplissage_active = True
        print("Remplissage activé.")

    def désactiverRemplissage(self):
        self.remplissage_active = False
        print("Remplissage désactivé.")

    def lancerOperationOrientation(self):
        print("Opération d'orientation lancée.")

    def genererStat(self):
        print("Statistiques générées.")

class Etudiant(Personne):
    def __init__(self, nom, prénom, numEtudiant, mdp, filiere, moyenneGenerale):
        super().__init__(nom, prénom)
        self.numEtudiant = numEtudiant
        self.mdp = mdp
        self.filiere = filiere
        self.moyenneGenerale = moyenneGenerale
        self.notes = {}
        self.orientationFinale = None

    def remplirFicheVoeux(self):
        if Admin.remplissage_active == False:
            print("Vous ne pouvez pas encore remlpir la fiche de voeux.")
        else:
            print("Fiche de voeux remplie.")

    def confirmerFicheVoeux(self):
        print("Fiche de voeux confirmée.")

    def consulterResultats(self):
        print("Résultats consultés")
    
    def ajouter_note(self, matiere, note):
        self.notes[matiere] = note

class Option:
    def __init__(self, idOption, intitule, description, isOptionMF, isOptionMI, isOptionGI, nbPlaces):
        self.idOption = idOption
        self.intitule = intitule
        self.description = description
        self.isOptionMF = isOptionMF
        self.isOptionMI = isOptionMI
        self.isOptionGI = isOptionGI
        self.nbPlaces = nbPlaces

class FicheVoeux:
    def __init__(self, etudiant, choix1, choix2, choix3,choix4, choix5):
        self.etudiant = etudiant
        self.choix1 = choix1
        self.choix2 = choix2
        self.choix3 = choix3
        self.choix4 = choix4
        self.choix5 = choix5

    def __init__(self, etudiant, choix1, choix2):
        self.etudiant = etudiant
        self.choix1 = choix1
        self.choix2 = choix2

    def __init__(self, etudiant, choix1, choix2, choix3,choix4):
        self.etudiant = etudiant
        self.choix1 = choix1
        self.choix2 = choix2
        self.choix3 = choix3
        self.choix4 = choix4


class Resultats:
    def __init__(self, etudiant, optionRetenue):
        self.etudiant = etudiant
        self.optionRetenue = optionRetenue
        self.etudiant.orientationFinale = optionRetenue

class Statistiques:
    def __init__(self, optionPlusSollicitee1, optionPlusSollicitee2, optionPlusSollicitee3,
                 pourcentagePremierChoix, pourcentageDeuxiemeChoix, pourcentageTroisiemeChoix):
        self.optionPlusSollicitee1 = optionPlusSollicitee1
        self.optionPlusSollicitee2 = optionPlusSollicitee2
        self.optionPlusSollicitee3 = optionPlusSollicitee3
        self.pourcentagePremierChoix = pourcentagePremierChoix
        self.pourcentageDeuxiemeChoix = pourcentageDeuxiemeChoix
        self.pourcentageTroisiemeChoix = pourcentageTroisiemeChoix

    def afficher_statistiques(self):
        print("Options les plus sollicitées :")
        print("1ère Option la plus sollicitée :")
        self.optionPlusSollicitee1.afficher_info()
        print("2ème Option la plus sollicitée :")
        self.optionPlusSollicitee2.afficher_info()
        print("3ème Option la plus sollicitée :")
        self.optionPlusSollicitee3.afficher_info()
        print(f"Pourcentage de premiers choix retenus: {self.pourcentagePremierChoix}%")
        print(f"Pourcentage de deuxièmes choix retenus: {self.pourcentageDeuxiemeChoix}%")
        print(f"Pourcentage de troisième choix retenus: {self.pourcentageTroisiemeChoix}%")

#Définition de la méthode du calcul du score selon la filière en ING2

def calculer_score(etudiant, option):
    score=0
    if etudiant.filiere == "MI":
        score += 4.5*etudiant.notes["Data Mining 2"] + 5*etudiant.notes["IA:application"] + 2.5*etudiant.notes["Compressive Sensing"] + 2*etudiant.notes["Introduction Séries Temporelles"] + 3*etudiant.notes["Décidabilité et complexité"] + 3*etudiant.notes["Architecture et Programmation Parallèle"]
    elif etudiant.filiere == "MF":
        score += 4.5*etudiant.notes["Contingent Claims Valuation"] + 3.5*etudiant.notes["Proba"] + 3*etudiant.notes["Introduction à la finance"] + 3*etudiant.notes["Méthodes Num Av pour EDP"] + 2.5*etudiant.notes["Equations aux dérivées partielles"] + 2*etudiant.notes["Portfolio Management & financial risks"] + 1.5*etudiant.notes["Intro à l'assurance"]
    else:
        score += 4.5*etudiant.notes["IA:théories et algorithmes"] + 3*etudiant.notes["IA:applications"] + 3*etudiant.notes["Cybersécurité opérations"] + 3*etudiant.notes["Architecture Réseaux"] + 1.5*etudiant.notes["Programmation fonctionnelle"] + 2.5*etudiant.notes["Architecture et Programmation parallèle"] + 2.5*etudiant.notes["Développement distribué Java EE"]
    return score

################################## Solution algorithmique et résultats d'affectation #####################################

#Import du jeu de données et entraînement des arbres de décision par filière de ING2
"""
Veuillez installez ces bibliothèques python à l'aide de la commande pip pour une bonne exécution
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import tabula

"""
Commençons par les classes de MI
"""

# Lire le fichier PDF de la filière MI et le convertir en DataFrame
file_path = "../Annexes/jeu_donnees_MI.pdf"
tablesMI = tabula.read_pdf(file_path, pages='1,2')
dataMI = tablesMI[0]

# Vérifier les noms des colonnes
#print(data.columns)

# Renommer les colonnes si nécessaire
dataMI.columns = ['Identifiant', 'Nom', 'Prenom','Moyenne', 'Score', 'Affectation']

# Afficher les premières lignes du dataframe pour vérifier la lecture du fichier
#print(data.head())

# Préparer les données
X_MI = dataMI[['Moyenne', 'Score']]
y_MI = dataMI['Affectation']


# Créer l'arbre de décision en utilisant la base d'apprentissage pour la filière de MI
clf_MI = DecisionTreeClassifier(random_state=42)
clf_MI.fit(X_MI, y_MI)

# Évaluer le modèle
#score = clf_MI.score(X_test, y_test)
#print(f"Accuracy: {score}")

# Visualiser l'arbre de décision
#plt.figure(figsize=(10,10))
#tree.plot_tree(clf_MI, feature_names=['Moyenne', 'Score'], class_names=clf_MI.classes_, filled=True)
#plt.title("Arbre de décision pour prédire la Filiere")
#plt.show()

"""
Commençons par les classes de MF
"""

# Lire le fichier PDF de la filière MF et le convertir en DataFrame
file_path = "../Annexes/jeu_donnees_MF.pdf"
tablesMF = tabula.read_pdf(file_path, pages='1,2')
dataMF = tablesMI[0]

# Vérifier les noms des colonnes
#print(data.columns)

# Renommer les colonnes si nécessaire
dataMF.columns = ['Identifiant', 'Nom', 'Prenom','Moyenne', 'Score', 'Affectation']

# Afficher les premières lignes du dataframe pour vérifier la lecture du fichier
#print(data.head())

# Préparer les données
X_MF = dataMF[['Moyenne', 'Score']]
y_MF = dataMF['Affectation']

# Créer l'arbre de décision pour la filière de MI
clf_MF = DecisionTreeClassifier(random_state=42)
clf_MF.fit(X_MF, y_MF)

"""
Commençons par les classes de GI
"""

# Lire le fichier PDF de la filière MF et le convertir en DataFrame
file_path = "../Annexes/jeu_donnees_GI.pdf"
tablesGI = tabula.read_pdf(file_path, pages='1,2')
dataGI = tablesGI[0]

# Vérifier les noms des colonnes
#print(data.columns)

# Renommer les colonnes si nécessaire
dataGI.columns = ['Identifiant', 'Nom', 'Prenom','Moyenne', 'Score', 'Affectation']

# Afficher les premières lignes du dataframe pour vérifier la lecture du fichier
#print(data.head())

# Préparer les données
X_GI = dataGI[['Moyenne', 'Score']]
y_GI = dataGI['Affectation']

# Créer l'arbre de décision pour la filière de MI
clf_GI = DecisionTreeClassifier(random_state=42)
clf_GI.fit(X_GI, y_GI)
