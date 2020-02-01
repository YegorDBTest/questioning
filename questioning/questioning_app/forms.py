from django import forms
from django.contrib.auth.models import Permission
from django.utils import timezone

from questioning_app.models import User


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

    def full_clean(self):
        timestamp = timezone.now().strftime('%y%m%d%H%M%S%f')
        self.data = self.data.copy()
        self.data['username'] = timestamp
        self.data['password'] = timestamp
        return super().full_clean()

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.user_permissions.add(
            Permission.objects.get(codename='showcase_allowed')
        )
        return user
