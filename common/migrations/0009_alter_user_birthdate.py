# Generated by Django 3.2 on 2021-07-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_alter_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(),
        ),
    ]