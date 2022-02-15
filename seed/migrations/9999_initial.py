from django.db import migrations

from accounts.gen_master_data import gen_master as accounts_gen_master
from markets.gen_master_data import gen_master as markets_gen_master
from products.gen_master_data import gen_master as products_gen_master
from qna.gen_master_data import gen_master as qna_gen_master


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('cart', '__latest__'),
        ('qna', '__latest__'),
        ('summernote_support', '__latest__'),
    ]

    operations = [
        migrations.RunPython(accounts_gen_master),
        migrations.RunPython(markets_gen_master),
        migrations.RunPython(products_gen_master),
        migrations.RunPython(qna_gen_master),
    ]
