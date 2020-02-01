from django.contrib.auth import get_user_model
from django.db import migrations


products = [
    {
        'name': f'Товар{i}',
        'code':  f'{i}' * 8,
        'price':  f'{i}{i}.{i}{i}',
    }
    for i in range(1, 4)
]


def get_models(apps):
    return (
        get_user_model(),
        apps.get_model("questioning_app", "Product")
    )


def create_data(apps, schema_editor):
    User, Product = get_models(apps)
    User.objects.create_superuser('qwerty', '', 'qwerty')
    User.objects.create_user('guest', password='guest')
    Product.objects.bulk_create([Product(**p) for p in products])


def delete_data(apps, schema_editor):
    User, Product = get_models(apps)
    User.objects.filter(username__in=('qwerty', 'guest')).delete()
    Product.objects.filter(name__in=categories_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('questioning_app', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_data, delete_data),
    ]
