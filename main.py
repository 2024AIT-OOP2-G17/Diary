from diaries.k23121Diary import k23121Diary
from diaries.FuwaDiary import FuwaDiary
from diaries.SakaiDiary import SakaiDiary
from diaries.YuhiDiary import YuhiDiary
from diaries.KokiDiary import KokiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    k23121Diary(),
    FuwaDiary(),
    SakaiDiary(),
    YuhiDiary(),
    KokiDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()