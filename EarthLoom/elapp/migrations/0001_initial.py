# Generated by Django 4.1.4 on 2024-02-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('farmer', 'Farmer'), ('customer', 'Customer')], max_length=20)),
            ],
        ),
    ]
