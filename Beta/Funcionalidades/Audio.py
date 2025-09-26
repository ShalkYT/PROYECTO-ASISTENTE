import speech_recognition as sr

from gtts import gTTS
import pygame
import tempfile
import os

def hablar(texto):
    print(f"Asistente: {texto}")
    tts = gTTS(text=texto, lang='es')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        path = fp.name
        tts.save(path)

    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    os.remove(path)



def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Escuchando...")
        recognizer.adjust_for_ambient_noise(source)  # ajusta al ruido ambiente
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="es-CO")
        print(f"👂 Escuchado: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("⚠️ No entendí lo que dijiste.")
        return ""
    except sr.RequestError:
        print("❌ Error con el servicio de reconocimiento.")
        return ""

def esperar_comando(activador="viernes"):
    while True:
        texto = escuchar_comando()
        if activador in texto:
            partes = texto.split(activador, 1)
            comando = partes[1].strip() if len(partes) > 1 else ""
            if comando:
                return comando
            else:
                hablar("¿Qué necesitas?")
                return escuchar_comando()
        else:
            print("Esperando palabra de activación...")
