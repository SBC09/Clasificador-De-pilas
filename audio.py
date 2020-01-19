#EJEMPLO DE GRABADORA DE SONIDO CON "pyaudio".
#IMPORTAMOS LIBRERIAS NECESARIAS
import pyaudio
import wave
import speech_recognition as sr # Importamos los modulos necesarios
def entrada_de_vo():

    FORMAT=pyaudio.paInt16
    CHANNELS=2
    RATE=44100
    CHUNK=1024
    duracion=5
    archivo="Pilas.wav"
    #INICIAMOS "pyaudio"
    audio=pyaudio.PyAudio()

#INICIAMOS GRABACION
    stream=audio.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("grabando...")
    frames=[]

    for i in range(0, int(RATE/CHUNK*duracion)):
        dato=stream.read(CHUNK)
        frames.append(dato)
    print("grabacion terminada")

#DETENEMOS GRABACION
    stream.stop_stream()
    stream.close()
    audio.terminate()

#CREAMOS/GUARDAMOS EL ARCHIVO DE AUDIO
    waveFile = wave.open(archivo, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("Pilas.wav") as source:
    audio2 = r.record(source)
    fichero = open("Pilas.txt", "w")
        # recognize speech usando Google Speech Recognition
    try:
        salida = (r.recognize_google(audio2, language='es-ESP'))
        fichero.write(salida)

    except sr.UnknownValueError: # Definimos excepciones que se puedan presentar
            salida = ("")
            fichero.write(salida)
    except sr.RequestError as e:
            salida = ("no se pueden usar los servicios de Google Speech Recognition; {0}".format(e))
            fichero.write(salida)

    fichero.close()
