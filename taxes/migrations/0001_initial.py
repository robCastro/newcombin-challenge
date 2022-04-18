# Generated by Django 4.0.4 on 2022-04-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payable',
            fields=[
                ('barcode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('service_type', models.CharField(choices=[('L', 'Luz'), ('G', 'Gas')], max_length=2)),
                ('description', models.CharField(max_length=50)),
                ('expiration_date', models.DateField()),
                ('service_import', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_status', models.CharField(choices=[('PE', 'Pending'), ('PA', 'Paid')], max_length=2)),
            ],
            options={
                'verbose_name': 'payable',
                'verbose_name_plural': 'payables',
            },
        ),
    ]
