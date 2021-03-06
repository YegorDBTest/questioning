from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse

from questioning_app.forms import QuestioningForm, OrderForm
from questioning_app.models import Product


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

    def form_valid(self, *args, **kwargs):
        response = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return response


class ShowcaseView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    '''
    Страница с витриной.
    '''

    login_url = '/'
    template_name = 'questioning_app/showcase.html'
    permission_required = 'questioning_app.showcase_allowed'
    model = Product


class OrderView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''
    Страница с заказом.
    '''

    login_url = '/'
    template_name = 'questioning_app/order.html'
    permission_required = 'questioning_app.showcase_allowed'
    form_class = OrderForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        products_ids = self.request.COOKIES.get('order-products')
        if products_ids:
            products = Product.objects.filter(id__in=products_ids.split(','))
            context['products'] = products
            context['total_price'] = products.aggregate(Sum('price'))['price__sum']
        return context
