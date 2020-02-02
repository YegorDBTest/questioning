from django.urls import include, path

from questioning_app import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('guest_login', views.GuestLoginView.as_view(), name='guest-login'),
    path('questioning/', views.QuestioningView.as_view(), name='questioning'),
    path('showcase/', views.ShowcaseView.as_view(), name='showcase'),
    path('order/', views.OrderView.as_view(), name='order'),
]
