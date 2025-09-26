from Funcionalidades import Audio 
from Funcionalidades import Spotify

def MenuSpotify():
    Audio.hablar("¿Que deseas realizar en espotify?")
    while True:
        comando = Audio.escuchar_comando()
        subcomando = comando.split()

        if len(subcomando) > 1:
            if subcomando[0] == "buscar":
                cancion = ' '.join(subcomando[1:len(subcomando)])
                Spotify.buscar_cancion(subcomando[1])
            else:
                print(subcomando[1] + " es inválida")
        else:
            print("Comando incompleto")

        match comando:
            case "siguiente canción" | "siguiente":
                Spotify.sp.next_track()
                Audio.hablar("Pasando a la siguiente canción")
            case "pausar" | "detener":
                Spotify.sp.pause_playback()
                Audio.hablar("Música pausada")
            case "reproducir" | "reanudar":
                Spotify.sp.start_playback()
                Audio.hablar("Reproduciendo música")
            case "gracias":
                Audio.hablar("De nada")
            case "regresar" | "volver" | "salir" | "menu" | "retnornar":
                Audio.hablar("Regresando.")
                return
             