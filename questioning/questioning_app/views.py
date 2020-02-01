from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView
from django.urls import reverse

from questioning_app.forms import QuestioningForm


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


class QuestioningView(LoginRequiredMixin, CreateView):
    '''
    Страница анкетирования.
    '''

    login_url = '/'
    template_name = 'questioning_app/questioning.html'
    form_class = QuestioningForm
    success_url = '/showcase/'

    def post(self, request, *args, **kwargs):
        self._request = request

        return super().post(request, *args, **kwargs)

    def form_valid(self, *args, **kwargs):
        response = super().form_valid(*args, **kwargs)
        login(self._request, self.object)

        return response
