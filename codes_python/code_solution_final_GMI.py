import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree

file_path = "../Annexes/jeu_donnees.xlsx"
feuille = "MI"
data = pd.read_excel(file_path, sheet_name=feuille)

print("Colonnes du DataFrame:", data.columns)

# Supprimer les espaces supplémentaires dans les noms de colonnes
data.columns = data.columns.str.strip()

# Vérifier les lignes contenant des valeurs manquantes dans Affectation_Predite
print("Lignes avec des valeurs manquantes dans 'Affectation':")
print(data[data['Affectation'].isna()])

# Remplir les valeurs manquantes dans Affectation_Predite avec des valeurs aléatoires parmi les options disponibles
options = ['IA', 'DS', 'Fintech', 'BI']
#data['Affectation_Predite'] = data['Affectation_Predite'].fillna(pd.Series(np.random.choice(options, len(data))))

feature_columns = ['Moyenne', 'Score']  # Colonnes utilisées pour l'entraînement du modèle

# Vérifier si les colonnes existent dans le DataFrame
missing_columns = [col for col in feature_columns if col not in data.columns]
if missing_columns:
    raise KeyError(f"Les colonnes suivantes sont manquantes dans le DataFrame: {missing_columns}")

X = data[feature_columns]
y = data['Affectation']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)

# Entraîner le modèle
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

plt.figure(figsize=(10,10))
tree.plot_tree(clf, feature_names=['Moyenne', 'Score'], class_names=clf.classes_, filled=True)
plt.title("Arbre de décision pour prédire la Filiere pour les étudiants en GMI")
plt.show()

file_path = "../Annexes/jeu_donnees_final.xlsx"
feuille = "test GMI"
data_testMI = pd.read_excel(file_path, sheet_name=feuille)


data_testMI.columns = data_testMI.columns.str.strip()  # Supprimer les espaces supplémentaires

Xtest_MI = data_testMI[feature_columns]
print(clf)
data_testMI['Affectation_Predite'] = clf.fit(X_train, y_train).predict(Xtest_MI)


# Ajouter une colonne vide 'Liste de voeux' pour les besoins de la simulation
data_testMI['Liste_de_voeux'] = ['DS,IA,BI,Fintech', 'DS,IA,BI,Fintech', 'DS,IA,BI,Fintech', 
                                 'IA,BI,DS,Fintech', 'Fintech,BI,DS,IA', 'DS,IA,BI,Fintech', 
                                 'IA,DS,Fintech,BI', 'IA,DS,Fintech,BI', 'DS,IA,BI,Fintech', 
                                 'DS,Fintech,BI,IA', 'IA,BI,DS,Fintech']

print("\n le résultat de la prédiction:")
print(data_testMI[['Identifiant','Affectation_Predite','Liste_de_voeux']])

# Conversion des listes de voeux en format exploitable
data_testMI['Liste_de_voeux'] = data_testMI['Liste_de_voeux'].apply(lambda x: x.split(','))

# Capacité des options
options_capacity = {
    'IA': 3,
    'DS': 3,
    'Fintech': 3,
    'BI': 2
}
options_places = {
    'IA': 0,
    'DS': 0,
    'Fintech': 0,
    'BI': 0
}

# Préparation des préférences des étudiants et des options
students_preferences = {
    row['Identifiant']: row['Liste_de_voeux']
    for idx, row in data_testMI.iterrows()
}

# Préparation des préférences inversées des options
options_preferences = {option: [] for option in options_capacity.keys()}
for student, preferences in students_preferences.items():
    for preference in preferences:
        options_preferences[preference].append(student)

def gale_shapley(students_preferences, options_preferences, options_capacity):
    # Initialiser les listes de préférence inversées pour un accès rapide
    rank = {
        student: {option: rank for rank, option in enumerate(prefs)}
        for student, prefs in students_preferences.items()
    }

    # Les listes d'options non appariées
    free_options = list(options_preferences.keys())
    
    # Initialiser les appariements vides pour chaque étudiant
    matches = {student: None for student in students_preferences.keys()}

    # Pointeurs pour suivre les propositions faites par chaque option
    option_proposals = {option: 0 for option in options_preferences.keys()}

    # Organiser les résultats par option en respectant les capacités
    option_to_students = {option: [] for option in options_capacity.keys()}

    # Propose aux étudiants selon les préférences jusqu'à remplir les capacités
    while free_options:
        option = free_options.pop(0)
        option_pref_list = options_preferences[option]

        while len(option_to_students[option]) < options_capacity[option] and option_proposals[option] < len(option_pref_list):
            student = option_pref_list[option_proposals[option]]
            option_proposals[option] += 1

            if matches[student] is None:
                matches[student] = option
                option_to_students[option].append(student)
            else:
                current_option = matches[student]
                if rank[student][option] < rank[student][current_option]:
                    matches[student] = option
                    option_to_students[current_option].remove(student)
                    option_to_students[option].append(student)
                    if current_option not in free_options:
                        free_options.append(current_option)

    # Assurer que chaque filière est remplie à sa capacité maximale
    for option, students in option_to_students.items():
        if len(students) > options_capacity[option]:
            excess_students = students[options_capacity[option]:]
            option_to_students[option] = students[:options_capacity[option]]
            for ex_student in excess_students:
                matches[ex_student] = None
    
    # Réaffecter les étudiants non assignés aux options non remplies
    unassigned_students = [student for student, assigned in matches.items() if assigned is None]
    for option, students in option_to_students.items():
        while len(students) < options_capacity[option] and unassigned_students:
            student = unassigned_students.pop(0)
            option_to_students[option].append(student)
            matches[student] = option

    return option_to_students

# Appeler la fonction avec les données
matches = gale_shapley(students_preferences, options_preferences, options_capacity)

# Afficher les appariements
for option, students in matches.items():
    print(f"{option}: {students}")

import csv

def save_matches_to_csv(matches, filename):
     with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Filière', 'Etudiants_orientés'])
        for option, students in matches.items():
            # Convertir chaque étudiant en chaîne de caractères avant de joindre
            students_str = [str(student) for student in students]
            writer.writerow([option, ', '.join(students_str)])

save_matches_to_csv(matches, 'resultats_orientation_GMI.csv')


# Calculer les pourcentages des étudiants affectés à leur n-ème choix
def calculate_choice_statistics(students_preferences, matches):
    choice_ranks = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    total_students = len(students_preferences)
    
    for option, students in matches.items():
        for student in students:
            prefs = students_preferences[student]
            rank = prefs.index(option) + 1  # Index + 1 pour obtenir un rang basé sur 1
            if rank in choice_ranks:
                choice_ranks[rank] += 1

    choice_percentages = {rank: (count / total_students) * 100 for rank, count in choice_ranks.items()}

    return choice_percentages

# Calculer la popularité des options dans les listes de voeux
def calculate_first_choice_popularity(students_preferences):
    first_choice_counts = {option: 0 for option in ['IA', 'DS', 'Fintech', 'BI']}
    for prefs in students_preferences.values():
        first_choice = prefs[0]
        first_choice_counts[first_choice] += 1

    total_first_choices = sum(first_choice_counts.values())
    first_choice_percentages = {option: (count / total_first_choices) * 100 for option, count in first_choice_counts.items()}

    return first_choice_percentages

# Appeler les fonctions pour obtenir les statistiques
choice_stats = calculate_choice_statistics(students_preferences, matches)
first_choice_popularity = calculate_first_choice_popularity(students_preferences)

# Afficher les résultats
print("\nPourcentage des étudiants affectés à leur choix:")
for rank, percentage in choice_stats.items():
    print(f"Choix {rank}: {percentage:.2f}%")

print("\nPopularité des options dans les premiers choix:")
for option, percentage in first_choice_popularity.items():
    print(f"{option}: {percentage:.2f}%")

print(first_choice_popularity)

# Créer un histogramme pour visualiser les résultats
plt.figure(figsize=(10, 6))


for option in first_choice_popularity :
    bars=plt.bar(option, first_choice_popularity[option], color='green')
# Ajouter des annotations pour chaque barre
#for bar in bars:
    plt.text(option, first_choice_popularity[option] + 1, f'{first_choice_popularity[option]:.2f}%', ha='center', va='bottom')
    
plt.xlabel('Option')
plt.ylabel('Popularité (%)')
plt.title('Popularité des options dans les premiers choix pour les étudiants de la GMI')
plt.ylim(0, 100)
plt.show()

plt.figure(figsize=(10, 6))
for choix in choice_stats :
    plt.bar(choix, choice_stats[choix], color='blue')
    plt.text(choix, choice_stats[choix] + 1, f'{choice_stats[choix]:.2f}%', ha='center', va='bottom')
plt.xlabel('Choix')
plt.ylabel('Pourcentage')
plt.title("Pourcentage d'affectation en fonction du choix pour les étudiants de la GMI")
plt.ylim(0, 100)
plt.show()

