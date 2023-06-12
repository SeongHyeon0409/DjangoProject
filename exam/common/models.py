from django.contrib.auth.models import User
from django.db.models import QuerySet


def get_all_users() -> QuerySet[User]:
    """
    저장된 모든 사용자의 목록을 가져오는 함수
    """
    return User.objects.all()


def get_single_user_by_id(user_id: int) -> User:
    """
    id가 user_id인 사용자를 반환한다.
    :raise django.http.Http404: 해당 id를 가지는 User가 존재하지 않는 경우
    """
    return User.objects.get(id=user_id)
