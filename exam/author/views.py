from django.shortcuts import render

from author.models import Author


def author_list(request):
    """
    시스템에 등록된 모든 작가(Author)의 목록을 표시하는 View
    """
    context = {
        'authors': Author.get_all_authors()
    }
    return render(request, 'author/list.html', context)


def author_detail(request, author_id: int):
    """
    id가 author_id인 작가(Author)에 대한 상세 정보 및 출간 도서를 표시하는 View
    """
    context = {}

    author = Author.get_single_author_by_id(author_id)
    context['author'] = author

    published_books = author.get_published_books()
    context['published_books'] = published_books

    return render(request, 'author/detail.html', context)
