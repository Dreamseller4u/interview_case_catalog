from turtle import title
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

# Create your models here.

class Categories (MPTTModel):
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', 
                            on_delete=models.PROTECT, 
                            null=True,
                            blank=True, 
                            related_name='children', 
                            verbose_name='Родительская категория')
    slug = models.SlugField()
    
    class MPTTMeta:
        order_iteration_by = ['title']        
    
    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    slug = models.SlugField()
    category = TreeForeignKey('Categories', on_delete=models.PROTECT, related_name='products', verbose_name="Категория",)
    imgage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None , blank = True )
    spec = models.FileField( upload_to=None, max_length=100, blank = True)
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        index_together = (('id', 'slug'), )
        
    def __str__(self):
        return self.title 
