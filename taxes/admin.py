from django.contrib import admin
from taxes.models import Payable, Transaction

# Register your models here.

admin.site.register(Payable)
admin.site.register(Transaction)