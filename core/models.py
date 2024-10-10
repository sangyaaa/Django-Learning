from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=31)
    description = models.TextField(
        null=True, blank=True
    )

class product(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("author", on_delete=models.PROTECT, related_name="product")#protect ko sattaa ma cascade->delete garnye, set_null,set_default, do_nothing
    #image = models.ImageField()
    PageCount = models.IntegerField()
    weight = models.IntegerField()
    language = models.CharField(max_length=50)
    isbn_number = models.CharField(max_length=127, unique=True)
    price = models.FloatField()
    genre = models.ForeignKey("genre", on_delete=models.PROTECT, related_name="product")
    avg_review = models.FloatField()
class author(models.Model):
    name=models.CharField(max_length=50)
class genre(models.Model):
    name=models.CharField(max_length=30)


    
