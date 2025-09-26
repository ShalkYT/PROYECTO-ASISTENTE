from Funcionalidades import Audio 
from Funcionalidades import Windows

def MenuWindows():
    Audio.hablar("¿Que deseas realizar en el equipo?")
    while True:

        comando = Audio.escuchar_comando()
        subcomando = comando.split()

        if len(subcomando) > 1:
            if subcomando[0] == "abrir":
                Windows.abrir_app(subcomando[1])
            elif subcomando[0] == "cerrar":
                Windows.cerrar_app(subcomando[1])
            else:
                Audio.hablar(subcomando[1]+ " es una opcion invalida")
        
        match comando:
            case "regresar" | "volver" | "salir" | "menu" | "retnornar":
                Audio.hablar("Regresando.")
                return

        
