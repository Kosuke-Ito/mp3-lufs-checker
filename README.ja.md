# MP3からWAVへの変換とLUFS解析

このコードはGoogle Colabで実行することを想定しています。

このリポジトリは、MP3ファイルをWAV形式に変換し、`pydub`、`pyloudnorm`、`soundfile`ライブラリを使用してLUFS（ラウドネス単位）を解析するPythonスクリプトを提供します。これは、音声処理や音声ファイルの一貫したラウドネスレベルを確保するのに役立ちます。

[English README here](README.md)

## 特徴

	•	MP3ファイルをメモリ上でWAV形式に変換
	•	変換した音声データのLUFS解析

インストール

必要なパッケージをインストールします：

```bash
!apt-get update
!apt-get install -y ffmpeg
!pip install pydub numpy pyloudnorm soundfile
```

## 使用方法

'/path/to/your/file.mp3'をMP3ファイルのパスに置き換えてください。

以下のPythonスクリプトを使用して、MP3ファイルをWAV形式に変換し、LUFSを解析します：

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


## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルをご覧ください。
