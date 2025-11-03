from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="recipes/covers/%Y/%m/%d/")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servigns_unit
# preparation_step
# preparation_step_is_time
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)