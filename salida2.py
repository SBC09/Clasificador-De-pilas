import pyaudio
import wave
def correcto():
    file=wave.open("Correcto.wav","rb")
    p = pyaudio.PyAudio()
    chunk=1024
    # open stream
    stream = p.open(format=p.get_format_from_width(file.getsampwidth()),
                        channels=file.getnchannels(),
                        rate=file.getframerate(),
                        output=True)
    data = file.readframes(chunk)

#play stream
    while data:
        stream.write(data)
        data = file.readframes(chunk)

    stream.stop_stream()
    stream.close()
    #close PyAudio
    p.terminate()


def incorrecto():
    file = wave.open("incorrecto.wav", "rb")
    p = pyaudio.PyAudio()
    chunk = 1024
    # open stream
    stream = p.open(format=p.get_format_from_width(file.getsampwidth()),
                    channels=file.getnchannels(),
                    rate=file.getframerate(),
                    output=True)
    data = file.readframes(chunk)

    # play stream
    while data:
        stream.write(data)
        data = file.readframes(chunk)

    stream.stop_stream()
    stream.close()
    # close PyAudio
    p.terminate()


