# Generated by Django 3.0.6 on 2020-05-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheckbookApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='ammount',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=60),
        ),
    ]
