# Generated by Django 3.1.7 on 2021-03-29 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0003_auto_20210329_0538'),
        ('order', '0002_auto_20210329_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='courier.courier'),
        ),
    ]
