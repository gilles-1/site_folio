# Generated by Django 5.0 on 2024-01-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0004_alter_experience_title_alter_experience_typ_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(max_length=500),
        ),
    ]
