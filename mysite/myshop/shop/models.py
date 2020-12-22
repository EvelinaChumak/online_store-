# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import AbstractUser





class Categories(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category',
                        args=[self.slug])



class Users(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='user_id')
    patronymic = models.TextField(max_length=64, blank=True, null=True)
    phone_number = models.IntegerField(max_length=11, blank=True, null=True)
    adress = models.TextField(max_length=256, blank=True, null=True)
    orders = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return str(self.user)


class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'

    def __str__(self):
        return self.name


class Orders(models.Model):
    id_client = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='id_client')
    id_products = models.ForeignKey('Products', models.CASCADE, db_column='id_products')
    id_order = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    data_of_issue = models.CharField(max_length=128,blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('id_client', 'id_products', 'id_order', 'size'),)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return self.id_order

def image_folder1(instance, filename):
    filename = str(1) + '.' + filename.split('.')[1]
    return "image_for_products/{0}/{1}".format(str(instance.slug), filename)

def image_folder2(instance, filename):
    filename = str(2) + '.' + filename.split('.')[1]
    return "image_for_products/{0}/{1}".format(str(instance.slug), filename)

def image_folder3(instance, filename):
    filename = str(3) + '.' + filename.split('.')[1]
    return "image_for_products/{0}/{1}".format(str(instance.slug), filename)

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=200, db_index=True)
    size_xs = models.PositiveSmallIntegerField()
    size_s = models.PositiveSmallIntegerField()
    size_m = models.PositiveSmallIntegerField()
    size_l = models.PositiveSmallIntegerField()
    size_xl = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    id_category = models.ForeignKey(Categories, models.CASCADE, db_column='id_category')
    id_collection = models.ForeignKey(Collection, models.CASCADE, db_column='id_collection', blank=True, null=True)
    number_of_sold = models.IntegerField()
    image_1 = models.ImageField(upload_to=image_folder1, blank=True)
    image_2 = models.ImageField(upload_to=image_folder2, blank=True)
    image_3 = models.ImageField(upload_to=image_folder3, blank=True)

    class Meta:
        ordering = ['number_of_sold']
        managed = False
        db_table = 'products'

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

