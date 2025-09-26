#################################################
# menuSpotify.py
# Script para gestionar el menú de Spotify
# Autor: Andres Eduardo Meneses Rincon
# Fecha: 2025-09-26
#################################################

# Lista de comandos disponibles
Comandos = ["reproducir <cancion>", "pausar", "regresar, volver, salir, menu, retornar"]

# Función para el menú de Spotify
def menuSpotify():
    print("Has entrado al menú de Spotify.")
    while True:
        comando = input("¿Qué deseas hacer? (escribe 'regresar' para volver al menú principal): ")
        subcomando = comando.split()

        # Manejo de comandos con argumentos
        if len(subcomando) > 1:
            match subcomando[0]:
                case "reproducir":
                    print(f"Reproduciendo {subcomando[1]}...")
                case _:
                    print(f"{subcomando[0]} es una opción inválida.")
        
        # Manejo de comandos sin argumentos
        match comando:
            case "pausar":
                print("Pausando la canción...")
            case "comandos" | "help":
                for item in Comandos:
                    print(f"- {item}")
            case "regresar" | "volver" | "salir" | "menu" | "retornar":
                print("Regresando al menú principal.")
                return
            case _:
                print("Comando no reconocido.")