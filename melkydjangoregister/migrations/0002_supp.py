# Generated by Django 4.1.7 on 2023-03-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melkydjangoregister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supp_name', models.CharField(max_length=30)),
                ('supp_item', models.CharField(max_length=30)),
                ('supp_phone', models.CharField(max_length=30)),
                ('supp_email', models.EmailField(max_length=30)),
            ],
        ),
    ]
