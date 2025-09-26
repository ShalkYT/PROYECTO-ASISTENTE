from Funcionalidades import Audio
from Funcionalidades import Random
from datetime import datetime
from Menus.SpotMenu import MenuSpotify
from Menus.WindMenu import MenuWindows

def PasoAPaso(comando):
    if "viernes" in comando:
        Audio.hablar("Esperando instrucción")
        while True:
            comando = Audio.escuchar_comando()
            match comando:
                case "spotify":
                    MenuSpotify()
                case "equipo":
                    MenuWindows()
                case "salir" | "adios" | "Cerrar":
                    break
    else:
        print("Comando invalido")

def MenuDirecto(comandos):
    if Comandos[0] == "viernes":
        match Comandos[1]:
            case "spotify":
                MenuSpotify()
            case "equipo":
                MenuWindows()
            case _:
                Audio.hablar("Menu no reconocido")
                

#Main

Hora = datetime.now().strftime("%H:%M")
Audio.hablar("Bienvenido. La hora actual es: " + Hora)

bucle = True
while bucle:
    Escuchado = Audio.escuchar_comando()    
    Comandos = Escuchado.split()
    
    if len(Comandos) == 1:
        PasoAPaso(Escuchado)
    elif len(Comandos) == 2:
        MenuDirecto(Comandos)
    elif len(Comandos) > 2:
        Random.Repite(Comandos)

