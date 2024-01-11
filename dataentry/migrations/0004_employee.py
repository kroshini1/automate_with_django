# Generated by Django 5.0 on 2024-01-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0003_alter_csvfile_contactno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retirement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_benefits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_benefits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_compensation', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
