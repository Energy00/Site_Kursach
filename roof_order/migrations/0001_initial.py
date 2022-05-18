# Generated by Django 4.0.4 on 2022-05-18 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('photo', models.ImageField(upload_to='media/img/materials_photo/')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('size', models.IntegerField(blank=True)),
                ('photo_roof', models.ImageField(null=True, upload_to='media/img/roof_photo/')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roof_order.materials')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]