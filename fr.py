import webbrowser
import colorama
from colorama import Back, Fore, Style, init
colorama.init(autoreset=True)





traduzioni = {
    "key_not_found": "Fichier {color_key}Key.txt{color_reset} introuvable. Création du fichier...",
    "enter_valid_npsso": "Entrez un code npsso valide: ",
    "npsso_correct": "Code {color_key}VALIDE{color_reset}",
    "npsso_incorrect": "Code npsso {color_key}INCORRECT{color_reset}. Entrez un {color_key2}nouveau code{color_reset2}",
    "npsso_created_successfully": "Key.txt créé et code inséré avec succès",
    "npsso_expired": "Code npsso {color_key}expiré ou incorrect{color_reset}.",
    "enter_npsso_valid": "Entrez un code npsso valide: ",
    "reading_error": "Erreur lors de la lecture du fichier Key.txt: {error_message}",
    "exit": "Appuyez sur une touche pour quitter",
    "invalid_input": "ENTRÉE INVALIDE. VEUILLEZ RÉESSAYER",
    "id_non_trovato": "ID INTRROUVABLE. RECHERCHEZ À NOUVEAU",
    "random":"ERREUR ALÉATOIRE",
    "npsso_correct2": "Code {color_key}VALIDE{color_reset}"
}



def benvenuto():
    print(f"Tool by {Fore.CYAN}@yAmethxst{Fore.RESET}")
    print(f"API wrapper by{Fore.RED}'isFakeAccount'{Fore.RESET}(github)")
    print()
    API = input("Vous voulez voir les API? [y/n]: ")
    if API == "y":
        webbrowser.open("https://github.com/isFakeAccount/psnawp")
        print()
        print(f"{Back.WHITE}                                  ")
        print()
    else:
        print()
        print(f"{Back.WHITE}                                  ")
        print()