import numpy as np
from pydub import AudioSegment
import pyloudnorm as pyln
import soundfile as sf
import io

mp3_path = '/path/to/your/file.mp3'

audio = AudioSegment.from_file(mp3_path, format='mp3')
wav_io = io.BytesIO()
audio.export(wav_io, format='wav')
wav_io.seek(0)

data, sample_rate = sf.read(wav_io)
meter = pyln.Meter(sample_rate)
loudness = meter.integrated_loudness(data)

print(f'Integrated Loudness (LUFS): {loudness}')
print(f'YouTube Loudness (LUFS): {loudness + 12}')
