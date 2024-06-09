import numpy as np
from pydub import AudioSegment
import pyloudnorm as pyln
import soundfile as sf
import io

# MP3ファイルのパス
mp3_path = '/path/to/your/file.mp3'

# MP3をWAVに変換し、メモリ上に保持
audio = AudioSegment.from_file(mp3_path, format='mp3')
wav_io = io.BytesIO()
audio.export(wav_io, format='wav')
wav_io.seek(0)  # バイトオブジェクトの先頭に戻る

# バイトオブジェクトを使ってWAVデータをsf.readで読み込む
data, sample_rate = sf.read(wav_io)

# LUFS解析
meter = pyln.Meter(sample_rate)  # BS.1770メーターを作成
loudness = meter.integrated_loudness(data)

print(f'Integrated Loudness (LUFS): {loudness}')
print(f'YouTube Loudness (LUFS): {loudness + 12}')
