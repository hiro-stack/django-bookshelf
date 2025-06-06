from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("detail/<int:pk>/", views.book_detail, name="book_detail"),
    path("create/", views.book_create, name="book_create"),
    path("update/<int:pk>/", views.book_update, name="book_update"),
    path("delete/<int:pk>/", views.book_delete, name="book_delete"),
    path("review/<int:pk>/", views.book_review, name="book_review"),
]
