from diaries.DiarySample import DiarySample
from diaries.k23121Diary import k23121Diary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    k23121Diary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()