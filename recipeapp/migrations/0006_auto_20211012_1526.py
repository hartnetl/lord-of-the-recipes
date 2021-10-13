# Generated by Django 3.2.8 on 2021-10-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0005_auto_20211011_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('BFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner'), ('DRINKS', 'Drinks'), ('OTHER', 'Snacks')], default='OTHER', max_length=9),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]