"""
═══════════════════════════════════════════════════════════════════════════════
            COLLECTION ET TRAITEMENT DE DONNÉES (DATA WRANGLING)
═══════════════════════════════════════════════════════════════════════════════

Apprenez à :
  1️⃣ Collecter les données (fichiers, APIs, web scraping)
  2️⃣ Nettoyer les données (valeurs manquantes, doublons)
  3️⃣ Transformer les données (normalisation, encoding)
  4️⃣ Explorer les données (EDA)
  5️⃣ Préparer pour le Machine Learning

Ce tutoriel couvre 80% du travail du data scientist !
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import io


# ═══════════════════════════════════════════════════════════════════════════════
# 1️⃣ COLLECTION DE DONNÉES
# ═══════════════════════════════════════════════════════════════════════════════

def collection_csv():
    """Charger des données depuis un fichier CSV"""
    print('\n' + '═' * 80)
    print('  1️⃣ COLLECTION - CHARGER UN FICHIER CSV')
    print('═' * 80)
    
    print('''
📂 FORMATS COURANTS :
  • CSV (Comma-Separated Values) - Format texte
  • Excel (.xlsx) - Feuilles de calcul
  • JSON - Données structurées
  • SQL - Bases de données
  • Parquet - Format binaire rapide
    ''')
    
    # Créer un petit CSV d'exemple
    csv_data = """id,nom,age,salaire,ville
1,Alice,28,3500,Paris
2,Bob,35,4200,Lyon
3,Charlie,26,3000,Marseille
4,Diana,32,4500,Paris
5,Etienne,29,3800,Toulouse
"""
    
    # Charger depuis string
    print('\n🚀 Chargement du CSV...')
    df = pd.read_csv(io.StringIO(csv_data))
    
    print(f'✅ Données chargées : {len(df)} lignes, {len(df.columns)} colonnes')
    print('\n📊 Aperçu des données :')
    print(df.to_string())
    
    return df


def collection_excel():
    """Charger depuis Excel"""
    print('\n' + '═' * 80)
    print('  2️⃣ COLLECTION - CHARGER UN FICHIER EXCEL')
    print('═' * 80)
    
    print('''
📈 EXCEL AVEC PANDAS :
  df = pd.read_excel('fichier.xlsx')
  df = pd.read_excel('fichier.xlsx', sheet_name='Feuille1')
  df = pd.read_excel('fichier.xlsx', skiprows=2)  # Ignorer premières lignes
    ''')


def collection_api():
    """Récupérer depuis une API"""
    print('\n' + '═' * 80)
    print('  3️⃣ COLLECTION - RÉCUPÉRER DEPUIS UNE API')
    print('═' * 80)
    
    print('''
🌐 EXEMPLE AVEC API PUBLIC :
  
  import requests
  
  # API gratuite de météo
  url = 'https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522'
  response = requests.get(url)
  data = response.json()
  df = pd.DataFrame(data)

📌 ÉTAPES :
  1. Faire la requête GET
  2. Vérifier le statut (200 = OK)
  3. Parser le JSON
  4. Convertir en DataFrame
  5. Nettoyer et explorer

💡 APIs POPULAIRES GRATUITES :
  • OpenWeatherMap - Météo
  • JSONPlaceholder - Données de test
  • PokéAPI - Pokémon
  • GitHub API - Données GitHub
  • CoinGecko - Cryptomonnaies
    ''')


def collection_web_scraping():
    """Web scraping avec BeautifulSoup"""
    print('\n' + '═' * 80)
    print('  4️⃣ COLLECTION - WEB SCRAPING')
    print('═' * 80)
    
    print('''
🕷️ WEB SCRAPING AVEC BEAUTIFULSOUP :

  from bs4 import BeautifulSoup
  import requests
  
  # Télécharger le HTML
  url = 'https://example.com'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  
  # Extraire les données
  titles = soup.find_all('h2')
  for title in titles:
      print(title.text)

⚠️ IMPORTANT :
  • Respecter robots.txt
  • Utiliser un délai entre les requêtes (time.sleep)
  • Lire les conditions d'utilisation
  • Utiliser des User-Agent

📚 SÉLECTEURS CSS :
  • soup.select('.class-name')  # Par classe
  • soup.select('#id')           # Par ID
  • soup.select('div > p')       # Par structure
    ''')


# ═══════════════════════════════════════════════════════════════════════════════
# 2️⃣ NETTOYAGE DE DONNÉES
# ═══════════════════════════════════════════════════════════════════════════════

def nettoyage_valeurs_manquantes():
    """Gérer les valeurs manquantes (NaN)"""
    print('\n' + '═' * 80)
    print('  5️⃣ NETTOYAGE - VALEURS MANQUANTES')
    print('═' * 80)
    
    print('''
❌ VALEURS MANQUANTES :
  • NaN (Not a Number)
  • Représentation : None, NaN, "", "NA"
  • Causes : Erreur de saisie, données non collectées, etc.

🔧 SOLUTIONS :
  1. Supprimer les lignes (si peu de données manquantes)
  2. Remplir avec une valeur par défaut
  3. Interpoler (pour séries temporelles) 
  4. Prédire avec un modèle
    ''')
    
    # Créer un dataset avec valeurs manquantes
    data = {
        'nom': ['Alice', 'Bob', None, 'Diana', 'Etienne'],
        'age': [28, np.nan, 26, 32, 29],
        'salaire': [3500, 4200, 3000, np.nan, 3800],
        'ville': ['Paris', 'Lyon', 'Marseille', 'Paris', None]
    }
    df = pd.DataFrame(data)
    
    print('\n📊 Données avec valeurs manquantes :')
    print(df.to_string())
    
    print(f'\n❌ Valeurs manquantes par colonne :')
    print(df.isnull().sum())
    
    # SOLUTION 1 : Supprimer les lignes avec NaN
    print('\n🔧 SOLUTION 1 : Supprimer les lignes')
    df_clean1 = df.dropna()
    print(f'   Avant : {len(df)} lignes → Après : {len(df_clean1)} lignes')
    
    # SOLUTION 2 : Remplir les valeurs manquantes
    print('\n🔧 SOLUTION 2 : Remplir les valeurs')
    df_clean2 = df.copy()
    df_clean2['age'].fillna(df_clean2['age'].mean(), inplace=True)  # Moyenne
    df_clean2['nom'].fillna('Inconnu', inplace=True)  # Valeur défaut
    print(df_clean2.to_string())
    
    # SOLUTION 3 : Interpoler (séries temporelles)
    print('\n🔧 SOLUTION 3 : Interpoler (séries temporelles)')
    df_clean3 = df.copy()
    df_clean3['age'] = df_clean3['age'].interpolate()
    print(df_clean3.to_string())


def nettoyage_doublons():
    """Supprimer les doublons"""
    print('\n' + '═' * 80)
    print('  6️⃣ NETTOYAGE - DOUBLONS')
    print('═' * 80)
    
    print('''
🔄 DOUBLONS :
  • Même données répétées
  • Problème : Fausse analyse, poids excessif

🔧 SOLUTIONS :
  • df.drop_duplicates() - Supprimer tous les doublons
  • df.drop_duplicates(subset=['colonne']) - Sur colonne spécifique
  • df.duplicated() - Identifier les doublons
    ''')
    
    # Créer un dataset avec doublons
    data = {
        'nom': ['Alice', 'Bob', 'Alice', 'Diana', 'Bob'],
        'age': [28, 35, 28, 32, 35],
        'ville': ['Paris', 'Lyon', 'Paris', 'Paris', 'Lyon']
    }
    df = pd.DataFrame(data)
    
    print('\n📊 Données avec doublons :')
    print(df.to_string())
    
    print(f'\n🔍 Doublons détectés : {df.duplicated().sum()}')
    
    # Supprimer les doublons
    df_clean = df.drop_duplicates()
    print(f'\n✅ Après suppression :')
    print(df_clean.to_string())


def nettoyage_outliers():
    """Détecter et traiter les outliers (valeurs aberrantes)"""
    print('\n' + '═' * 80)
    print('  7️⃣ NETTOYAGE - OUTLIERS (VALEURS ABERRANTES)')
    print('═' * 80)
    
    print('''
⚠️ OUTLIERS :
  • Valeurs extrêmes différentes du reste
  • Causes : Erreur de saisie, événement rare, capteur cassé
  • Exemple : Âge = 999 ans

🔧 MÉTHODES DE DÉTECTION :
  1. IQR (Interquartile Range)
     - Q1 = 25e percentile
     - Q3 = 75e percentile
     - Outliers : x < Q1 - 1.5*IQR ou x > Q3 + 1.5*IQR
  
  2. Z-Score
     - z = (x - moyenne) / std
     - Outliers : |z| > 3
  
  3. Isolation Forest (Machine Learning)
    ''')
    
    # Générer des données avec outliers
    np.random.seed(42)
    data = {
        'age': [28, 35, 26, 32, 29, 31, 27, 999, 25, 30],  # 999 = outlier
        'salaire': [3500, 4200, 3000, 4500, 3800, 4100, 3200, 3600, 3400, 4000]
    }
    df = pd.DataFrame(data)
    
    print('\n📊 Données avec outlier (âge=999) :')
    print(df.to_string())
    
    # MÉTHODE 1 : IQR
    print('\n🔧 MÉTHODE 1 : IQR')
    Q1 = df['age'].quantile(0.25)
    Q3 = df['age'].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    print(f'   Q1 = {Q1}, Q3 = {Q3}, IQR = {IQR}')
    print(f'   Limites : [{lower}, {upper}]')
    
    outliers = df[(df['age'] < lower) | (df['age'] > upper)]
    print(f'   ❌ Outliers détectés : {len(outliers)}')
    print(outliers.to_string())
    
    # Supprimer les outliers
    df_clean = df[(df['age'] >= lower) & (df['age'] <= upper)]
    print(f'\n   ✅ Après suppression : {len(df_clean)} lignes')
    
    # MÉTHODE 2 : Z-Score
    print('\n🔧 MÉTHODE 2 : Z-Score')
    z_scores = np.abs((df['age'] - df['age'].mean()) / df['age'].std())
    outliers_z = df[z_scores > 3]
    print(f'   ❌ Outliers détectés : {len(outliers_z)}')


def nettoyage_types():
    """Corriger les types de données"""
    print('\n' + '═' * 80)
    print('  8️⃣ NETTOYAGE - TYPES DE DONNÉES')
    print('═' * 80)
    
    print('''
🔤 TYPES DE DONNÉES :
  • int (entiers)
  • float (nombres décimaux)
  • str (chaînes de caractères)
  • datetime (dates)
  • category (catégories)
  • bool (booléen)

🔧 CONVERSION :
  df['age'] = df['age'].astype('int')
  df['date'] = pd.to_datetime(df['date'])
  df['ville'] = df['ville'].astype('category')
    ''')
    
    # Créer un dataset avec mauvais types
    data = {
        'id': ['1', '2', '3', '4', '5'],
        'age': ['28', '35', '26', '32', '29'],
        'date': ['2024-01-15', '2024-02-10', '2024-03-05', '2024-04-20', '2024-05-30'],
        'ville': ['Paris', 'Lyon', 'Paris', 'Marseille', 'Lyon']
    }
    df = pd.DataFrame(data)
    
    print('\n📊 Avant (mauvais types) :')
    print(df.dtypes)
    print(df.to_string())
    
    # Convertir les types
    df['id'] = df['id'].astype('int')
    df['age'] = df['age'].astype('int')
    df['date'] = pd.to_datetime(df['date'])
    df['ville'] = df['ville'].astype('category')
    
    print('\n✅ Après (bons types) :')
    print(df.dtypes)


# ═══════════════════════════════════════════════════════════════════════════════
# 3️⃣ TRANSFORMATION DE DONNÉES
# ═══════════════════════════════════════════════════════════════════════════════

def transformation_normalisation():
    """Normaliser les données"""
    print('\n' + '═' * 80)
    print('  9️⃣ TRANSFORMATION - NORMALISATION')
    print('═' * 80)
    
    print('''
📊 NORMALISATION :
  Mettre les données sur la même échelle [0, 1]
  
  Formule : x_norm = (x - min) / (max - min)
  
💡 QUAND L'UTILISER :
  • Avant K-Means
  • Avant réseaux de neurones
  • Quand variables ont unités différentes
  
EXEMPLE :
  • Âge : [20, 80] ans
  • Salaire : [1000, 5000] €
  → Normaliser pour avoir même impact
    ''')
    
    data = {
        'age': [20, 25, 30, 35, 40, 45, 50],
        'salaire': [1000, 1500, 2000, 2500, 3000, 3500, 4000]
    }
    df = pd.DataFrame(data)
    
    print('\n📊 Avant normalisation :')
    print(df.to_string())
    
    # Normalisation Min-Max
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    print('\n✅ Après normalisation [0, 1] :')
    print(df_normalized.to_string())
    
    # Normalisation Z-Score
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    print('\n✅ Avec Z-Score (moyenne=0, std=1) :')
    print(df_standardized.to_string())


def transformation_encoding():
    """Encoder les variables catégorielles"""
    print('\n' + '═' * 80)
    print('  🔟 TRANSFORMATION - ENCODING CATÉGORIES')
    print('═' * 80)
    
    print('''
🏷️ VARIABLES CATÉGORIELLES :
  • Texte ou catégories (homme/femme, couleur, etc.)
  • Les modèles ML ont besoin de nombres
  
🔧 MÉTHODES :

  1. LABEL ENCODING (Ordinal)
     Paris → 0, Lyon → 1, Marseille → 2
     ✓ Utiliser quand ordre logique
     ✗ Peut créer fausse ordre
  
  2. ONE-HOT ENCODING
     Paris → [1, 0, 0]
     Lyon → [0, 1, 0]
     Marseille → [0, 0, 1]
     ✓ Pas de fausse ordre
     ✗ Crée plus de colonnes
    ''')
    
    data = {
        'id': [1, 2, 3, 4, 5],
        'ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon'],
        'genre': ['M', 'F', 'M', 'F', 'M']
    }
    df = pd.DataFrame(data)
    
    print('\n📊 Avant encoding :')
    print(df.to_string())
    
    # Label Encoding
    print('\n🔧 LABEL ENCODING :')
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    df_label = df.copy()
    df_label['ville'] = le.fit_transform(df['ville'])
    print(df_label.to_string())
    
    # One-Hot Encoding
    print('\n🔧 ONE-HOT ENCODING :')
    df_onehot = pd.get_dummies(df, columns=['ville', 'genre'])
    print(df_onehot.to_string())


# ═══════════════════════════════════════════════════════════════════════════════
# 4️⃣ EXPLORATION DES DONNÉES (EDA)
# ═══════════════════════════════════════════════════════════════════════════════

def exploration_basique():
    """Exploration basique des données"""
    print('\n' + '═' * 80)
    print('  1️⃣1️⃣ EXPLORATION - STATISTIQUES BASIQUES')
    print('═' * 80)
    
    print('''
🔍 EXPLORATION (EDA - Exploratory Data Analysis) :
  • Comprendre les données
  • Détecter les anomalies
  • Former des hypothèses
    ''')
    
    # Générer des données
    np.random.seed(42)
    data = {
        'age': np.random.randint(20, 60, 100),
        'salaire': np.random.randint(2000, 5000, 100),
        'ville': np.random.choice(['Paris', 'Lyon', 'Marseille'], 100),
        'experience': np.random.randint(0, 20, 100)
    }
    df = pd.DataFrame(data)
    
    print('\n📊 FORME DU DATASET :')
    print(f'   Lignes : {len(df)}')
    print(f'   Colonnes : {len(df.columns)}')
    
    print('\n📋 APERÇU :')
    print(df.head())
    
    print('\n📈 STATISTIQUES :')
    print(df.describe())
    
    print('\n🏷️ TYPES :')
    print(df.dtypes)
    
    print('\n📊 DISTRIBUTION VILLE :')
    print(df['ville'].value_counts())


def exploration_correlations():
    """Analyser les corrélations"""
    print('\n' + '═' * 80)
    print('  1️⃣2️⃣ EXPLORATION - CORRÉLATIONS')
    print('═' * 80)
    
    print('''
📊 CORRÉLATION :
  Relation linéaire entre deux variables
  
  Valeur : [-1, 1]
  • +1 : Corrélation positive parfaite
  •  0 : Pas de corrélation
  • -1 : Corrélation négative parfaite
    ''')
    
    # Générer des données
    np.random.seed(42)
    data = {
        'age': np.random.randint(20, 60, 100),
        'salaire': np.random.randint(2000, 5000, 100),
        'experience': np.random.randint(0, 20, 100)
    }
    df = pd.DataFrame(data)
    
    # Ajouter corrélations réalistes
    df['salaire'] = df['experience'] * 150 + np.random.randint(0, 500, 100)
    
    print('\n📊 MATRICE DE CORRÉLATION :')
    corr = df.corr()
    print(corr)
    
    # Visualiser
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title('Matrice de Corrélation', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.show()


# ═══════════════════════════════════════════════════════════════════════════════
# 5️⃣ PRÉPARATION POUR ML
# ═══════════════════════════════════════════════════════════════════════════════

def preparation_ml():
    """Préparer les données pour le Machine Learning"""
    print('\n' + '═' * 80)
    print('  1️⃣3️⃣ PRÉPARATION - POUR LE MACHINE LEARNING')
    print('═' * 80)
    
    print('''
🎯 PIPELINE COMPLET :

  ÉTAPE 1 : Charger les données
  ↓
  ÉTAPE 2 : Nettoyage (valeurs manquantes, doublons, outliers)
  ↓
  ÉTAPE 3 : Exploration (statistiques, corrélations)
  ↓
  ÉTAPE 4 : Transformation (normalisation, encoding)
  ↓
  ÉTAPE 5 : Feature Selection (garder les meilleures colonnes)
  ↓
  ÉTAPE 6 : Train/Test Split (80/20)
  ↓
  ÉTAPE 7 : Entraîner le modèle
  ↓
  ÉTAPE 8 : Évaluer le modèle
    ''')
    
    # Générer un dataset d'exemple
    np.random.seed(42)
    n_samples = 200
    
    data = {
        'age': np.random.randint(20, 60, n_samples),
        'experience': np.random.randint(0, 30, n_samples),
        'formation': np.random.choice(['Bac', 'L1', 'L3', 'Master'], n_samples),
        'ville': np.random.choice(['Paris', 'Lyon', 'Marseille'], n_samples),
        'salaire': np.random.randint(2000, 5000, n_samples)
    }
    df = pd.DataFrame(data)
    
    print('\n📊 Dataset original :')
    print(df.head())
    
    # ÉTAPE 2 : Nettoyage
    print('\n✅ ÉTAPE 2 : Nettoyage')
    df = df.drop_duplicates()
    df = df.dropna()
    print(f'   Lignes : {len(df)}')
    
    # ÉTAPE 3 : Exploration
    print('\n✅ ÉTAPE 3 : Exploration')
    print(f'   Salaire moyen : €{df["salaire"].mean():.0f}')
    print(f'   Âge moyen : {df["age"].mean():.0f} ans')
    
    # ÉTAPE 4 : Transformation
    print('\n✅ ÉTAPE 4 : Transformation')
    
    # Normaliser les numériques
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[['age', 'experience']] = scaler.fit_transform(df[['age', 'experience']])
    
    # Encoder les catégorielles
    df = pd.get_dummies(df, columns=['formation', 'ville'])
    
    print(f'   Colonnes après encoding : {len(df.columns)}')
    
    # ÉTAPE 5 : Séparation features/target
    print('\n✅ ÉTAPE 5 : Séparation Features/Target')
    X = df.drop('salaire', axis=1)  # Features
    y = df['salaire']                 # Target
    print(f'   Features (X) : {X.shape}')
    print(f'   Target (y) : {y.shape}')
    
    # ÉTAPE 6 : Train/Test Split
    print('\n✅ ÉTAPE 6 : Train/Test Split (80/20)')
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f'   Train : {X_train.shape[0]} lignes')
    print(f'   Test : {X_test.shape[0]} lignes')
    
    print('\n✅ Données prêtes pour le ML !')


# ═══════════════════════════════════════════════════════════════════════════════
# MENU INTERACTIF
# ═══════════════════════════════════════════════════════════════════════════════

def menu():
    """Menu interactif"""
    
    print('\n' + '═' * 80)
    print('  🎓 COLLECTION ET TRAITEMENT DE DONNÉES')
    print('═' * 80)
    
    while True:
        print('\n📚 CHAPITRES DISPONIBLES :')
        print('  1️⃣  Collection - CSV')
        print('  2️⃣  Collection - Excel')
        print('  3️⃣  Collection - API')
        print('  4️⃣  Collection - Web Scraping')
        print('  5️⃣  Nettoyage - Valeurs manquantes')
        print('  6️⃣  Nettoyage - Doublons')
        print('  7️⃣  Nettoyage - Outliers')
        print('  8️⃣  Nettoyage - Types')
        print('  9️⃣  Transformation - Normalisation')
        print('  🔟 Transformation - Encoding')
        print('  1️⃣1️⃣ Exploration - Statistiques')
        print('  1️⃣2️⃣ Exploration - Corrélations')
        print('  1️⃣3️⃣ Préparation - Pipeline ML')
        print('  0️⃣  Quitter')
        
        choix = input('\n▶️  Sélectionnez un chapitre : ').strip()
        
        if choix == '1':
            collection_csv()
        elif choix == '2':
            collection_excel()
        elif choix == '3':
            collection_api()
        elif choix == '4':
            collection_web_scraping()
        elif choix == '5':
            nettoyage_valeurs_manquantes()
        elif choix == '6':
            nettoyage_doublons()
        elif choix == '7':
            nettoyage_outliers()
        elif choix == '8':
            nettoyage_types()
        elif choix == '9':
            transformation_normalisation()
        elif choix == '10':
            transformation_encoding()
        elif choix == '11':
            exploration_basique()
        elif choix == '12':
            exploration_correlations()
        elif choix == '13':
            preparation_ml()
        elif choix == '0':
            print('\n👋 Au revoir! Bon traitement de données!')
            break
        else:
            print('❌ Choix invalide. Essayez à nouveau.')


if __name__ == '__main__':
    menu()
