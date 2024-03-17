# Generated by Django 5.0.1 on 2024-03-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('designation', models.CharField(choices=[('HR', 'HR'), ('Manager', 'Manager'), ('Sales', 'Sales'), ('Developer', 'Developer'), ('Others', 'Others')], max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('BSC', 'Bachelor of Science'), ('IT', 'Information Technology'), ('BCOM', 'Bachelor of Commerce'), ('CA', 'Chartered Accountancy'), ('MBA', 'Master of Business Administration')], max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
