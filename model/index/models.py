from django.db import models

# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class News(models.Model):
    pr_name = models.CharField(max_length=64)
    pr_description = models.CharField(max_length=256)
    pr_date = models.DateField(blank=True, null=True)
    pr_photo = models.ImageField(upload_to='pr_img', null=True, blank=True)
    pr_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.pr_name


