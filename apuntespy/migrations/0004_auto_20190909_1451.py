# Generated by Django 2.2.4 on 2019-09-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuntespy', '0003_auto_20190906_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]