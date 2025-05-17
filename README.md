# Jeu Snake - README
### 🎮 Description
Le jeu **Snake** est un classique des jeux d'arcade où le joueur contrôle un serpent qui grandit en mangeant de la nourriture. L'objectif est de survivre le plus longtemps possible sans heurter les murs ou son propre corps.

Ce projet est une implémentation moderne du Snake, développé en [langage/technologie utilisée, ex: Python avec Pygame]

### ⚙️ Mécanismes du jeu
### 🎯 Contrôles
* Flèches directionnelles (↑, ↓, →, ←) : Déplacer le serpent.

* Espace (optionnel) : Mettre le jeu en pause.

* Échap (optionnel) : Quitter le jeu.

### 📌 Règles du jeu
1. Déplacement : Le serpent se déplace en continu dans la direction choisie.

2. Nourriture : Manger la nourriture (🔴) fait grandir le serpent et augmente le score.

3. Collisions :

* Mur → Game Over.

* Corps du serpent → Game Over.

* Score : Chaque nourriture mangée rapporte + 1 point.

### ✨ Fonctionnalités
* **Niveaux de difficulté** (Vitesse augmentée).

* **Meilleurs scores** (Sauvegarde locale).

* **Effets sonores** (Manger, Game Over).

* **Design rétro ou moderne** (Personnalisable).

### Structure du code :
/snake-game    
│── snake.py         # Code principal  
│── README.md