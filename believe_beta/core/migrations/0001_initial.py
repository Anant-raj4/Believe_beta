# Generated by Django 4.0.4 on 2022-04-20 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_name', models.CharField(max_length=100)),
                ('consumer_email', models.EmailField(max_length=200)),
                ('consumer_puja', models.CharField(choices=[('GP', 'Ganesh Puja'), ('LP', 'Lakshmi Puja'), ('SP', 'Satyanarayan Puja')], max_length=100)),
                ('consumer_pandit', models.CharField(choices=[('A', 'Abhi'), ('B', 'Shado'), ('C', 'Lado'), ('d', 'Hado')], max_length=2)),
                ('consumer_age', models.IntegerField(default=18)),
                ('puja_date', models.DateField()),
                ('puja_time', models.TimeField()),
            ],
        ),
    ]