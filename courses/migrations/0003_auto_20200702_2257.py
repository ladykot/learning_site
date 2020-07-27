# Generated by Django 2.2.12 on 2020-07-02 19:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('date_joined', models.DateTimeField(verbose_name='Дата регистрации')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата регистрации'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
    ]