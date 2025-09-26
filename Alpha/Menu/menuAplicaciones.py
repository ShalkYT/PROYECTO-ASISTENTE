#################################################
# menuAplicaciones.py
# Script para gestionar el menú de aplicaciones
# Autor: Andres Eduardo Meneses Rincon
# Fecha: 2025-09-26
#################################################

from Funcionalidades.windows import abrir_app, cerrar_app, procesos

Comandos = ["abrir <aplicacion>", "cerrar <aplicacion>", "regresar, volver, salir, menu, retornar"]

def menuAplicaciones():
    print("Has entrado al menú de aplicaciones.")
    while True:
        comando = input("¿Qué deseas hacer? (escribe 'regresar' para volver al menú principal): ")
        subcomando = comando.split()

        # Manejo de comandos con argumentos
        if len(subcomando) > 1:
            if subcomando[0] == "abrir":
                if (subcomando[1] == "help" or subcomando[1] == "ayuda"):
                    for item in procesos.keys():
                        print(f"- {item}")
                else:
                    print(f"Abriendo {subcomando[1]}...")
                    abrir_app(subcomando[1])
            elif subcomando[0] == "cerrar":
                print(f"Cerrando {subcomando[1]}...")
                cerrar_app(subcomando[1])
            else:
                print(f"{subcomando[1]} es una opción inválida.")
        
        # Manejo de comandos sin argumentos
        match comando:
            case "ayuda" | "help":
                for item in Comandos:
                    print(f"- {item}")
            case "regresar" | "volver" | "salir" | "menu" | "retornar":
                print("Regresando al menú principal.")
                return