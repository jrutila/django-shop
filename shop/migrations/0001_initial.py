# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from shop.models import Product
import shop.util.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Cart',
                'abstract': False,
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(to='shop.Cart', related_name='items')),
            ],
            options={
                'verbose_name': 'Cart item',
                'abstract': False,
                'verbose_name_plural': 'Cart items',
            },
        ),
        migrations.CreateModel(
            name='ExtraOrderItemPriceField',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('label', models.CharField(verbose_name='Label', max_length=255)),
                ('value', shop.util.fields.CurrencyField(verbose_name='Amount', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('data', jsonfield.fields.JSONField(verbose_name='Serialized extra data', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Extra order item price field',
                'verbose_name_plural': 'Extra order item price fields',
            },
        ),
        migrations.CreateModel(
            name='ExtraOrderPriceField',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('label', models.CharField(verbose_name='Label', max_length=255)),
                ('value', shop.util.fields.CurrencyField(verbose_name='Amount', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('data', jsonfield.fields.JSONField(verbose_name='Serialized extra data', null=True, blank=True)),
                ('is_shipping', models.BooleanField(verbose_name='Is shipping', editable=False, default=False)),
            ],
            options={
                'verbose_name': 'Extra order price field',
                'verbose_name_plural': 'Extra order price fields',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('status', models.IntegerField(verbose_name='Status', choices=[(10, 'Processing'), (20, 'Confirming'), (30, 'Confirmed'), (40, 'Completed'), (50, 'Shipped'), (60, 'Canceled')], default=10)),
                ('order_subtotal', shop.util.fields.CurrencyField(verbose_name='Order subtotal', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('order_total', shop.util.fields.CurrencyField(verbose_name='Order Total', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('shipping_address_text', models.TextField(verbose_name='Shipping address', null=True, blank=True)),
                ('billing_address_text', models.TextField(verbose_name='Billing address', null=True, blank=True)),
                ('created', models.DateTimeField(verbose_name='Created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Updated', auto_now=True)),
                ('cart_pk', models.PositiveIntegerField(verbose_name='Cart primary key', null=True, blank=True)),
                ('user', models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Order',
                'abstract': False,
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='Extra info', blank=True)),
                ('order', models.ForeignKey(verbose_name='Order', related_name='extra_info', to='shop.Order')),
            ],
            options={
                'verbose_name': 'Order extra info',
                'verbose_name_plural': 'Order extra info',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('product_reference', models.CharField(verbose_name='Product reference', max_length=255)),
                ('product_name', models.CharField(verbose_name='Product name', null=True, max_length=255, blank=True)),
                ('unit_price', shop.util.fields.CurrencyField(verbose_name='Unit price', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('line_subtotal', shop.util.fields.CurrencyField(verbose_name='Line subtotal', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('line_total', shop.util.fields.CurrencyField(verbose_name='Line total', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('order', models.ForeignKey(verbose_name='Order', related_name='items', to='shop.Order')),
            ],
            options={
                'verbose_name': 'Order item',
                'abstract': False,
                'verbose_name_plural': 'Order items',
            },
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('amount', shop.util.fields.CurrencyField(verbose_name='Amount', max_digits=30, default=Decimal('0.0'), decimal_places=2)),
                ('transaction_id', models.CharField(verbose_name='Transaction ID', max_length=255, help_text="The transaction processor's reference")),
                ('payment_method', models.CharField(verbose_name='Payment method', max_length=255, help_text='The payment backend used to process the purchase')),
                ('order', models.ForeignKey(verbose_name='Order', to='shop.Order')),
            ],
            options={
                'verbose_name': 'Order payment',
                'verbose_name_plural': 'Order payments',
            },
        ),
    ]
