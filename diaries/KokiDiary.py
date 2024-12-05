from diaries.AbstractDiary import AbstractDiary

class KokiDiary(AbstractDiary):
    
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return """Githubdesktopのインストールを見逃していたので意味が分からなくて大変だった。
    資料の見落としには気をつけないとなと思った。"""
    
    def get_author(self):
        return "Koki"