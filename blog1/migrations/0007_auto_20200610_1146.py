# Generated by Django 3.0.3 on 2020-06-10 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog1', '0006_auto_20200610_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent11',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
