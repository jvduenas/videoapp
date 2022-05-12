from tabnanny import verbose
from django.db import models

# Create your models here.

class Vids(models.Model):

    class Meta:
        verbose_name_plural = "Vids"
    
    caption=models.CharField(max_length=1000)
    date = models.DateField(verbose_name="Upload Date")
    remarks = models.CharField(max_length=200, verbose_name="Comments")
    thumbnail= models.ImageField(upload_to="images", null=True, blank=True)
    video=models.FileField(upload_to="videos", null=True, blank=True)
    playlist=models.CharField(max_length=100, default="uncategorized", null=True, blank=True)

    def __str__(self):
        return self.caption


class Featured(models.Model):

    class Meta:
        verbose_name_plural = "Featured"
    
    title=models.CharField(max_length=100)
    date_uploaded=models.DateField(verbose_name="Date Uploaded")
    description=models.CharField(max_length=200)
    featured=models.ForeignKey(Vids, on_delete=models.CASCADE)



class Category(models.Model):

    class Meta:
        verbose_name_plural = "Category"

    name = models.CharField(max_length=100)
    category=models.ForeignKey(Vids, on_delete=models.CASCADE, null=True, default="Uncategorized")

    def __str__(self):
        return self.name



class Events(models.Model):
    class Meta:
        verbose_name_plural = "Events"

    title=models.CharField(max_length=200)
    image=models.FileField(upload_to='images', null=True, blank=True)
    narrative=models.CharField(max_length=5000)

    def __str__(self):
        return self.title
