from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Review
from django.views.generic import ListView
from .forms import BookForm, ReviewForm


class ListBookView(ListView):
    def get(self, request):
        books = Book.objects.all().order_by("category")
        return render(request, "book/list.html", {"books": books})


class DetailBookView(ListView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        reviews = Review.objects.filter(book=book)
        return render(request, "book/detail.html", {"book": book, "reviews": reviews})


class CreateBookView(ListView):
    def get(self, request):
        form = BookForm()
        return render(request, "book/create.html", {"form": form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book:book_list")
        return render(request, "book/create.html", {"form": form})


class UpdateBookView(ListView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, "book/update.html", {"form": form, "book": book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book:book_list")
        return render(request, "book/update.html", {"form": form})


class DeleteBookView(ListView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, "book/delete_confirm.html", {"book": book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect("book:book_list")


class ReviewBookView(ListView):
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
