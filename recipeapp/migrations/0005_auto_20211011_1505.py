# Generated by Django 3.2.8 on 2021-10-11 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0004_auto_20211011_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(related_name='recipe_category', to='recipeapp.Category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipeapp.recipe')),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
    ]
