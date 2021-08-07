# Generated by Django 3.2 on 2021-08-01 15:04

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '이미 존재하는 ID 입니다.'}, help_text='150자 이내, 영문자, 숫자, @/./+/-/_ 만 사용 가능', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='ID'),
        ),
    ]