# Generated by Django 2.2.12 on 2020-07-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200709_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='sex',
            field=models.CharField(choices=[('m', 'Мужс.'), ('f', 'Женс.')], default='пол', max_length=1, verbose_name='Пол'),
            preserve_default=False,
        ),
    ]