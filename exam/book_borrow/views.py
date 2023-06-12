from django.shortcuts import render, redirect

from book.models import Book
from common.models import get_all_users


def book_borrow(request, book_id: int):
    """
    해당 도서에 대한 대출 처리를 수행하는 View
    - WARNING : AlreadyCheckedOutBookException에 대한 handling 수행 X
    """
    # 대출 요청 도서
    book = Book.get_single_book_by_id(book_id)

    if request.method == 'POST':
        borrow_user_id = int(request.POST['borrow-user'])
        borrowed_history = book.borrow(borrow_user_id)
        return redirect('book:detail', book.id)
    else:
        context = {
            'book': book,
            'users': get_all_users(),  # 모든 유저는 대출 가능
        }
        return render(request, 'book/book-borrow.html', context)


def book_give_back(request, book_id: int):
    """
    해당 도서에 대한 반납 처리를 수행하는 View
    - WARNING : BookHasNoRentalsException에 대한 handling 수행 X
    """
    # 반납 요청 도서
    book = Book.get_single_book_by_id(book_id)
    # 반납 처리된 대출 이력
    returned_history = book.give_back()
    return redirect('book:detail', book.id)
