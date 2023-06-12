from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404


class BorrowHistory(models.Model):
    """
    책 대출 이력
    """
    book = models.ForeignKey('book.Book', null=False, blank=False, on_delete=models.CASCADE, verbose_name='대상 도서')
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name='대출 사용자')
    borrowed_at = models.DateTimeField(auto_now_add=True, verbose_name='대출일')
    return_deadline = models.DateTimeField(verbose_name='반납 기한')
    returned_at = models.DateTimeField(null=True, blank=True, verbose_name='반납일')

    class Meta:
        db_table = 'book_rentals'
        verbose_name = '대출 이력'
        verbose_name_plural = '대출 이력 목록'

    @classmethod
    def get_all_borrow_histories(cls) -> QuerySet['BorrowHistory']:
        """
        저장된 도서 대출 이력 목록을 가져오는 함수
        :return: 저장된 모든 도서 대출 이력 목록
        """
        return cls.objects.all()

    @classmethod
    def get_single_borrow_history_by_id(cls, rental_id: int) -> 'BorrowHistory':
        """
        id가 rental_id인 도서 대출 이력 객체 하나를 반환한다.
        :raise django.http.Http404: 해당 id를 가지는 BorrowHistory가 존재하지 않는 경우
        :return: id가 rental_id인 BorrowHistory 객체
        """
        return get_object_or_404(cls, id=rental_id)

    def is_overdue(self):
        """
        해당 대출 이력의 반납 기한 초과 여부를 반환한다.
        :return: 반납 기한과 현재 일시가 같거나 현재 일시가 반납 기한을 넘긴 경우 True, 그렇지 않은 경우 False
        """
        return self.return_deadline <= datetime.now()

    def is_returned(self):
        """
        해당 대출 이력이 반납 여부를 확인한다.
        returned_at이 None인 경우 미반납, None이 아닌 경우 반납으로 한다.
        :return: 해당 대출 이력이 반납 상태인 경우 True, 그렇지 않은 경우 False
        """
        return self.returned_at is not None

    def give_back(self) -> None:
        """
        해당 대출 이력을 반납 처리한다.
        해당 대출 이력의 상태를 체크하지 않고, 항상 returned_at을 갱신하기만 한다.
        """
        self.returned_at = datetime.now()
        self.save()

    @staticmethod
    def get_seven_days_later(given_dt: datetime) -> datetime:
        """
        전달 받은 datetime로부터 7일 후의 값을 가지는 datetime을 반환한다.
        (반납 기한 설정을 위해 사용됨)
        :param given_dt: 계산에 사용할 datetime 객체
        :return: given_at으로부터 7일 후의 값을 가지는 datetime 객체
        """
        return given_dt + timedelta(days=7)

    @staticmethod
    def get_seven_days_before(given_dt: datetime) -> datetime:
        """
        전달 받은 datetime로부터 7일 전의 값을 가지는 datetime을 반환한다.
        :param given_dt: 계산에 사용할 datetime 객체
        :return: given_at으로부터 7일 전의 값을 가지는 datetime 객체
        """
        return given_dt - timedelta(days=7)
