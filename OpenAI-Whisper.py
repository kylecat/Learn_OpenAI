"""
:Official Document https://github.com/openai/whisper
注意：一個檔案只能小於25MB，且只能是MP3或MP4

Error:
    SystemError: initialization of _internal failed without raising an exception
    初始化失敗，Numpy及Numba版本不對打架，解決方案
    https://github.com/openai/whisper/discussions/1103

"""
import whisper
from pathlib import Path, PurePath
import json


# 製作檔案路徑（我懶得key）
MP4_ROOT = Path("../../05.台大生機博班/00.生機機電工程學系研究生表單")
MP4_FILE = MP4_ROOT / "會前會-Part 2 (2023-06-08 20_04 GMT+8).mp4"

MP4 = str(MP4_FILE.resolve())  # 路徑轉乘string
print(MP4)


model = whisper.load_model("base")  # 建立辨識模型
result = model.transcribe(MP4)  # 讀取檔案辨識出結果

print(result.keys())  # 把辨識結果的文字印出來

with open('會前會Part2.json', 'w') as f:
    json.dump(result, f)
f.close()
