class AlreadyCheckedOutBookException(Exception):
    """
    이미 대출 중인 도에 대출을 요청했을 경우 발생하는 에러
    """


class BookHasNoBorrowHistory(Exception):
    """
    대출 이력이 없는 도서에 반납을 요청했을 경우 발생하는 에러
    """


class BookIsNotCheckedOutException(Exception):
    """
    대출되지 않은 도서에 반납을 요청했을 경우 발생하는 에러
    """
