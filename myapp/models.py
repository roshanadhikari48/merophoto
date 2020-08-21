from django.db import models


# Create your models here.

# create categories model
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# create Image model
class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField( null=True)
    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title