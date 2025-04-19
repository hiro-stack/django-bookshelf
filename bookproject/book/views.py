from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review
from django.views.generic import ListView
from .forms import BookForm, ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE


class ListBookView(ListView):
    def get(self, request):
        books = Book.objects.all().order_by("-id")

        paginator = Paginator(books, ITEM_PER_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        ranking_list = Book.objects.annotate(average_rate=Avg("review__rate")).order_by(
            "-average_rate"
        )[:5]

        return render(
            request,
            "book/list.html",
            {"books": page_obj, "ranking_list": ranking_list, "page_obj": page_obj},
        )


class DetailBookView(ListView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        reviews = Review.objects.filter(book=book)
        return render(request, "book/detail.html", {"book": book, "reviews": reviews})


class CreateBookView(LoginRequiredMixin, ListView):
    def get(self, request):
        form = BookForm()
        return render(request, "book/create.html", {"form": form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book:book_list")
        return render(request, "book/create.html", {"form": form})


class UpdateBookView(LoginRequiredMixin, ListView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, "book/update.html", {"form": form, "book": book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if request.user != book.user:
            raise PermissionDenied("You do not have permission to edit this book.")

        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book:book_list")
        return render(request, "book/update.html", {"form": form})


class DeleteBookView(LoginRequiredMixin, ListView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, "book/delete_confirm.html", {"book": book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if request.user != book.user:
            raise PermissionDenied("You do not have permission to edit this book.")
        book.delete()
        return redirect("book:book_list")


class ReviewBookView(LoginRequiredMixin, ListView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = ReviewForm()
        return render(request, "book/review.html", {"form": form, "book": book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect("book:book_detail", pk=pk)
        return render(request, "book/review.html", {"form": form, "book": book})


book_list = ListBookView.as_view()
book_detail = DetailBookView.as_view()
book_create = CreateBookView.as_view()
book_update = UpdateBookView.as_view()
book_delete = DeleteBookView.as_view()
book_review = ReviewBookView.as_view()
