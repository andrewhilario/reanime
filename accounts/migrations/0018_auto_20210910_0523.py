# Generated by Django 3.1.7 on 2021-09-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210909_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rate',
            field=models.IntegerField(choices=[(1, '1 - Horrible'), (2, '2 - Bad'), (3, '3 - OK'), (4, '4 - Good'), (5, '5 - Master Piece')], default=1),
        ),
    ]
