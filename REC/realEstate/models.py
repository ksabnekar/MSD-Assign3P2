from django.db import models
from django.utils import timezone

purpose = (
    ('For Sale', 'For Sale'),
    ('For Lease', 'For Lease')
)

type = (
    ('Condo', 'Condo'),
    ('House', 'House'),
    ('Apartment', 'Apartment')
)


# Customer Model
class Customer(models.Model):
    cust_id = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, default='Null')
    phone = models.CharField(max_length=50)
    maxPrice = models.IntegerField()
    minPrice = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.fname)


# Properties Model
class Property (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customers')
    prop_number = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=type, default='Condo', blank=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    dimension = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    bed = models.CharField(max_length=50)
    bath = models.CharField(max_length=50)
    build = models.CharField(max_length=50)
    purpose = models.CharField(max_length=10, choices=purpose, default='For Sale', blank=False)
    status = models.BooleanField(default='True')

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

