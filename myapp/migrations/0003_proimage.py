# Generated by Django 4.1.2 on 2022-11-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contact_product_pro_price_alter_customer_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='proimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_image', models.ImageField(upload_to='productimages')),
                ('p_price', models.IntegerField()),
            ],
        ),
    ]
