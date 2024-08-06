# Generated by Django 2.2.24 on 2024-08-06 21:18

from django.db import migrations
import phonenumbers as pnum


def normalize_flat_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber_matched = pnum.PhoneNumberMatcher(
            flat.owners_phonenumber,
            'RU'
        )
        is_phonenumber = phonenumber_matched.has_next()
        if not is_phonenumber:
            continue
        parsed_phonenumber = pnum.parse(
            phonenumber_matched.next().raw_string,
            'RU'
        )
        if pnum.is_valid_number(parsed_phonenumber):
            flat.owner_pure_phone = f'+7{parsed_phonenumber.national_number}'
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_alter_flat_who_liked'),
    ]

    operations = [
        migrations.RunPython(normalize_flat_phonenumbers),
    ]
