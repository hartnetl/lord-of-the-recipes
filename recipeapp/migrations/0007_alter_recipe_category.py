# Generated by Django 3.2.8 on 2021-10-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0006_auto_20211012_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('BFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner'), ('DRINKS', 'Drinks'), ('OTHER', 'Other')], default='OTHER', max_length=9),
        ),
    ]
