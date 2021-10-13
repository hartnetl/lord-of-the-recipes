from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


# Recipe model
STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY_CHOICE = (
    ("BFAST", "Breakfast"),
    ("LUNCH", "Lunch"),
    ("DINNER", "Dinner"),
    ("DRINKS", "Drinks"),
    ("OTHER", "Other"),
)


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    date_created = models.DateTimeField(auto_now_add=True)
    about = models.TextField(blank=True)
    nutrition = models.TextField(blank=True)
    servings = models.PositiveIntegerField()
    prep_time = models.CharField(max_length=20)
    cook_time = models.CharField(max_length=20)
    method = models.TextField()
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    approval = models.BooleanField(default=False)
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICE,  default='OTHER')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


# ingredients model
class Ingredients(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    item = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.item} {self.quantity}  {self.unit}"


# Comments model
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return f"Comment {self.message} by {self.name}"

