class PracticeBookError(Exception):
    """モジュール独自の例外の基底クラス"""

class PageNotFoundError(PracticeBookError):
    """ページが見つからないときの例外"""
    def __init__(self, message):
        self.message = message

class InvalidPageNumberError(PracticeBookError):
    """不正なページ番号が指定されたときの例外"""
    def __init__(self, message):
        self.message = message