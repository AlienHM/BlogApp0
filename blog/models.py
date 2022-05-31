
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date, datetime

# # Create your models here.

class Category (models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
        # return reverse('post_detail', kwargs={"pk": self.pk})
class Post (models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="coding")
    snip=models.CharField(max_length=100, default="Click above to read more...")
    likes = models.ManyToManyField(User, related_name='blog_posts')

    # body=models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author) 
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})