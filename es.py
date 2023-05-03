import webbrowser
import colorama
from colorama import Back, Fore, Style, init
colorama.init(autoreset=True)





traduzioni = {
    "key_not_found": "Archivo {color_key}Key.txt{color_reset} no encontrado. Creando el archivo...",
    "enter_valid_npsso": "Introduce un código npsso válido: ",
    "npsso_correct": "Código {color_key}VÁLIDO{color_reset}",
    "npsso_incorrect": "Código npsso {color_key}INCORRECTO{color_reset}. Introduce un {color_key2}nuevo código{color_reset2}",
    "npsso_created_successfully": "Key.txt creado y código insertado correctamente",
    "npsso_expired": "Código npsso {color_key}caducado o incorrecto{color_reset}.",
    "enter_npsso_valid": "Introduce un código npsso válido: ",
    "reading_error": "Error al leer el archivo Key.txt: {error_message}",
    "exit": "Presiona cualquier tecla para salir",
    "invalid_input": "ENTRADA INVÁLIDA. POR FAVOR, INTÉNTALO DE NUEVO",
    "id_non_trovato": "ID NO ENCONTRADO. BUSCA DE NUEVO",
    "random":"ERROR AL AZAR",
    "npsso_correct2": "Código {color_key}VÁLIDO{color_reset}"
}



def benvenuto():
    print(f"Tool by {Fore.CYAN}@yAmethxst{Fore.RESET}")
    print(f"API wrapper by{Fore.RED}'isFakeAccount'{Fore.RESET}(github)")
    print()
    API = input("¿Quieres ver las API? [y/n]: ")
    if API == "y":
        webbrowser.open("https://github.com/isFakeAccount/psnawp")
        print()
        print(f"{Back.WHITE}                                  ")
        print()
    else:
        print()
        print(f"{Back.WHITE}                                  ")
        print()