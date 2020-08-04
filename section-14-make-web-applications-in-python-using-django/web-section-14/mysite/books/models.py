from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.


class Book(models.Model):

    def get_absolute_url(self):
        return reverse("book:details", kwargs={"pk": self.pk})
    
    def __str__(self):
        
        return self.name + '-' + self.author
    
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    book_image = models.CharField(max_length=100)
