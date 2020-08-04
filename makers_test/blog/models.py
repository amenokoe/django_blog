from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

# Post -> Category

# Category1 Category2
# |
# Post1 Post2 Post3


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(null=True, blank = True, upload_to='posts')

    def __str__(self):
        return self.title
