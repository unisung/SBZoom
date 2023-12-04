# Generated by Django 4.2.7 on 2023-12-04 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guName', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('quarter', models.CharField(max_length=20)),
                ('ilban', models.DecimalField(decimal_places=0, max_digits=10)),
                ('franchise', models.DecimalField(decimal_places=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=0, max_digits=10)),
                ('sales', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]
