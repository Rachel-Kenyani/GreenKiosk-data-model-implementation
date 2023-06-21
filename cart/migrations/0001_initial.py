# Generated by Django 4.2.1 on 2023-06-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32)),
                ('total_price', models.DecimalField(decimal_places=4, max_digits=6)),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
    ]
