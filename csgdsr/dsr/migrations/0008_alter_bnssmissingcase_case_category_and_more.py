# Generated by Django 5.2.1 on 2025-06-04 02:03

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsr', '0007_rename_date_submitted_bnssmissingcase_submitted_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnssmissingcase',
            name='case_category',
            field=models.CharField(choices=[('194 BNSS', '194 BNSS'), ('Missing', 'Missing')], default='-- Select Category --', max_length=20),
        ),
        migrations.AlterField(
            model_name='csr',
            name='date_of_receipt',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='othercases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_number', models.CharField(max_length=50)),
                ('police_station', models.CharField(max_length=100)),
                ('mps_limit', models.CharField(choices=[('-- Select Police Station --', '-- Select Police Station --'), ('MARINA MPS', 'MARINA MPS'), ('ERNAVUR MPS', 'ERNAVUR MPS'), ('PAZHAVERKADU MPS', 'PAZHAVERKADU MPS'), ('ARAMBAKKAM MPS', 'ARAMBAKKAM MPS'), ('KOVALAM MPS', 'KOVALAM MPS'), ('KALPAKKAM MPS', 'KALPAKKAM MPS'), ('MUTHALIYARKUPPAM MPS', 'MUTHALIYARKUPPAM MPS'), ('MARAKKANAM MPS', 'MARAKKANAM MPS'), ('PUDUKUPPAM MPS', 'PUDUKUPPAM MPS'), ('DEVANAMPATTINAM  MPS', 'DEVANAMPATTINAM MPS'), ('PARANGIPETTAI MPS', 'PARANGIPETTAI MPS'), ('PUDUPATTINAM MPS', 'PUDUPATTINAM MPS'), ('THIRUMULLAIVASAL MPS', 'THIRUMULLAIVASAL MPS'), ('POOMBUHAR MPS', 'POOMBUHAR MPS'), ('THARANGAMBADI MPS', 'THARANGAMBADI MPS'), ('NAGAPATTINAM MPS', 'NAGAPATTINAM MPS'), ('VELANKANNI MPS', 'VELANKANNI MPS'), ('KEELAIYUR MPS', 'KEELAIYUR MPS'), ('VEDARANYAM MPS', 'VEDARANYAM MPS'), ('THERKUKADU MPS', 'THERKUKADU MPS'), ('ADHIRAMAPATTINAM MPS', 'ADHIRAMAPATTINAM MPS'), ('SETHUBAVACHATIRAM MPS', 'SETHUBAVACHATIRAM MPS'), ('MANAMELKUDI MPS', 'MANAMELKUDI MPS'), ('MIMISAL MPS', 'MIMISAL MPS'), ('THIRUPUNAVASAL MPS', 'THIRUPUNAVASAL MPS'), ('THONDI MPS', 'THONDI MPS'), ('DEVIPATTINAM MPS', 'DEVIPATTINAM MPS'), ('ATTRANKARAI MPS', 'ATTRANKARAI MPS'), ('MANDAPAM MPS', 'MANDAPAM MPS'), ('RAMESWARAM MPS', 'RAMESWARAM MPS'), ('PUDUMADAM MPS', 'PUDUMADAM MPS'), ('KEELAKARAI MPS', 'KEELAKARAI MPS'), ('VALINOKKAM MPS', 'VALINOKKAM MPS'), ('VEMBAR MPS', 'VEMBAR MPS'), ('THARUVAIKULAM MPS', 'THARUVAIKULAM MPS'), ('MEENAVAR COLONY MPS', 'MEENAVAR COLONY MPS'), ('THIRUCHENDUR MPS', 'THIRUCHENDUR MPS'), ('KULASEKARAPATTINAM MPS', 'KULASEKARAPATTINAM MPS'), ('UVARI MPS', 'UVARI MPS'), ('KOODANKULAM MPS', 'KOODANKULAM MPS'), ('KANNIYAKUMARI MPS', 'KANNIYAKUMARI MPS'), ('COLACHEL MPS', 'COLACHEL MPS')], default='-- Select Police Station --', max_length=100)),
                ('date_of_occurrence', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_of_receipt', models.DateTimeField(default=django.utils.timezone.now)),
                ('place_of_occurrence', models.CharField(max_length=200)),
                ('petitioner', models.CharField(max_length=100)),
                ('diseased', models.CharField(blank=True, max_length=200, null=True)),
                ('injured', models.CharField(blank=True, max_length=200, null=True)),
                ('accused', models.CharField(blank=True, max_length=200, null=True)),
                ('gist_of_case', models.TextField()),
                ('io', models.CharField(blank=True, max_length=100, null=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
