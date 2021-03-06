# Generated by Django 3.1.7 on 2021-09-08 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210909_0227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=2000)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - Horrible'), (2, '2 - Bad'), (3, '3 - OK'), (4, '4 - Good'), (5, '5 - Master Piece')])),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
