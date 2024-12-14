from pynput.keyboard import Key, Controller
import time

def read_ascii_from_file(filename):
    """Lit l'art ASCII depuis un fichier texte.
    
    Args:
        filename: Le nom du fichier texte contenant l'art ASCII.
        
    Returns:
        Une liste de chaînes de caractères représentant l'art ASCII.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_ascii_art(ascii_art, delay=0.0):
    """Écrit l'art ASCII ligne par ligne en utilisant uniquement les flèches.

    Args:
        ascii_art: Une liste de chaînes de caractères représentant chaque ligne de l'art ASCII.
        delay: Le délai entre chaque caractère tapé (en secondes).
    """
    keyboard = Controller()

    for line in ascii_art:
        # Supprime les espaces ou retours à la ligne inutiles
        line = line.strip()

        # Tape la ligne
        for char in line:
            keyboard.type(char)
            time.sleep(delay)

        # Revenir au début et passer à la ligne suivante
        for _ in range(len(line)):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            time.sleep(0.01)  # Ajuster si besoin pour des performances optimales
        
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(0.05)

if __name__ == "__main__":
    # Charger l'art ASCII depuis le fichier
    ascii_file = "ascii.txt"
    try:
        ascii_art = read_ascii_from_file(ascii_file)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {ascii_file} est introuvable.")
        exit(1)

    # Compte à rebours pour positionner le curseur
    print("Placez votre curseur là où vous voulez que le dessin commence.")
    for i in range(5, 0, -1):
        print(f"Début dans {i} secondes...")
        time.sleep(1)

    # Écriture de l'art ASCII
    write_ascii_art(ascii_art, delay=0.01)  # Plus rapide
    print("Dessin terminé !")
