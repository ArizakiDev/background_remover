# Background Remover - Python CLI Tool

Bienvenue dans **Background Remover**, un programme créé en Python qui permet de supprimer le fond d'une image PNG ou JPEG avec simplicité. Ce projet utilise les bibliothèques `rembg` et `PIL`, et intègre des animations ASCII grâce à `pystyle` pour rendre l'expérience plus agréable et visuelle.

## Fonctionnalités

- **Suppression automatique du fond** : Chargez une image et supprimez son fond en un instant.
- **Interface CLI intuitive** : Facile à utiliser, avec support pour glisser-déposer d'images.
- **Retour visuel** : Ouvre l'image originale et l'image sans fond pour prévisualisation.
- **Compatibilité** : Supporte les formats PNG et JPEG.
- **Effets visuels avec Pystyle** : ASCII et bannières pour rendre l'interface plus vivante.

## Prérequis

Avant d'installer et de lancer l'application, assurez-vous d'avoir installé Python 3.x sur votre machine. Si Python n'est pas installé, vous pouvez le télécharger depuis : https://www.python.org/downloads/

### Bibliothèques requises :

- `rembg` : Pour supprimer le fond d'une image.
- `PIL` (Pillow) : Pour ouvrir et manipuler les images.
- `pystyle` : Pour l'affichage de textes colorés et d'animations ASCII dans la console.

## Installation

### Étape 1 : Cloner le dépôt

Commencez par cloner ce dépôt sur votre machine locale :

```bash
git clone https://github.com/ArizakiDev/background_remover.git
cd background_remover
pip install -r requirements.txt
python main.py
```

### Étape 2 : Le Lancement
- Une fois sur sur l'interface vous aurez une poire en ascii appuyez sur "entrer" pour voir le menu s'ouvrir.
- Glisser votre image dessus.
- Attendez la fin de l'opération.
