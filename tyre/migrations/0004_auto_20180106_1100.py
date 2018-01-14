# Generated by Django 2.0 on 2018-01-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyre', '0003_auto_20180106_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tyre_issue_to_vehicle',
            name='Nature',
            field=models.CharField(choices=[('Tyre MRN', 'Tyre MRN'), ('Chassis Tyre MRN', 'Chassis Tyre MRN'), ('Remould Tyre MRN', 'Remould Tyre MRN'), ('Tyre against Claim MRN', 'Tyre against Claim MRN'), ('Tyre Claim Rejection MRN', 'Tyre Claim Rejection MRN'), ('Tyre Remould Rejection MRN', 'Tyre Remould Rejection MRN'), ('Tyre Claim Recieved', 'Tyre Claim Recieved'), ('Old Tyre MRN', 'Old Tyre MRN')], max_length=40),
        ),
    ]