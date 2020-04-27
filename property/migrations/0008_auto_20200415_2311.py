# Generated by Django 2.2.4 on 2020-04-15 19:11

from django.db import migrations
import phonenumbers


def set_field_owner_phone_pure(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phonenumber):
            flat.owner_phone_pure = phonenumber
            flat.save()

def set_back_field_owner_phone_pure(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(set_field_owner_phone_pure, set_back_field_owner_phone_pure),
    ]
