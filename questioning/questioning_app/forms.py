from django import forms
from django.contrib.auth.models import Permission
from django.utils import timezone

from questioning_app.models import User, Order


class QuestioningForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'age',
            'occupation',
            'email',
            'facebook_username',
        )
        widgets = {
            'username': forms.HiddenInput(),
            'password': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_required_fields()

    def _set_required_fields(self):
        for field_name in ('first_name', 'last_name', 'age', 'occupation'):
            self.fields[field_name].required = True

    def _check_same_user_exists(self, cleaned_data):
        same_user_exists = (
            User.objects
            .filter(
                first_name=cleaned_data.get('first_name'),
                last_name=cleaned_data.get('last_name'),
                age=cleaned_data.get('age'),
                occupation=cleaned_data.get('occupation'),
                email=cleaned_data.get('email'),
                facebook_username=cleaned_data.get('facebook_username'),
            )
            .exists()
        )
        if same_user_exists:
            raise forms.ValidationError(
                'Пользователь с такими данными уже существует. '
                'Вы можете скорректировать данные или завершить сессию.'
            )

    def full_clean(self):
        timestamp = timezone.now().strftime('%y%m%d%H%M%S%f')
        self.data = self.data.copy()
        self.data['username'] = timestamp
        self.data['password'] = timestamp
        return super().full_clean()

    def clean(self):
        cleaned_data = super().clean()
        self._check_same_user_exists(cleaned_data)
        return cleaned_data

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.user_permissions.add(
            Permission.objects.get(codename='showcase_allowed')
        )
        return user


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'products')
