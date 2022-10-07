from django.db import models

# Create your models here.

class Auto(models.Model):
    brand = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    year = models.PositiveIntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField('Image',upload_to='pictures/', blank=True, null=True)
    
    def __str__(self):
        return (self.brand +'  ' + self.model +' ' + str(self.year) +' $' + str(self.price) + ' '+ self.image.name)