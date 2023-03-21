"""
Error:
    SystemError: initialization of _internal failed without raising an exception
    初始化失敗，Numpy及Numba版本不對打架，解決方案
    https://github.com/openai/whisper/discussions/1103
"""
import whisper
import pathlib

# 製作檔案路徑（我懶得key）
PATH = pathlib.Path()
HOME = PATH.home()
MP4_ROOT = HOME.joinpath("Desktop/ISHS_Talks")
MP4_FILE = MP4_ROOT.joinpath(
    "How can CO2 and light co-optimization improve propagation in Vertical Farms Ricardo Hernandez NCSU, USA..mp4")

MP4 = str(MP4_FILE.resolve())
print(MP4)

model = whisper.load_model("base")  # 建立便是模型
result = model.transcribe(MP4)  # 讀取檔案辨識出結果

print(result)  # 把辨識結果的文字印出來
