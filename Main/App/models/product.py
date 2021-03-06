from django.db import models
import uuid


class Types(models.Model):
    type = models.CharField(max_length=100)
    on_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.type


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200)
    avatar = models.FileField(upload_to='image/product', blank=True, null=True, default="avatar.jpg")
    sold = models.IntegerField(default=0)
    type = models.ForeignKey(Types, related_name='products', on_delete=models.CASCADE)
    from_saleprice = models.IntegerField(default=0)
    to_saleprice = models.IntegerField(default=0)
    comments = models.TextField(max_length=1000, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    on_delete = models.BooleanField(default=False)


    def __str__(self):
        return self.name + ": " + str(self.on_delete)


class Details(models.Model):
    product = models.ForeignKey(Products, related_name="details", on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    saleprice = models.IntegerField()
    amount = models.IntegerField(default=0)
    on_delete = models.BooleanField(default=False)


    def __str__(self):
        return str(self.product) + ": " + self.color + ": " + self.size


class Amounts(models.Model):
    detail = models.ForeignKey(Details, related_name="amounts", on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    amount = models.IntegerField()
    note = models.CharField(max_length=100, blank=True)
    is_plus = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.detail) + ": " + str(self.amount)


class Image(models.Model):
    product = models.ForeignKey(Products, related_name="image", on_delete=models.CASCADE)
    img = models.FileField(upload_to='image/product')

    def __str__(self):
        return "Images prduct: " + str(self.product)


class Describe(models.Model):
    product = models.ForeignKey(Products, related_name="describe", on_delete=models.CASCADE)
    # header = models.CharField(max_length=100)
    context = models.CharField(max_length=200)

    def __str__(self):
        return str(self.product) + ": " + self.context


class Description(models.Model):
    product = models.ForeignKey(Products, related_name='description', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, null=True, blank=True)
    img = models.FileField(upload_to='image/description/', null=True, blank=True)

    def __str__(self):
        return str(self.product)+ " - " + str(self.text)