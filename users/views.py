from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import MyUserCreateForm
from .models import MyUser


class Register(UserPassesTestMixin, CreateView):
    model = MyUser
    form_class = MyUserCreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def test_func(self):
        return self.request.user.is_anonymous


class Login(UserPassesTestMixin, LoginView):
    template_name = 'users/login.html'

    def test_func(self):
        return self.request.user.is_anonymous


class Logout(LogoutView):
    pass
