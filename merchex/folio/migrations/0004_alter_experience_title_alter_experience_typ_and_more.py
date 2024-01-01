# Generated by Django 5.0 on 2024-01-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0003_remove_experience_task_remove_skill_item_item_skill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='experience',
            name='typ',
            field=models.CharField(choices=[('Emploi', 'Emploi'), ('Travail', 'Travail'), ('Stage', 'Stage'), ('Projet', 'Projet'), ('Implication', 'Implication')], max_length=25),
        ),
        migrations.AlterField(
            model_name='formation',
            name='institution',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='formation',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
