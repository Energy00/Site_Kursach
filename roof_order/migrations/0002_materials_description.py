# Generated by Django 4.0.4 on 2022-06-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roof_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='description',
            field=models.TextField(default='Какое-то описание'),
            preserve_default=False,
        ),
    ]
