# Generated by Django 3.2.5 on 2021-07-18 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(upload_to='uploads/photos/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.customer')),
            ],
        ),
    ]
