from diaries.AbstractDiary import AbstractDiary

class SakaiDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "1限目から授業で眠かった"

    def get_author(self):
        return "Sakai"