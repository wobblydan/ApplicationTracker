# Generated by Django 4.1.2 on 2022-12-09 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptrackpages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='testDummy',
            new_name='Client',
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'clients'},
        ),
        migrations.AlterModelTable(
            name='client',
            table='client',
        ),
    ]
