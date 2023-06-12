from django.shortcuts import render

from book.models import Book


def book_list(request):
    """
    시스템에 등록된 모든 도서(Book)의 목록을 표시하는 View
    단, query parameter의 sort 값이 'published_at_desc'인 경우 published_at 기준
    내림차순 정렬하여 목록을 표시한다.
    """
    context = {}

    sort = request.GET.get('sort')
    if sort == 'published_at_desc':
        books = Book.get_all_books_order_by_published_at_desc()
    else:
        books = Book.get_all_books()

    context['books'] = books

    return render(request, 'book/list.html', context)


def book_detail(request, book_id: int):
    """
    id가 book_id인 도서(Book)에 대한 상세 정보 및 해당 도서의 대출 이력을 표시하는 View
    """
    context = {}

    # 대상 도서
    book = Book.get_single_book_by_id(book_id)
    context['book'] = book

    # NOTICE : 단, 아래 코드는 문제 3-1부터 사용됩니다. (풀지 않아도 삭제하지 마세요!)
    borrow_histories = book.get_borrow_histories_order_by_borrowed_at_desc()
    context['borrow_histories'] = borrow_histories

    return render(request, 'book/detail.html', context)
