# Generated by Django 4.1.7 on 2023-03-10 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_codregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValoRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(blank=True, max_length=256, null=True)),
                ('leadname', models.CharField(blank=True, max_length=256, null=True)),
                ('leadnumber', models.CharField(blank=True, max_length=256, null=True)),
                ('riotid', models.CharField(blank=True, max_length=256, null=True)),
                ('discordid', models.CharField(blank=True, max_length=256, null=True)),
                ('mem2', models.CharField(blank=True, max_length=256, null=True)),
                ('mem2ph', models.CharField(blank=True, max_length=256, null=True)),
                ('mem2dis', models.CharField(blank=True, max_length=256, null=True)),
                ('mem3', models.CharField(blank=True, max_length=256, null=True)),
                ('mem3dis', models.CharField(blank=True, max_length=256, null=True)),
                ('mem4', models.CharField(blank=True, max_length=256, null=True)),
                ('mem4dis', models.CharField(blank=True, max_length=256, null=True)),
                ('mem5', models.CharField(blank=True, max_length=256, null=True)),
                ('mem5dis', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('college_name', models.CharField(blank=True, max_length=256, null=True)),
                ('event_name', models.CharField(blank=True, max_length=256, null=True)),
                ('year', models.PositiveBigIntegerField(blank=True, null=True)),
                ('payment', models.ImageField(blank=True, null=True, upload_to='valo/')),
            ],
        ),
    ]
