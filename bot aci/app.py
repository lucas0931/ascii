import customtkinter as ctk
from tkinter import filedialog, messagebox
from pynput.keyboard import Key, Controller
import time
import threading


# Fonction pour lire le fichier ASCII
def read_ascii_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


# Fonction pour écrire l'art ASCII
def write_ascii_art(ascii_art, delay=0.01):
    keyboard = Controller()

    for line in ascii_art:
        for char in line:
            if char == " ":
                keyboard.press(Key.space)
                keyboard.release(Key.space)
            else:
                keyboard.type(char)
            time.sleep(delay)

        for _ in range(len(line)):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            time.sleep(0.01)
        
        keyboard.press(Key.down)
        keyboard.release(Key.down)


# Fonction pour démarrer l'impression
def start_printing(file_path, delay):
    try:
        ascii_art = read_ascii_from_file(file_path)
    except FileNotFoundError:
        messagebox.showerror("Erreur", f"Le fichier '{file_path}' est introuvable.")
        return

    countdown_window = ctk.CTkToplevel()
    countdown_window.title("Préparation")
    countdown_window.geometry("250x150")
    countdown_window.config(bg="#2e3b4e")
    
    ctk.CTkLabel(countdown_window, text="Placez votre curseur là où vous voulez commencer.", text_color="white", bg_color="#2e3b4e").pack(pady=10)
    countdown_label = ctk.CTkLabel(countdown_window, text="Début dans 5 secondes...", font=("Arial", 14), text_color="white", bg_color="#2e3b4e")
    countdown_label.pack(pady=10)

    def countdown_and_start():
        for i in range(5, 0, -1):
            countdown_label.configure(text=f"Début dans {i} secondes...")
            time.sleep(1)

        countdown_window.destroy()
        threading.Thread(target=write_ascii_art, args=(ascii_art, delay), daemon=True).start()

    threading.Thread(target=countdown_and_start, daemon=True).start()


# Fonction de sélection du fichier
def select_file():
    file_path = filedialog.askopenfilename(
        title="Sélectionnez un fichier ASCII",
        filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
    )
    if file_path:
        file_entry.delete(0, ctk.END)
        file_entry.insert(0, file_path)


# Action du bouton "Démarrer"
def start_button_action():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Erreur", "Veuillez sélectionner un fichier ASCII.")
        return

    try:
        delay = float(delay_entry.get())
    except ValueError:
        messagebox.showerror("Erreur", "Le délai doit être un nombre valide.")
        return

    start_printing(file_path, delay)


# Création de la fenêtre principale
ctk.set_appearance_mode("dark")  # Mode sombre
ctk.set_default_color_theme("blue")  # Thème bleu

root = ctk.CTk()
root.title("Impression ASCII")
root.geometry("600x400")
root.resizable(False, False)

# Titre de l'application
title_label = ctk.CTkLabel(root, text="Impression d'Art ASCII", font=("Arial", 20, "bold"), text_color="white")
title_label.pack(pady=20)


# Section de sélection du fichier
file_frame = ctk.CTkFrame(root)
file_frame.pack(pady=20)

file_label = ctk.CTkLabel(file_frame, text="Fichier ASCII : ", font=("Arial", 12), text_color="white")
file_label.grid(row=0, column=0, padx=5)

file_entry = ctk.CTkEntry(file_frame, width=40, font=("Arial", 12), placeholder_text="Sélectionner un fichier")
file_entry.grid(row=0, column=1, padx=5)

browse_button = ctk.CTkButton(file_frame, text="Parcourir", font=("Arial", 12), command=select_file)
browse_button.grid(row=0, column=2, padx=5)


# Section pour le délai
delay_frame = ctk.CTkFrame(root)
delay_frame.pack(pady=20)

delay_label = ctk.CTkLabel(delay_frame, text="Délai (s) entre les caractères : ", font=("Arial", 12), text_color="white")
delay_label.grid(row=0, column=0, padx=5)

delay_entry = ctk.CTkEntry(delay_frame, width=10, font=("Arial", 12))⠀⠀
delay_entry.grid(row=0, column=1, padx=5)
delay_entry.insert(0, "0.04")


# Bouton Démarrer
start_button = ctk.CTkButton(root, text="Démarrer", font=("Arial", 14, "bold"), command=start_button_action)
start_button.pack(pady=30)


# Lancer l'application
root.mainloop()
