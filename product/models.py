from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=5)
    num_pages = models.IntegerField()
    is_published = models.BooleanField()
    description = models.TextField(null=True, blank=True)
    qualification = models.CharField(max_length=10, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        # return self.title
        return f"{self.title} - {self.author} - {self.num_pages}"

# class == book table
