from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, RedirectView
from django.urls import reverse


class IndexView(TemplateView):
    '''
    Главная. Пользователь может залогинится как гость.
    '''

    template_name = 'questioning_app/index.html'


class GuestLoginView(RedirectView):
    '''
    Вход в систему за гостевую учетку.
    '''

    def get(self, request, *args, **kwargs):
        guest = authenticate(request, username='guest', password='guest')
        login(request, guest)

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('questioning')


class QuestioningView(LoginRequiredMixin, TemplateView):
    '''
    Страница анкетирования.
    '''

    template_name = 'questioning_app/questioning.html'
