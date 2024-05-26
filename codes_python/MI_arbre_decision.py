import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import tabula

# Lire le fichier PDF et convertir en DataFrame
file_path = "../Annexes/jeu_donnees_MI.pdf"
tables = tabula.read_pdf(file_path, pages='1,2')
data = tables[0]

# Vérifier les noms des colonnes
print(data.columns)

# Renommer les colonnes si nécessaire
data.columns = ['Identifiant', 'Nom', 'Prenom','Moyenne', 'Score', 'Affectation']

# Afficher les premières lignes du dataframe pour vérifier la lecture du fichier
print(data.head())

# Préparer les données
X = data[['Moyenne', 'Score']]
y = data['Affectation']

# Diviser les données en ensembles d'entraînement et de test
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer l'arbre de décision
clf_MI = DecisionTreeClassifier(random_state=42)
clf_MI.fit(X, y)

# Évaluer le modèle
#score = clf.score(X_test, y_test)
#print(f"Accuracy: {score}")

# Visualiser l'arbre de décision
plt.figure(figsize=(10,10))
tree.plot_tree(clf_MI, feature_names=['Moyenne', 'Score'], class_names=clf_MI.classes_, filled=True)
plt.title("Arbre de décision pour prédire la Filiere")
plt.show()
