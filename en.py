import webbrowser
import colorama
from colorama import Back, Fore, Style, init
colorama.init(autoreset=True)





traduzioni = {
    "key_not_found": "File {color_key}Key.txt{color_reset} not found. Creating the file...",
    "enter_valid_npsso": "Enter a valid npsso code: ",
    "npsso_correct": "Code {color_key}VALID{color_reset}",
    "npsso_incorrect": "npsso code {color_key}INCORRECT{color_reset}. Enter a {color_key2}new code{color_reset2}",
    "npsso_created_successfully": "Key.txt created and code inserted successfully",
    "npsso_expired": "npsso code {color_key}expired or incorrect{color_reset}.",
    "enter_npsso_valid": "Enter a valid npsso code: ",
    "reading_error": "Error while reading the Key.txt file: {error_message}",
    "exit":"Press any key to exit",
    "invalid_input": "INVALID INPUT. PLEASE TRY AGAIN",
    "id_non_trovato": "ID NOT FOUND. SEARCH AGAIN",
    "random":"RANDOM ERROR",
    "npsso_correct2": "Code {color_key}VALID{color_reset}"
}



def benvenuto():
    print(f"Tool by {Fore.CYAN}@yAmethxst{Fore.RESET}")
    print(f"API wrapper by{Fore.RED}'isFakeAccount'{Fore.RESET}(github)")
    print()
    API = input("You want to view the APIs? [y/n]: ")
    if API == "y":
        webbrowser.open("https://github.com/isFakeAccount/psnawp")
        print()
        print(f"{Back.WHITE}                                  ")
        print()
    else:
        print()
        print(f"{Back.WHITE}                                  ")
        print()