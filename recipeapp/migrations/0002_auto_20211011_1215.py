# Generated by Django 3.2.8 on 2021-10-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='unit',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='nutrition',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(max_length=20),
        ),
    ]