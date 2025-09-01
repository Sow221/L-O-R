# HTML – Les formulaires

## Objectif
Créer un formulaire de saisie simple et comprendre ses composants.

---

## Exemple de formulaire basique

```html
<form action="#" method="post">
  <label>Nom : <input type="text" name="nom"></label><br>
  <label>Email : <input type="email" name="email"></label><br>
  <input type="submit" value="Envoyer">
</form>
```

---

## Exercice pratique
1. Crée `formulaire.html`.
2. Ajoute les champs prénom, nom, email et un bouton d’envoi.
3. Ajoute un champ de type mot de passe et une zone de texte longue (`textarea`).