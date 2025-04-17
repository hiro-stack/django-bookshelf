from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import SignUpForm
from django.views import View


class UserLoginView(LoginView):
    template_name = "registration/login.html"


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("book:book_list")


class UserSignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
        return render(request, "registration/signup.html", {"form": form})


login_view = UserLoginView.as_view()
logout_view = UserLogoutView.as_view()
signup_view = UserSignUpView.as_view()
