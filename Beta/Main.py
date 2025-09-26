import Spotify
import Audio
import Windows
import time

Audio.hablar("Estoy listo. Puedes hablar")
Audio.hablar("Prueba")
while True:
    comando = Audio.esperar_comando()
    subcomando = comando.split()

    if len(subcomando) > 1:
        if subcomando[0] == "abrir":
            Windows.abrir_app(subcomando[1])
        else:
            print(subcomando[1] + " es inválida")
    else:
        print("Comando incompleto")

    if len(subcomando) > 1:
        if subcomando[0] == "cerrar":
            Windows.cerrar_app(subcomando[1])
        else:
            print(subcomando[1] + " es inválida")
    else:
        print("Comando incompleto")

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
        case "salir" | "adiós":
            Audio.hablar("Hasta luego.")
            break
        case "gracias":
            Audio.hablar("De nada")
        

