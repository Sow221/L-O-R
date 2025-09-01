# 🏁 Initiation Pratique à Git & GitHub

## Objectifs du cours

- **Comprendre** les principes et intérêts du versionnement
- **Installer** et **configurer** Git
- **Versionner** ses travaux en local
- **Partager** sur GitHub et collaborer pas à pas
- **Découvrir** les commandes essentielles et les bonnes pratiques

---

## 1. Qu’est-ce que Git ? Qu’est-ce que GitHub ?

**Git** est un logiciel permettant de suivre et d’organiser les modifications de fichiers (historique, retour en arrière, collaboration).
- Versionnage **local** : on travaille sur sa machine, sans connexion Internet
- Rapide, robuste, utilisé par tous les grands projets

**GitHub** : service Web qui héberge des projets Git et facilite la collaboration et le suivi à distance.

---

## 2. Installer Git

- Télécharger depuis : https://git-scm.com/
- Installer (Windows, Mac, Linux : cliquer, accepter)
- Vérifier l’installation :

    ```sh
    git --version
    ```

---

## 3. Configurer Git

Spécifie ton nom et ton mail :

```sh
git config --global user.name "Votre Prénom NOM"
git config --global user.email "votre@email.com"
```

Vérifie ta config :

```sh
git config --list
```

---

## 4. Créer son premier dépôt Git

Ouvre un terminal ou un invite de commandes et tape :

```sh
mkdir mon-projet-git
cd mon-projet-git
git init
```

*Le dossier caché `.git` est là — c’est le cœur du versionnement.*

---

## 5. Ajouter et sauvegarder ses fichiers (add & commit)

### Ajouter un fichier, puis le “suivre” :

```sh
echo "Ceci est mon premier fichier" > fichier.txt
git status
git add fichier.txt
git status
```

### Enregistrer le changement (commit) :

```sh
git commit -m "Premier commit : ajout du fichier.txt"
```

### Visualiser l’historique

```sh
git log
```

*Astuce : `q` pour quitter Git log !*

---

## 6. Modifier, supprimer ou renommer un fichier

```sh
echo "Deuxieme ligne" >> fichier.txt   # On modifie
git add fichier.txt
git commit -m "Ajout d'une 2e ligne"

git mv fichier.txt notes.txt           # Renommer
git commit -am "Renommage en notes.txt"

git rm notes.txt                       # Supprimer
git commit -m "Suppression du fichier notes.txt"
```

---

## 7. Travailler avec GitHub

### 7.1 Créer un dépôt GitHub

1. Aller sur https://github.com/
2. Cliquer sur “New repository”
3. Nommer ton repo (ex : mon-projet-git), ne rien cocher, valider.

### 7.2 Lier le projet local au distant

```sh
git remote add origin https://github.com/TonPseudo/mon-projet-git.git
```

### 7.3 Envoyer le projet sur GitHub (push)

```sh
git push -u origin master
```

> **Si tu fais une erreur ou si un “main” et non “master” existe, adapte la branche !**

---

## 8. Mettre à jour son dépôt (pull) et cloner

- **Tirer** : récupérer ce qui a changé sur GitHub :

    ```sh
    git pull origin master
    ```

- **Cloner** un projet GitHub chez toi :

    ```sh
    git clone https://github.com/lecompte/lemodule.git
    ```

---

## 9. Les branches pour travailler sans se gêner

```sh
git branch nouvelle-fonction
git checkout nouvelle-fonction
# On modifie, add/commit
git checkout master
git merge nouvelle-fonction
```

---

## 10. Résumé visuel : Le cycle Git de base

1. Modifier/créer un fichier
2. `git status` — vérifier ce qui a changé
3. `git add ...` — préparer
4. `git commit -m "Message"` — enregistrer
5. `git push origin master` — envoyer sur GitHub

---

## 🏋️ Exercices pratiques

**1. Crée un dossier, initialises-y git, ajoutes un fichier et versionne-le.**
**2. Crée un repo GitHub, relie-le à ton dossier local, et pousse ton historique.**
**3. Clone ce repo sur une autre machine ou dossier, travailles-y puis push/pull.**
**4. Crée une branche, fais-y un commit, fusionne-la.**

---

## 📚 Ressources utiles

- [Git - La documentation](https://git-scm.com/doc)
- [GitHub Docs (fr)](https://docs.github.com/fr)
- [Learn Git Branching (FR)](https://learngitbranching.js.org/?locale=fr_FR)
- [Git cheat sheet PDF (officiel)](https://education.github.com/git-cheat-sheet-education.pdf)

---

## ✅ Bonnes pratiques

- Commitez souvent, avec des messages clairs.
- Travaillez sur des branches.
- Pull avant de push !
- Ne mettez jamais de secrets ou mots de passe dans les dépôts publics !
- Documentez votre historique.

---
