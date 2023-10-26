# Generated by Django 4.2.6 on 2023-10-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=20)),
                ('bank_branch', models.CharField(max_length=20)),
                ('IFSC', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='seller/')),
                ('account_number', models.CharField(max_length=20)),
                ('loginid', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=50)),
            ],
            options={
                'db_table': 'seller_tb',
            },
        ),
    ]
