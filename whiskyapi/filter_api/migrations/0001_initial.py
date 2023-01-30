# Generated by Django 4.1.5 on 2023-01-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Whisky',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_house_names', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_date', models.DateField()),
                ('url', models.URLField()),
                ('distillery', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('cask', models.CharField(max_length=255)),
                ('vintage', models.IntegerField()),
                ('bottled_year', models.IntegerField()),
                ('abv', models.DecimalField(decimal_places=2, max_digits=4)),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bottler', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField()),
                ('scraped_at', models.DateTimeField()),
                ('image', models.URLField()),
            ],
        ),
    ]