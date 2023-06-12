from typing import Optional

from django.contrib.auth.models import User
from django.db import models
from django.db.models import QuerySet, Q
from django.shortcuts import get_object_or_404

from book_borrow.models import BorrowHistory

class Book(models.Model):
    """
    책 모델
    """
    author = models.ForeignKey('author.Author', null=False, blank=False, on_delete=models.CASCADE, verbose_name='저자')
    title = models.CharField(max_length=50, verbose_name='제목')
    published_at = models.DateField(verbose_name='출간일')

    class Meta:
        db_table = 'books'
        verbose_name = '도서'
        verbose_name_plural = '도서 목록'

    @classmethod
    def get_all_books(cls) -> QuerySet['Book']:
        """
        저장된 모든 도서의 목록을 가져오는 함수
        :return: 저장된 모든 도서의 목록
        """
        return cls.objects.all()

    @classmethod
    def get_all_books_order_by_published_at_desc(cls) -> QuerySet['Book']:
        """
        MIDTERM EXAM 4 : 아래 코드가 정상 작동하도록 고치세요.

        저장된 모든 도서의 목록을 출간일 내림차순으로 가져오는 함수
        :return: 저장된 모든 도서의 목록 (출간일 내림차순 정렬 적용)
        """
        return Book.objects.filter(book=self).order_by('-borrowed_at')


    @classmethod
    def get_single_book_by_id(cls, book_id: int) -> 'Book':
        """
        id가 book_id인 도서 객체 하나를 반환한다.
        :raise django.http.Http404: 해당 id를 가지는 Book이 존재하지 않는 경우
        :return: id가 book_id Book 객체
        """
        return get_object_or_404(cls, id=book_id)

    def get_borrow_histories_order_by_borrowed_at_desc(self) -> QuerySet[BorrowHistory]:
        """
        해당 도서의 대출 이력 목록을 borrowed_at 기준 내림차순으로 정렬하여 반환한다.
        :return: 해당 도서의 대출 이력목록 (borrowed_at 기준 내림차순)
        """
        return BorrowHistory.objects.filter(book=self).order_by('-borrowed_at')

    def get_latest_borrow_history(self) -> Optional['BorrowHistory']:
        """
        해당 도서에 연결된 대출 이력 중 가장 최근에 만들어진(borrowed_at이 가장 큰)
        대출 이력을 반환한다. 대출 이력이 없는 경우, None을 반환한다.
        :return: None, 또는 해당 도서에 대한 가장 최근의 대출 기록
        """
        borrow_histories = self.get_borrow_histories_order_by_borrowed_at_desc()
        return borrow_histories.first()

    def is_checked_out(self) -> bool:
        """
        해당 도서의 대출 여부를 확인한다.
        :return: 현재 대출 중인 경우 True, 그렇지 않은 경우 False
        """
        borrow_histories = self.get_borrow_histories_order_by_borrowed_at_desc()
        return borrow_histories.filter(Q(returned_at=None)).exists()

    def borrow(self, user_id: int) -> 'BorrowHistory':
        """
        MIDTERM EXAM 6 : 아래 명세에 맞게 코드를 완성하세요.

        해당 도서를 대출 처리한다.
        :param user_id: 대출을 요청한 사용자의 id
        :raises AlreadyCheckedOutBookException: 이미 대출 중인 도서에 대출을 요청한 경우
        :return: 생성된 대출 이력
        """
        return None

    def give_back(self) -> 'BorrowHistory':
        """
        MIDTERM EXAM 7 : 아래 명세에 맞게 코드를 완성하세요.

        해당 도서를 반납 처리한다.
        :raises book_borrow.exceptions.BookHasNoBorrowHistory: 대출 이력이 없는 도서에 반납을 요청한 경우
        :raises book_borrow.exceptions.BookIsNotCheckedOutException: 이미 반납된 도서에 반납을 요청한 경우
        :return: 반납 처리된 대출 이력
        """
        return None
