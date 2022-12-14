# Generated by Django 4.1.2 on 2022-10-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('image', models.URLField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]
