# Generated by Django 4.1.7 on 2023-06-02 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(max_length=250, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Teacher', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
