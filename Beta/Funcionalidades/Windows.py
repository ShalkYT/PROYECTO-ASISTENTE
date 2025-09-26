import os
import subprocess

def abrir_app(nombre_app):
    carpeta_accesos = os.path.join(os.path.dirname(__file__), "accesos")
    nombre_lnk = nombre_app.lower() + ".lnk"
    ruta_lnk = os.path.join(carpeta_accesos, nombre_lnk)

    if os.path.exists(ruta_lnk):
        subprocess.Popen(ruta_lnk, shell=True)
        print(f"Abriste {nombre_app}")
    else:
        print(f"No se encontró acceso para '{nombre_app}' en {carpeta_accesos}")

procesos = {
    "osu": "osu!.exe",
    "spotify": "Spotify.exe",
    "bloc": "notepad.exe",
    "epic": "EpicGamesLauncher.exe",
    "discord": "Discord.exe",
    "google": "chrome.exe",
    "steam": "steam.exe",
    "paint": "paintdotnet.exe"
}

def cerrar_app(nombre_alias):
    nombre_proceso = procesos.get(nombre_alias.lower())
    if nombre_proceso:
        resultado = subprocess.run(
            ["taskkill", "/f", "/im", nombre_proceso],
            capture_output=True,
            text=True
        )
        if "SUCCESS" in resultado.stdout:
            print(f"{nombre_alias} ha sido cerrada.")
        else:
            print(f"No se pudo cerrar {nombre_alias}. Resultado:\n{resultado.stdout}")
    else:
        print(f"{nombre_alias} es inválida.")

