from django.db import models

class Menus(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Products(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    product = models.ForeignKey('Products',on_delete=models.CASCADE) 

    class Meta:
        db_table = 'images'

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 6, decimal_places = 2, null=True)
    sodium_mg = models.DecimalField(max_digits = 6, decimal_places = 2, null=True)
    saturated_fat_g = models.DecimalField(max_digits = 6, decimal_places = 2, null=True)
    sugars_g = models.DecimalField(max_digits = 6, decimal_places = 2, null=True)
    protein_g = models.DecimalField(max_digits = 6, decimal_places = 2, null=True)
    caffeine_mg = models.DecimalField(max_digits = 6, decimal_places = 2, null=True)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)
    product = models.OneToOneField('Products', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Allergies(models.Model):
    name = models.CharField(max_length=45)
    product_id = models.ManyToManyField(Products, through = 'Allergies_Products')

    class Meta:
        db_table = 'allergies'

class Allergies_Products(models.Model):
    allergy = models.ForeignKey('Allergies', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergies_products'