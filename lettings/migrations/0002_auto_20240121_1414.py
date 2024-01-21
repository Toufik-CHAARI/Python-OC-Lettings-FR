from django.db import migrations

def transfer_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('lettings', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')

    address_mapping = {}  

    for old_address in OldAddress.objects.all():
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )
        address_mapping[old_address.id] = new_address

    for old_letting in OldLetting.objects.all():
        new_letting_address = address_mapping[old_letting.address_id]
        NewLetting.objects.create(
            title=old_letting.title,
            address=new_letting_address
        )

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),  
        ('oc_lettings_site', '0002_delete_profile'),  
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
