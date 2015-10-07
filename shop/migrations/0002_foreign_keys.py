import django
from shop.models import PRODUCT_MODEL, Product
from django.db import models, migrations
from django.conf import settings

__author__ = 'jorutila'
class Migration(migrations.Migration):

    dependencies = [
        #migrations.swappable_dependency(Product),
        ('shop', '0001_initial'),
        ('stables_shop', '0001_initial')
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(Product, verbose_name='Product', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extraorderpricefield',
            name='order',
            field=models.ForeignKey('shop.Order', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='extraorderitempricefield',
            name='order_item',
            field=models.ForeignKey('shop.OrderItem', verbose_name='Order item'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(Product),
        ),
    ]

