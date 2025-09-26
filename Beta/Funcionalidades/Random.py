from Funcionalidades import Audio

def Repite(texto):
    repetir = ''.join(texto[2:len(texto)])        
    Audio.hablar(repetir)