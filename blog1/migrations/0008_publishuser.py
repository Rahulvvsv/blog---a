# Generated by Django 3.0.3 on 2020-06-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0007_auto_20200610_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('story', models.CharField(max_length=5000)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
