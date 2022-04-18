import random
from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import transaction
from taxes.models import Payable, Transaction


class Command(BaseCommand):
    REGISTER_COUNT = 100
    help = f'Seeds the database with {REGISTER_COUNT} payables and transactions.'

    
    def handle(self, *args, **options):
        self.seed()
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {self.REGISTER_COUNT} payables and transactions.'))

    @transaction.atomic
    def seed(self):
        if Payable.objects.exists():
            raise CommandError("There are payables on the DB, can't seed.")
        if Transaction.objects.exists():
            raise CommandError("There are transactions on the DB, can't seed.")
        for i in range(self.REGISTER_COUNT):
            random_payment = random.uniform(1000, 2000)
            random_expiration = timezone.now() + timedelta(days=random.randint(-5, 5))
            Payable.objects.create(
                barcode=str(i),
                service_type=(Payable.LIGHT if random.random() > 0.5 else Payable.GAS),
                description=f'Fake payable {i}',
                expiration_date=random_expiration,
                service_import=random_payment,
                payment_status=Payable.PENDING,
            )
            Transaction.objects.create(
                payment_method=random.choice([Transaction.CREDIT_CARD, Transaction.DEBIT_CARD]),
                card_number=f'fake-card-{i}',
                payment_import=random_payment,
                barcode=str(i),
                payment_date=random_expiration + timedelta(days=-1),
            )
