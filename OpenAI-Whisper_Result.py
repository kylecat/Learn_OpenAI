"""
Topic:"How can CO2 and light co-optimization improve propagation in Vertical Farms Ricardo Hernandez NCSU, USA..mp4"
"""
import json
import datetime


FILE_NAME = "會前會Part2"

PATH = "./"+FILE_NAME+".json"
with open(PATH) as f:
    RawData = json.load(f)
f.close()

print(RawData.keys())
print(RawData.get('language'))
# 分段列出來
Segments = RawData.get('segments')
# _temp = Segments[0]
# print(_temp)
# print(_temp.keys())
_temp_seek = -1

MeetingDate = datetime.datetime.strptime("2023-06-08 20_04 GMT+8", "%Y-%m-%d %H_%M GMT+8")
MP4_START_TIME = datetime.datetime.strptime("00:00", "%H:%M")

# 看是用哪一個當作基準點
DATETIME_BASE = MeetingDate

Txt = open(FILE_NAME+".txt", "w")

for _line in Segments:
    _id = _line.get('id')
    _seek = _line.get('seek') # 同一個段落

    _start = _line.get('start')
    _end = _line.get('end')
    _f_start = datetime.timedelta(seconds=_start)
    _formate_start = DATETIME_BASE + _f_start
    _formate_start = _formate_start.strftime("%H:%M:%S")

    _f_end = datetime.timedelta(seconds=_end)
    _formate_end = DATETIME_BASE + _f_end
    _formate_end = _formate_end.strftime("%H:%M:%S")

    _text = _line.get('text')

    if _temp_seek != _seek:
        _temp_seek=_seek
        print(f" ===== {_seek:10d} ======================================== ")
    print(f"\t{_formate_start} ~ {_formate_end}\t{_text}")
    Txt.write(f"{_formate_start} ~ {_formate_end}\t{_text}\n")

Txt.close()