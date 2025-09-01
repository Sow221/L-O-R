# 🚀 Débuter avec Git (Pratique)

## Objectif
Apprendre à initialiser un dépôt Git, versionner un fichier, et comprendre le cycle de base.

---

### 1. Créer un dossier projet

```sh
mkdir essai-git
cd essai-git
```

---

### 2. Initialiser Git

```sh
git init
```

*Un dossier .git apparaît : Git est prêt !*

---

### 3. Créer un fichier, l’ajouter au dépôt

```sh
echo "Hello Git" > fichier.txt
git status          # Voir les fichiers non suivis
git add fichier.txt # Ajouter au suivi
git commit -m "Premier fichier versionné"
```

---

### 4. Apporter une modification

```sh
echo "Nouvelle ligne" >> fichier.txt
git status
git add fichier.txt
git commit -m "Ajouté une nouvelle ligne"
```

---

### 5. Consulter l’historique

```sh
git log        # Liste détaillée des commits
git log --oneline   # Version compacte
```

---

### Résumé

Cycle à retenir :
1. Créer/modifier un fichier
2. `git status` — regarder les changements
3. `git add ...` — préparer
4. `git commit -m "..."` — enregistrer

---

### 🚩 À Toi de jouer

- Recommence ce cycle avec d’autres fichiers.
- Supprime ou renomme des fichiers, observe les réactions de Git.