# MP3 to WAV Conversion and LUFS Analysis

This code is intended to be run on Google Colab

This repository provides a Python script to convert MP3 files to WAV format and analyze the Loudness Units relative to Full Scale (LUFS) using `pydub`, `pyloudnorm`, and `soundfile` libraries. This is useful for audio processing and ensuring consistent loudness levels in audio files.

[日本語の説明もあります](README.ja.md)

## Features

	•	Convert MP3 files to WAV format in memory
	•	Perform LUFS analysis on the converted audio

Installation

```bash
!apt-get update
!apt-get install -y ffmpeg
!pip install pydub numpy pyloudnorm soundfile
```

## Usage

Replace '/path/to/your/file.mp3' with the path to your MP3 file.

Use the following Python script to convert an MP3 file to WAV format and perform LUFS analysis:

```python
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
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
