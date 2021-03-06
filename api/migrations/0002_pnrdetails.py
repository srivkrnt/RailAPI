# Generated by Django 2.1.3 on 2019-02-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PnrDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnr', models.IntegerField()),
                ('status', models.CharField(max_length=4)),
                ('trainInfo', models.CharField(max_length=60)),
                ('boardingPoint', models.CharField(max_length=40)),
                ('destinationPoint', models.CharField(max_length=40)),
                ('date', models.DateField()),
            ],
        ),
    ]
