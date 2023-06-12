from pydub import AudioSegment
from pathlib import Path, PurePath


def crop_audio(input_file, output_file, start_time, end_time):
    audio = AudioSegment.from_file(input_file, format="mp4")  # 讀取音頻文件
    cropped_audio = audio[start_time:end_time]  # 裁剪音頻文件
    cropped_audio.export(output_file, format="mp4")  # 將裁剪後的音頻文件保存為 mp4 格式

def set_time(hh, mm, ss):
    total_sec = hh*3600 + mm*60 + ss
    return total_sec*1000

# 製作檔案路徑（我懶得key）
MP4_ROOT = Path("../../05.台大生機博班/00.生機機電工程學系研究生表單")
MP4_FILE = MP4_ROOT / "會前會-Part 1 (2023-06-07 18_07 GMT+8).mp4"

SPILIT_ROOT = Path("./Split")
SPILIT_FILE = SPILIT_ROOT / "會前會Part1_1"

START_TIME = set_time(0, 0, 0)
END_TIME = set_time(0, 5, 0)

if __name__ == '__main__':
    crop_audio(MP4_FILE, SPILIT_FILE, START_TIME, END_TIME)