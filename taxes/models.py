from django.db import models

# Create your models here.

class Payable(models.Model):
    LIGHT = 'L'
    GAS = 'G'
    SERVICE_CHOICES = [
        (LIGHT, 'Luz'),
        (GAS, 'Gas'),
    ]
    
    PENDING = 'PE'
    PAID = 'PA'
    PAYMENT_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
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


class Transaction(models.Model):

    DEBIT_CARD = 'debit_card'
    CREDIT_CARD = 'credit_card'
    CASH = 'cash'
    PAYMENT_CHOICES = [
        (DEBIT_CARD, 'Debit Card'),
        (CREDIT_CARD, 'Credit Card'),
        (CASH, 'Cash'),
    ]
    payment_method = models.CharField(max_length=11, choices=PAYMENT_CHOICES)
    card_number = models.CharField(max_length=12, null=True, blank=True)
    payment_import = models.DecimalField(max_digits=12, decimal_places=2)
    barcode = models.CharField(max_length=20, primary_key=True)
    payment_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f'{self.barcode} - {self.payment_import}'

    