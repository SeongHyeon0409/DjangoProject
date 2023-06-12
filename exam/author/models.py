from django.db import models
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from book.models import Book


class Author(models.Model):
    """
    책의 저자 모델
    """
    name = models.CharField(max_length=20, verbose_name='이름')
    description = models.TextField(verbose_name='저자 소개')

    class Meta:
        db_table = 'authors'
        verbose_name = '저자'
        verbose_name_plural = '저자 목록'

    @classmethod
    def get_all_authors(cls) -> QuerySet['Author']:
        """
        MIDTERM EXAM 1 : 아래 코드가 정상 작동하도록 고치세요.

        저장된 모든 작가의 목록을 가져오는 함수
        :return: 저장된 모든 작가의 목록
        """
        return cls.objects.all()
    def get_single_author_by_id(cls, author_id: int) -> 'Author':
        """
        MIDTERM EXAM 2 : 아래 코드가 정상 작동하도록 고치세요.

        id가 author_id인 작가 객체 하나를 반환한다.
        :raise django.http.Http404: 해당 id를 가지는 Author가 존재하지 않는 경우
        :return: id가 author_id인 Author 객체
        """
        return get_object_or_404(cls, id=author_id)

    def get_published_books(self) -> QuerySet[Book]:
        """
        MIDTERM EXAM 3 : 아래 코드가 정상 작동하도록 고치세요.
)

    @classmethod
        해당 저자가 쓴 모든 도서의 목록을 반환한다.
        :return: 해당 저자가 쓴 모든 도서의 목록
        """
        return None
