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



######################################## Test de prédiction et algorithme de Gale&Shapley ##################################################
# Lire le fichier PDF test de la filière MI et le convertir en DataFrame
import pandas as pd
file_path = "../Annexes/jeu_donnees_final.xlsx"
feuille="test GMI"
data_testMI = pd.read_excel(file_path, sheet_name=feuille)

#Id_liste=[i for i in range(10000051,10000061)]
#Nom_liste=[Breton,Remy,Collin,Julien,Baron,Denis,Simone,Aubert,Roy,Dupuy,Millet]
#prenom_liste=[Félix,Alice,Thomas,Mia,Nathan,Logan,Sophia,William,Jacob,Amélia,Florence]
#moy_liste=[12.95833333,13.54166667,14.33333333,13.95833333,13.75,11.41666667,16.5,16.5,13.66666667,12.70833333,12.125]
#score_liste=[262.45,281.75,290.75,283,270.5,231.75,339.25,331.5,269.75,248.5,249.875]
'''Affectation=[None]*10
voeux=[
data_testMI={'Identifiant': [1, 2, 3, 4, 5],
        'Nom': ['A', 'B', 'C', 'D', 'E'],
        'Prenom': ['X', 'Y', 'Z', 'W', 'V'],
        'Moyenne': [15, 12, 14, 13, 16],
        'Score': [0.8, 0.6, 0.75, 0.7, 0.85],
        'Liste_de_voeux': ['Option1', 'Option2', 'Option3', 'Option4', 'Option5']}'''

print(data_testMI.columns)
print(data_testMI)
Xtest_MI=data_testMI.filter(regex='%e')
data_testMI['Affectation_Predite'] = clf_MI.predict(Xtest_MI)

# Ajouter une colonne vide 'Liste de voeux'
#data_testMI['Liste de voeux'] = None

# Maintenant, vous pouvez définir les noms des colonnes avec 7 noms
#data_testMI.columns = ['Identifiant', 'Nom', 'Prenom', 'Moyenne', 'Score', 'Affectation_Predite', 'Liste de voeux']


# Regrouper les étudiants par affectation prédite et trier par score
grouped = data_testMI.groupby('Affectation_Predite').apply(lambda x: x.sort_values(by='Score', ascending=False))

options_preferences = {}
for option, group in grouped.groupby('Affectation_Predite'):
    options_preferences[option] = group['Identifiant'].tolist()

# Exemple de préférences des étudiants (à adapter selon vos données)
students_preferences = {
    row['Identifiant']: row[['Liste de voeux']] for idx, row in data_testMI.iterrows()
}
# Capacité des options (exemple)
options_capacity = {
    'IA': 3,
    'DS': 3,
    'Fintech': 2,
    'BI': 2
}
def gale_shapley_inverse(students_preferences, options_capacity):
    # Initialiser les listes de préférence inversées pour un accès rapide
    rank = {
        student: {option: rank for rank, option in enumerate(prefs)}
        for student, prefs in students_preferences.items()
    }

    # Les listes d'options non appariées
    free_options = list(options_capacity.keys())

    # Initialiser les appariements vides pour chaque option
    matches = {student: [] for student in students_preferences.keys()}

    # Pointeurs pour suivre les propositions faites par chaque option
    option_proposals = {option: 0 for option in options_capacity.keys()}

    while free_options:
        option = free_options.pop(0)
        option_pref_list = list(students_preferences.keys())

        # Propose aux étudiants selon les préférences jusqu'à remplir les capacités
        for _ in range(options_capacity[option]):
            if option_proposals[option] < len(option_pref_list):
                student = option_pref_list[option_proposals[option]]
                option_proposals[option] += 1

                # Ajoutez l'option à la liste des appariements de l'élève
                matches[student].append(option)

                # Vérifiez si l'option a atteint sa capacité maximale
                if len(matches[student]) >= options_capacity[option]:
                    free_options.remove(option)

    return matches

# Appeler la fonction avec les données
matches = gale_shapley_inverse(students_preferences, options_capacity)

# Afficher les appariements
for student, options in matches.items():
    print(f"Étudiant {student}: Options {options}")
