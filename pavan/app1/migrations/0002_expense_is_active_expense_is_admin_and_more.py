# Generated by Django 5.0.1 on 2024-01-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expense',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('sel', 'select your gender'), ('Health', 'Health'), ('Electronics', 'Electronics'), ('Travel', 'Travel'), ('Education', 'Education'), ('Books', 'Books'), ('Others', 'Others')], max_length=90),
        ),
    ]
