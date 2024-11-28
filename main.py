from diaries.DiarySample import DiarySample
from diaries.k23121Diary import k23121Diary
from diaries.FuwaDiary import FuwaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
  k23121Diary(),
    FuwaDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()