##########################################
# karen.py
# Script para gestionar tareas de Karen
# Autor: Andres Eduardo Meneses Rincon
# Fecha: 2025-09-26
###########################################

# Importar los módulos necesarios
from Menu.menuAplicaciones import menuAplicaciones
from Menu.menuSpotify import menuSpotify

# Lista de comandos disponibles
Comandos = ["aplicaciones", "spotify", "apagar, salir"]

# Función principal para el asistente
def Menu(comando):
    match comando:
        case "aplicaciones":
            print("Abriendo menu de aplicaciones...")
            menuAplicaciones()
        case "spotify":
            print("Abriendo menu de Spotify...")
            menuSpotify()
        case "menus":
            for item in Comandos:
                print(f"- {item}")
        case "apagar" | "salir":
            print("Apagando Karen...")
            exit()
        case _:
            print("Comando no reconocido.")

# Bucle principal para mantener el asistente activo
Encendido = True
while Encendido:
    Comando = input("Karen: ¿Qué deseas hacer? (escribe 'apagar' para salir): ")
    Menu(Comando)

