import pygame
import random
import time

# Paramètres du jeu
largeur, hauteur = 800, 600
taille_carte = 100
couleur_fond = (255, 255, 255)
couleur_carte_retournee = (150, 150, 150)

# Initialisation de l'écran
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Meme au riz")

# Définition des couleurs
couleur_carte = (0, 0, 255)
couleur_texte = (255, 255, 255)
couleur_texte_retourne = (0, 0, 0)

# Création de la grille de cartes
grille = [[0, 0, 1, 1],
         [2, 2, 3, 3],
         [4, 4, 5, 5],
         [6, 6, 7, 7]]

# Mélanger les cartes
random.shuffle(grille)
for ligne in grille:
    random.shuffle(ligne)

# Création d'une grille pour suivre les cartes retournées
cartes_retournees = [[False] * 4 for _ in range(4)]

# Chargement des images des cartes
images_cartes = []
for i in range(8):
    image = pygame.image.load(f"carte_{i + 1}.png")  # Assurez-vous d'avoir des images nommées carte_1.png, carte_2.png, etc.
    images_cartes.append(pygame.transform.scale(image, (taille_carte, taille_carte)))

# Fonction pour afficher les cartes
def afficher_cartes():
    for i in range(4):
        for j in range(4):
            if cartes_retournees[i][j]:
                ecran.blit(images_cartes[grille[i][j]], (j * taille_carte, i * taille_carte))
            else:
                pygame.draw.rect(ecran, couleur_carte_retournee, (j * taille_carte, i * taille_carte, taille_carte, taille_carte))

    pygame.display.update()

# Fonction principale du jeu
def jeu_memory():
    carte_retournee = None
    cartes_retournees_affichees = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                colonne = x // taille_carte
                ligne = y // taille_carte

                if not cartes_retournees[ligne][colonne]:
                    cartes_retournees[ligne][colonne] = True
                    afficher_cartes()

                    if carte_retournee is None:
                        carte_retournee = (ligne, colonne)
                    else:
                        if grille[ligne][colonne] != grille[carte_retournee[0]][carte_retournee[1]]:
                            time.sleep(1)
                            cartes_retournees[ligne][colonne] = False
                            cartes_retournees[carte_retournee[0]][carte_retournee[1]] = False
                        carte_retournee = None
                        cartes_retournees_affichees += 2

        afficher_cartes()

        if cartes_retournees_affichees == 16:
            afficher_message("Félicitations! Vous avez gagné.")
            time.sleep(2)
            pygame.quit()
            quit()

# Fonction pour afficher un message
def afficher_message(message):
    font = pygame.font.SysFont(None, 55)
    texte = font.render(message, True, couleur_texte)
    ecran.blit(texte, (largeur // 2 - texte.get_width() // 2, hauteur // 2 - texte.get_height() // 2))
    pygame.display.update()

if __name__ == "__main__":
    jeu_memory()