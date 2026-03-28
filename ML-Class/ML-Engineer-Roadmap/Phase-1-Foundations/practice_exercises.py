import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('=== EXO 1: Lire et explorer data ===')
df = pd.read_csv('sample_data.csv')
print('Shape:', df.shape)
print(df.describe())

print('\\n=== EXO 2: Nettoyer ===')
df['quantite'] = df['quantite'].fillna(df['quantite'].mean())
print('Missing fixed:', df.isnull().sum().sum())

print('\\n=== EXO 3: Filtrer Dakar >15kg ===')
dakar = df[(df['ville'] == 'Dakar') & (df['quantite'] > 15)]
print(dakar)

print('\\n=== EXO 4: Graphique ===')
plt.hist(df['quantite'], bins=5)
plt.title('Distribution quantités')
plt.savefig('exo4_hist.png')
print('Graph sauvegardé: exo4_hist.png')

print('\\n=== BON! Fais tes propres tests ci-dessous ===')
# Ajoute ton code ici, relance le script!

