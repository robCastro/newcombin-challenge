from django.db import models

# Create your models here.

class Payable(models.Model):
    SERVICE_CHOICES = [
        ('L', 'Luz'),
        ('G', 'Gas'),
    ]
    PAYMENT_CHOICES = [
        ('PE', 'Pending'),
        ('PA', 'Paid'),
    ]
    barcode = models.CharField(max_length=20, primary_key=True)
    service_type = models.CharField(max_length=2, choices=SERVICE_CHOICES)
    description = models.CharField(max_length=50)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False)
    service_import = models.DecimalField(max_digits=12, decimal_places=2)
    payment_status = models.CharField(max_length=2, choices=PAYMENT_CHOICES)

    class Meta:
        verbose_name = "payable"
        verbose_name_plural = "payables"

    def __str__(self):
        return f'{self.barcode} - {self.description}'

